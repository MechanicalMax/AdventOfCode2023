from collections import deque
inputLines = open("input22.txt").readlines()

# It's getting too close to Christmas so I need to start
# going straight to the solutions.
# https://youtu.be/imz7uexX394?si=CElZLVKNvMI2vINK

# Yeah, this problem would take me far too long on my own

def getBricks(lines):
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in lines]
    bricks.sort(key=lambda b: b[2])
    return bricks

# Interesting range math for overlapping rectangles
def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

def getKVSupports(bricks):
    for i, brick in enumerate(bricks):
        minZ = 1
        for prevBrick in bricks[:i]:
            if overlaps(brick, prevBrick):
                minZ = max(minZ, prevBrick[5] + 1)
        brick[5] -= brick[2] - minZ
        brick[2] = minZ

    bricks.sort(key=lambda b: b[2])

    kSupportsv = {i:set() for i in range(len(bricks))}
    vSupportsk = {i:set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] +1:
                kSupportsv[i].add(j)
                vSupportsk[j].add(i)

    return kSupportsv, vSupportsk

def partA(lines):
    bricks = getBricks(lines)
    kSupportsv, vSupportsk = getKVSupports(bricks)
    
    total = 0

    for i in range(len(bricks)):
        if all(len(vSupportsk[j]) >= 2 for j in kSupportsv[i]):
            total += 1

    return total

def partB(lines):
    bricks = getBricks(lines)
    kSupportsv, vSupportsk = getKVSupports(bricks)
    
    total = 0
    
    for i in range(len(bricks)):
        q = deque(j for j in kSupportsv[i] if len(vSupportsk[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            # Use some set opperations
            for k in kSupportsv[j] - falling:
                if vSupportsk[k] <= falling:
                    q.append(k)
                    falling.add(k)
        total += len(falling) - 1

    return total

print(partA(inputLines))
print(partB(inputLines))