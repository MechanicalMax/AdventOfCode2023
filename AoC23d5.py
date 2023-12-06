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
    
    # Credit for this logic goes to HyperNeutrino,
    # I was still able to use my data structures,
    # But the range math is from
    # https://www.youtube.com/watch?v=NmxHw_bHhGM
    # I tried to understand everything first instead
    # of blindly copying.

    # Strategy:
    # For every seed map
    for seedMap in maps:
        # keep track of ranges already mapped
        mappedSeeds = []
        # while there are still ranges to be mapped
        while len(seedRanges) > 0:
            # Get a range start and end from seedRanges
            start, end = seedRanges.pop()
            # For every range in the map
            for rangeInfo in seedMap:
                # Check for overlap endpoints
                overlapStart = max(start, rangeInfo[1])
                overlapEnd = min(end, rangeInfo[1] + rangeInfo[2])
                # If there is a valid overlap
                if overlapStart < overlapEnd:
                    # Map the overlap and save in mapped seeds
                    mappedSeeds.append((overlapStart + rangeInfo[0] - rangeInfo[1], overlapEnd + rangeInfo[0] - rangeInfo[1]))
                    ## Check if there needs to be an additional range checked in seedRanges
                    #current start is within start
                    if overlapStart > start:
                        seedRanges.append((start, overlapStart))
                    #current end is within end
                    if overlapEnd < end:
                        seedRanges.append((overlapEnd, end))
                    break
            else:
                # if nothing else applies, it is out of range
                # So, don't apply a transformation to current
                # and save to mapped seeds
                mappedSeeds.append((start,end))
        # set mapped seeds to seedRanges to repeat process
        seedRanges = mappedSeeds

    # Lowest possible seed will be the minimum value of the lowest range
    lowest = sorted(seedRanges)[0][0]
    
    return lowest

print(partA(inputLines))
print(partB(inputLines)) ## Too much to optimize during finals; Thank you HyperNeutrino for the help!