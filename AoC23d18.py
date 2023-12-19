inputLines = open("input18.txt").readlines()

indexedMoves = ("R","D","L","U")
moves = {
    "U":(-1,0),
    "D":(1,0),
    "L":(0,-1),
    "R":(0,1),
}

def findInsidePoints(edges: set,mapRows: [int],mapCols: [int]) -> set:
    insidePoints = set()
    for row in range(mapRows[0]+1,mapRows[1]-1):
        intersections = 0
        col = mapCols[0]
        while col < mapCols[1]:
            if (row,col) in edges:
                needBottom = True if (row-1,col) in edges else False
                testCol = col
                while (row, testCol) in edges:
                    testCol += 1
                col = testCol-1
                if (not needBottom) and (row-1,col) in edges:
                    intersections += 1
                elif needBottom and (row+1,col) in edges:
                    intersections += 1
            elif intersections % 2 == 1:
                insidePoints.add((row,col))
            col += 1
    return insidePoints

def partA(lines):
    instructions = [l.strip().split(" ") for l in lines]
    edges = set()
    pos = [0,0]
    rowRange = [0,1]
    colRange = [0,1]
    for step in instructions:
        for _ in range(int(step[1])):
            pos[0] += moves[step[0]][0]
            pos[1] += moves[step[0]][1]
            if pos[0] == rowRange[1]:
                rowRange[1] += 1
            elif pos[0] < rowRange[0]:
                rowRange[0] -= 1
            if pos[1] == colRange[1]:
                colRange[1] += 1
            elif pos[1] < colRange[0]:
                colRange[0] -= 1
            edges.add((pos[0],pos[1]))

    insides = findInsidePoints(edges, rowRange, colRange)

    with open("d18Aoutput.txt", "w") as f:
        for row in range(*rowRange):
            rowString = ""
            for col in range(*colRange):
                if (row,col) in edges:
                    rowString += "#"
                elif (row,col) in insides:
                    rowString += "@"
                else:
                    rowString += "."
            print(rowString,file=f)

    return len(edges) + len(insides)


### Well, I should have looked at the solution sooner
# it turns out there's a mathematical formula for the area of a polygon
# given its points. So, instead of trying flux and range math,
# using a formula will always be faster
# HyperNeutrino
# https://youtu.be/bGWK76_e-LM?si=nfYiJ4PQ4ncImken
# Shoelace Formula and Pick's Theorem
# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem
def partB(lines):
    points = [(0,0)]
    b = 0
    for line in lines:
        line = line.split()[-1]
        length = int(line[2:-2], 16)
        direction = moves[indexedMoves[int(line[-2])]]
        r, c = points[-1]
        b += length
        points.append((r+direction[0]*length, c+direction[1]*length))

    A = abs(sum(points[i][0]*(points[i-1][1] - points[(i+1)%len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1
    return i+b
    #instructions = [l.strip().split(" ")[2] for l in lines]
    #vertLines, horiLines = instructionsToLines(instructions)
    #return areaFromEdges(vertLines, horiLines)

print(partA(inputLines))
print(partB(inputLines))

#example = [
#    "R 6 (#70c710)\n",
#    "D 5 (#0dc571)\n",
#    "L 2 (#5713f0)\n",
#    "D 2 (#d2c081)\n",
#    "R 2 (#59c680)\n",
#    "D 2 (#411b91)\n",
#    "L 5 (#8ceee2)\n",
#    "U 2 (#caa173)\n",
#    "L 1 (#1b58a2)\n",
#    "U 2 (#caa171)\n",
#    "R 2 (#7807d2)\n",
#    "U 3 (#a77fa3)\n",
#    "L 2 (#015232)\n",
#    "U 2 (#7a21e3)\n"
#]

#print(partA(example))
#print(partB(example))

#def instructionsToLines(instructions):
#    verticalLines = []
#    horizontalLines = []
#    pos = [0,0]
#    for instruct in instructions:
#        length = int(instruct[2:-2], 16)
#        direction = indexedMoves[int(instruct[-2])]
#        if moves[direction][1]==0:
#            #Vertical
#            newVert = moves[direction][0]*length + pos[0]
#            #col, startRow, endRow
#            verticalLines.append((pos[1],min(pos[0],newVert),max(pos[0],newVert)))
#            pos[0] = newVert
#        else:
#            #Horizontal
#            newHori = moves[direction][1]*length + pos[1]
#            #row, startCol, endCol
#            horizontalLines.append((pos[0],min(pos[1],newHori),max(pos[1],newHori)))
#            pos[1] = newHori
#
#    return verticalLines, horizontalLines
#
#def areaFromEdges(verticalLines, horizontalLines):
#    lines = sorted(horizontalLines,key=lambda line: line[1])
#    for l in lines:
#        print(l)
#    #activeLines = [lines.pop(0)]
#    #print(activeLines)
#    #while lines:
#    #    height, start, end = lines.pop(0)
#    #    for active in activeLines:
#    return 0