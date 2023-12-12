inputLines = open("input12.txt").readlines()

def getRowInfo(lines):
    info = []
    for row in lines:
        row = row.strip().split(" ")
        row[1] = [int(x) for x in row[1].split(",")]
        info.append(row)
    return info

def getFoldedInfo(lines):
    info = getRowInfo(lines)
    for item in info:
        item[0] += 4*("?" + item[0])
        item[1] = tuple(item[1] * 5)
    return info

def validArrangement(row, groupSizes) -> bool:
    if row.count("#") != sum(groupSizes):
        return False
    row = [damaged for damaged in row.split(".") if damaged]
    if len(row) != len(groupSizes):
        return False
    for index, group in enumerate(row):
        if len(group) == groupSizes[index]:
            continue
        else:
            return False
    return True

def getPermutations(row, groupSizes):
    perms = set()
    questionMarks = row.count("?")
    brokenSprings = row.count("#")
    requiredExtraSprings = sum(groupSizes)-brokenSprings

    for i in range(2**questionMarks):
        binPerm = format(i, f'0{questionMarks}b')
        if requiredExtraSprings != binPerm.count("1"):
            continue
        arrangement = ""
        markIndex = 0
        for char in row:
            if char != "?":
                arrangement += char
                continue
            arrangement += "#" if binPerm[markIndex] == "1" else "."
            markIndex += 1
        if validArrangement(arrangement, groupSizes):
            perms.add(arrangement)

    return perms

def partA(lines):
    total = 0
    rows = getRowInfo(lines)

    for row in rows:
        permutations = getPermutations(row[0], row[1])
        total += len(permutations)

    return total

# Thanks again to Hyper-Neutrino for the fast version
# of solving this problem for Part B
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day12p2.py

def smartPermutations(row, groupSizes, cache):
    if row == "":
        return 1 if groupSizes == () else 0
    
    if groupSizes == ():
        return 0 if "#" in row else 1
    
    key = (row, groupSizes)

    if key in cache:
        return cache[key]
    
    result = 0

    if row[0] in ".?":
        result += smartPermutations(row[1:], groupSizes, cache)
    
    if row[0] in "#?":
        if groupSizes[0] <= len(row) and "." not in row[:groupSizes[0]] and (groupSizes[0]==len(row) or row[groupSizes[0]] != "#"):
            result += smartPermutations(row[groupSizes[0]+1:], groupSizes[1:],cache)

    cache[key] = result
    return result

def partB(lines):
    total = 0
    cache = {}
    rows = getFoldedInfo(lines)

    for row in rows:
        total += smartPermutations(row[0], tuple(row[1]), cache)
        
    return total

#examples = [
#    ".# 1",
#    "???.### 1,1,3",
#    ".??..??...?##. 1,1,3",
#    "?#?#?#?#?#?#?#? 1,3,1,6",
#    "????.#...#... 4,1,1",
#    "????.######..#####. 1,6,5",
#    "?###???????? 3,2,1"
#]

#print(partB(examples))

print(partA(inputLines))
print(partB(inputLines))