inputLines = open("input14.txt").readlines()

def totalLoad(platform):
    total = 0
    for i in range(len(platform)):
        total += platform[i].count("O") * (len(platform)-i)
    return total

def tiltNS(platform,north=True):
    for col in range(len(platform[0])):
        solidIndex = 0 if north else len(platform)-1
        iterRange = range(len(platform)) if north else range(len(platform)-1,-1,-1)
        for i in iterRange:
            if platform[i][col] == ".":
                continue
            elif platform[i][col] == "#":
                solidIndex = i + 2*north -1
            else:
                platform[i] = platform[i][:col] + "." + platform[i][col+1:]
                platform[solidIndex] = platform[solidIndex][:col] + "O" + platform[solidIndex][col+1:]
                solidIndex += 2*north -1

def tiltWE(platform,west=True):
    for row in range(len(platform)):
        solidIndex = 0 if west else len(platform[0])-1
        iterRange = range(len(platform[0])) if west else range(len(platform[0])-1,-1,-1)
        for i in iterRange:
            if platform[row][i] == ".":
                continue
            elif platform[row][i] == "#":
                solidIndex = i + 2*west -1
            else:
                platform[row] = platform[row][:i] + "." + platform[row][i+1:]
                platform[row] = platform[row][:solidIndex] + "O" + platform[row][solidIndex+1:]
                solidIndex += 2*west -1

def applySpinCycle(platform):
    tiltNS(platform)
    tiltWE(platform)
    tiltNS(platform, north=False)
    tiltWE(platform, west=False)

def partA(lines):
    platform = [l.strip() for l in lines]
    tiltNS(platform)
    return totalLoad(platform)

def partB(lines, cycles):
    platform = [l.strip() for l in lines]
    pastPlatforms = []
    
    lookingForRepeat = True
    while lookingForRepeat:
        currentPlatform = tuple(platform)
        if pastPlatforms.count(currentPlatform):
            lookingForRepeat = False
        else:
            applySpinCycle(platform)
            pastPlatforms.append(currentPlatform)
    
    repeatIndex = pastPlatforms.index(currentPlatform)
    patternLength = len(pastPlatforms)-repeatIndex

    lastPlatformIndex = (cycles-repeatIndex) % patternLength
    return totalLoad(pastPlatforms[lastPlatformIndex+ repeatIndex])

print(partA(inputLines))
print(partB(inputLines,1000000000))

#example = [
#    "O....#....",
#    "O.OO#....#",
#    ".....##...",
#    "OO.#O....O",
#    ".O.....O#.",
#    "O.#..O.#.#",
#    "..O..#O..O",
#    ".......O..",
#    "#....###..",
#    "#OO..#...."
#]
#
#print(partA(example))
#print(partB(example,1000000000))

#south = tiltNS(example,north=False)
#for i in south:
#    print(i)
#print()
#north = tiltNS(example)
#for i in north:
#    print(i)
#print()
#east = tiltWE(example,west=False)
#for i in east:
#    print(i)
#print()
#west = tiltWE(example)
#for i in west:
#    print(i)