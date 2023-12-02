inputLines = open("input2.txt").readlines()

def partA(lines):
    total = sum(range(1,101))
    bagContents = (("d",12),("g",13),("b",14))

    for i, line in enumerate(lines):
        line = line[line.find(":")+2:]
        hands = line.split("; ")
        notPossible = False
        for hand in hands:
            cubeDescriptions = hand.strip().split(", ")
            for cube in cubeDescriptions:
                for cubeTotal in bagContents:
                    if cube.find(cubeTotal[0]) != -1:
                        drawnCubes = int(cube[:cube.find(" ")])
                        if drawnCubes > cubeTotal[1]:
                            notPossible = True
        
        if notPossible:
            total -= i+1

    return total

def partB(lines):
    total = 0

    for line in lines:
        minimums = [["d",0],["g",0],["b",0]]
        line = line[line.find(":")+2:]
        hands = line.split("; ")

        for hand in hands:
            cubeDescriptions = hand.strip().split(", ")
            for cube in cubeDescriptions:
                for cubeTotal in minimums:
                    if cube.find(cubeTotal[0]) != -1:
                        drawnCubes = int(cube[:cube.find(" ")])
                        if drawnCubes > cubeTotal[1]:
                            cubeTotal[1] = drawnCubes
        
        power = 1
        for val in minimums:
            power *= val[1]

        total += power

    return total

print(partA(inputLines))
print(partB(inputLines))