inputLines = open("input11.txt").readlines()

def getGalaxyCoords(lines):
    coords = []
    for row in range(0,len(lines)):
        for col in range(0,len(lines[0])):
            if lines[row][col] == "#":
                coords.append([row,col])

    return coords

def getEmptyRows(lines):
    emptyRows = []
    for row in range(0,len(lines)):
        for item in lines[row]:
            if item == "#":
                break
        else:
            emptyRows.append(row)

    return emptyRows

def getEmptyCols(lines):
    emptyCols = []
    for col in range(0,len(lines[0])):
        for row in range(0, len(lines)):
            if lines[row][col] == "#":
                break
        else:
            emptyCols.append(col)

    return emptyCols

def coordDistance(coordA, coordB):
    distance = abs(coordA[0]-coordB[0]) + abs(coordA[1]-coordB[1])
    return distance

def sumMinPairDistances(coords):
    total = 0
    pairStartIndex = 0
    while pairStartIndex < len(coords)-1:
        for i in range(pairStartIndex+1, len(coords)):
            total += coordDistance(coords[pairStartIndex], coords[i])
        pairStartIndex += 1

    return total

def partA(lines):
    galaxyCoords = getGalaxyCoords(lines)
    eRows = getEmptyRows(lines)
    eCols = getEmptyCols(lines)

    for index, empty in enumerate(eRows):
        for coord in galaxyCoords:
            if coord[0] > empty+index:
                coord[0] += 1

    for index, empty in enumerate(eCols):
        for coord in galaxyCoords:
            if coord[1] > empty+index:
                coord[1] += 1

    return sumMinPairDistances(galaxyCoords)

def partB(lines, expansionMultiplier):
    galaxyCoords = getGalaxyCoords(lines)
    eRows = getEmptyRows(lines)
    eCols = getEmptyCols(lines)

    for index, empty in enumerate(eRows):
        for coord in galaxyCoords:
            if coord[0] > empty+index*(expansionMultiplier-1):
                coord[0] += expansionMultiplier-1

    for index, empty in enumerate(eCols):
        for coord in galaxyCoords:
            if coord[1] > empty+index*(expansionMultiplier-1):
                coord[1] += expansionMultiplier-1

    return sumMinPairDistances(galaxyCoords)

#example = [
#"...#......",
#".......#..",
#"#.........",
#"..........",
#"......#...",
#".#........",
#".........#",
#"..........",
#".......#..",
#"#...#....."
#]
#
#print(partA(example))
#print(partB(example,10))
#print(partB(example,100))
#print()

print(partA(inputLines))
print(partB(inputLines,1000000))