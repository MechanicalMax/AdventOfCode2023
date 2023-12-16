inputLines = open("input16.txt").readlines()

directions = {
    "N": (-1,0),
    "S": (1,0),
    "E": (0,1),
    "W": (0,-1)
}

parts = {
    ".": {
        "N":("N"),
        "S":("S"),
        "E":("E"),
        "W":("W"),
    },
    "/": {
        "N":("E"),
        "S":("W"),
        "W":("S"),
        "E":("N")
    },
    "\\": {
        "N":("W"),
        "S":("E"),
        "W":("N"),
        "E":("S")
    },
    "|": {
        "N":("N"),
        "S":("S"),
        "W":("N", "S"),
        "E":("N", "S")
    },
    "-": {
        "E":("E"),
        "W":("W"),
        "N":("E", "W"),
        "S":("E", "W")
    }
}

def moveDirection(row,col,direction,contraption):
    newRow = row + directions[direction][0]
    newCol = col + directions[direction][1]
    if 0 <= newRow < len(contraption) and 0 <= newCol < len(contraption[0]):
        return newRow, newCol
    return False

def sumEnergized(contraption,start):
    energized = set()
    lightEnds = [start]
    while lightEnds:
        row, col, direction = lightEnds.pop()
        newPos = moveDirection(row, col, direction, contraption)
        if not newPos:
            continue

        curPart = contraption[newPos[0]][newPos[1]]
        for newDirection in parts[curPart][direction]:
            if (newPos[0],newPos[1],newDirection) not in energized:
                energized.add((newPos[0],newPos[1],newDirection))
            else:
                continue
            lightEnds.append((newPos[0],newPos[1], newDirection))

    energizedPoints = set()
    for item in energized:
        energizedPoints.add((item[0],item[1]))
    return len(energizedPoints)

def partA(lines):
    contraption = tuple([l.strip() for l in lines])
    return sumEnergized(contraption, (0,-1,"E"))

def partB(lines):
    contraption = tuple([l.strip() for l in lines])
    maxTotal = 0
    
    for row in range(len(contraption)):
        maxTotal = max(maxTotal, sumEnergized(contraption,(row,-1,"E")))
        maxTotal = max(maxTotal, sumEnergized(contraption,(row,len(contraption[0]),"W")))
    for col in range(len(contraption[0])):
        maxTotal = max(maxTotal, sumEnergized(contraption,(-1,col,"S")))
        maxTotal = max(maxTotal, sumEnergized(contraption,(len(contraption),col,"N")))
    
    return maxTotal

print(partA(inputLines))
print(partB(inputLines))

#example = [
#".|...\....",
#"|.-.\.....",
#".....|-...",
#"........|.",
#"..........",
#".........\\",
#"..../.\\\\..",
#".-.-/..|..",
#".|....-|.\\",
#"..//.|...."
#]