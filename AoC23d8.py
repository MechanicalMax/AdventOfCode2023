from math import lcm
inputLines = open("input8.txt").readlines()

def getCleanInput(lines):
    instructions = lines[0].strip()
    nodes = {}
    for line in lines[2:]:
        name = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[name] = (left,right)
    return instructions, nodes

def partA(lines):
    steps = 0
    instructions, nodes = getCleanInput(lines)
    instructLen = len(instructions)
    currentNode = "AAA"
    while currentNode != "ZZZ":
        nextDirection = 1 if instructions[steps%instructLen] == "R" else 0
        currentNode = nodes[currentNode][nextDirection]
        steps += 1

    return steps

def findStepsFromNode(currentNode, nodes, instructions, instructLen):
    steps = 0
    while currentNode[2] != "Z":
        nextDirection = 1 if instructions[steps%instructLen] == "R" else 0
        currentNode = nodes[currentNode][nextDirection]
        steps += 1
    return steps

def partB(lines):
    totalSteps = 0
    instructions, nodes = getCleanInput(lines)
    instructLen = len(instructions)
    startNodes = []

    for node in nodes.keys():
        if node[2] == "A":
            startNodes.append(node)

    ghostSteps = []

    # At first I thought there might be multiple paths to get to Z after
    # you get to Z the first time. This loop was supposed to get all the
    # different distances. But, when I saw there was only one distance in
    # all the lists, I knew it was just the least common multiple for the
    # number of steps
    for node in startNodes:
        ghostSteps.append([])

        steps = findStepsFromNode(node, nodes, instructions, instructLen)
        while steps not in ghostSteps[-1]:
            ghostSteps[-1].append(steps)
            steps = findStepsFromNode(node, nodes, instructions, instructLen)

    totalSteps = lcm(*[x[0] for x in ghostSteps])
    return totalSteps

print(partA(inputLines))
print(partB(inputLines))