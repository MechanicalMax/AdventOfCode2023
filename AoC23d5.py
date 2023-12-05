inputLines = open("input5.txt").readlines()

def getMapInfo(mapLines):
    maps = []

    for line in mapLines:
        if line == "\n":
            maps.append([])
        elif line[0].isnumeric():
            rangeInfo = line.strip().split(" ")
            rangeInfo = [int(x) for x in rangeInfo]
            maps[-1].append(tuple(rangeInfo))

    for map in maps:
        map.sort()

    return maps

def getGraph(maps):
    graph =  {}



    return graph

def partA(lines):
    lowest = 1000000000000000
    seeds = lines[0][7:].strip().split(" ")
    seeds = [int(x) for x in seeds]

    maps = getMapInfo(lines)
    for locationNum in seeds:
        for map in maps:
            for rangeInfo in map:
                if locationNum in range(rangeInfo[1],rangeInfo[1]+rangeInfo[2]):
                    locationNum += rangeInfo[0]-rangeInfo[1]
                    break
        if locationNum < lowest:
            lowest = locationNum

    return lowest

def partB(lines):
    seeds = lines[0][7:].strip().split(" ")
    seedRanges = []
    while len(seeds) != 0:
        items = int(seeds.pop())
        start = int(seeds.pop())
        seedRanges.append((start,start+items))
    seedRanges.sort()
    
    maps = getMapInfo(lines)
    graph = getGraph(maps)
    
    #foundSeed = False
#
    #while not foundSeed:
    #for curMap in reversed(maps):
    #    for rangeInfo in curMap:
    #        print(f"\tInput: {rangeInfo[1]} to {rangeInfo[1]+rangeInfo[2]-1}")
    #        print(f"\t\tOutput: {rangeInfo[0]} to {rangeInfo[0]+rangeInfo[2]-1}")
    #        if goalNum in range(rangeInfo[0],rangeInfo[0]+rangeInfo[2]):
    #            goalNum = rangeInfo[1]
    #    print("Next Map=")
    #    print(goalNum)
#
    #for i in seedRanges:
    #    print(i)
        
    return graph

print(partA(inputLines))
print(partB(inputLines)) ## Too much to optimize during finals