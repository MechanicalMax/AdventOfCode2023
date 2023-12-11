inputLines = open("input10.txt").readlines()

#exampleInput = [
#"FF7FSF7F7F7F7F7F---7",
#"L|LJ||||||||||||F--J",
#"FL-7LJLJ||||||LJL-77",
#"F--JF--7||LJLJ7F7FJ-",
#"L---JF-JLJ.||-FJLJJ7",
#"|F|F-JF---7F7-L7L|7|",
#"|FFJF7L7F-JF7|JL---7",
#"7-L-JL7||F7|L7F-7F7|",
#"L.L7LFJ|||||FJL7||LJ",
#"L7JLJL-JLJLJL--JLJ.L"
#]

loopPoints = set()

directionOpposites = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}

directionTransformations = {
    "N": (-1,0),
    "S": (1,0),
    "E": (0,1),
    "W": (0,-1)
}

pipeTypes = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("W", "S"),
    "F": ("E", "S"),
    ".": ()
}

inBends = ("F", "L")
outBends = ("J", "7")

def findStartPos(lines):
    pos = [0,0]
    for row in range(len(lines)):
        pos[0] = row
        for col in range(len(lines[0])):
            pos[1] = col
            if lines[row][col] == "S":
                return pos

def partA(lines):
    steps = 1
    pos = findStartPos(lines)
    lastDir = ""
    currentPipe = "S"
    
    #Find a valid next pipe
    for direction in directionTransformations:
        trans = directionTransformations[direction]
        guessPos = [pos[0]+trans[0],pos[1]+trans[1]]
        if directionOpposites[direction] in pipeTypes[lines[guessPos[0]][guessPos[1]]]:
            lastDir = direction
            pos = guessPos
            currentPipe = lines[pos[0]][pos[1]]
            break

    #Follow pipe until "S" reached again
    while True:
        currentPipe = lines[pos[0]][pos[1]]
        loopPoints.add(tuple(pos))
        if currentPipe == "S":
            break
        nextDirection = pipeTypes[currentPipe][1] if pipeTypes[currentPipe][0] == directionOpposites[lastDir] else pipeTypes[currentPipe][0]
        pos = [pos[0] + directionTransformations[nextDirection][0], pos[1] + directionTransformations[nextDirection][1]]
        steps += 1
        lastDir = nextDirection

    return int(steps/2)

def partB(lines):
    # Similar to flux, check if the number of boundary crosses
    # is even or odd. If the number of intersections is
    # odd, the point is inside. Else, it is outside
    # Note: This may not work for all points because this
    # function does not check for what type of pipe "S" acts
    # as. Add something to replace "S" for its equivalent pipe
    # in the input if this does not work. This still got me two
    # stars today though!
    insideTiles = 0

    pos = [0,0]
    curIntersections = 0
    for row in range(len(lines)):
        pos[0] = row
        for col in range(len(lines[0])):
            pos[1] = col
            if tuple(pos) not in loopPoints:
                curIntersections = 0
                searchForEndBend = False
                searchEndBendType = 0

                for fluxCol in range(col+1,len(lines[0])):
                    pipe = lines[row][fluxCol]
                    if (row,fluxCol) in loopPoints:
                        if pipe == "|":
                            curIntersections += 1
                            continue
                        if searchForEndBend:
                            if pipe in outBends:
                                searchForEndBend = False
                                if pipe == outBends[searchEndBendType]:
                                    curIntersections += 1
                                continue
                        if pipe in inBends:
                            searchEndBendType = inBends.index(pipe)
                            searchForEndBend = True
                if curIntersections % 2 == 1:
                    insideTiles += 1           

    return insideTiles

print(partA(inputLines))
print(partB(inputLines))