import sympy
inputLines = open("input24.txt").read().splitlines()

def parseStones(lines):
    stones = []
    for l in lines:
        pos, vel = l.split(" @ ")
        pos = tuple(map(float,pos.split(", ")))
        vel = tuple(map(float,vel.split(", ")))
        stones.append({"pos":pos,"vel":vel})
    return stones

def findXYIntersection(a, b):
    # y = a[vel][1]/a[vel][0](x-a[pos][0]) + a[pos][1]
    # y = b[vel][1]/b[vel][0](x-b[pos][0]) + b[pos][1]
    aSlope = a["vel"][1]/a["vel"][0]
    bSlope = b["vel"][1]/b["vel"][0]
    if aSlope == bSlope:
        return(-1,-1)
    
    x = (-aSlope*a["pos"][0]+a["pos"][1]+bSlope*b["pos"][0]-b["pos"][1]) / (bSlope-aSlope)
    if (x > a["pos"][0] and a["vel"][0] < 0) or (x < a["pos"][0] and a["vel"][0] > 0):
        return(-1,-1)
    elif (x > b["pos"][0] and b["vel"][0] < 0) or (x < b["pos"][0] and b["vel"][0] > 0):
        return(-1,-1)

    y = aSlope*(x-a["pos"][0]) + a["pos"][1]

    return (x,y)

# Solved Part A :D
def partA(lines, minPos=200000000000000, maxPos=400000000000000):
    stones = parseStones(lines)
    total = 0

    for a, stoneA in enumerate(stones[:-1]):
        for stoneB in stones[a+1:]:
            cross = findXYIntersection(stoneA,stoneB)
            if minPos <= cross[0] <= maxPos and minPos <= cross[1] <= maxPos:
                total += 1

    return total

# Attempted to solve my own equations, but after watching the solution
# video for a hint, I decided not to reinvent the wheel
# Simpy seems like a good library for solving equations (CAS)
# https://www.youtube.com/watch?v=guOyA7Ijqgk
def partB(lines):
    stones = parseStones(lines)
    # intersects at posR + velR*t = posS + velS*t
    # t*(velR - velS) = posS - posR
    # t = (posS - posR)/(velR - velS)
    # this is a vector equation, so values for componets equal t
    # t = (posSX - posRX)/(velRX - velSX) = (posSY - posRY)/(velRY - velSY) = (posSZ - posRZ)/(velRZ - velSZ)
    # this gives us a system of equations with six unknowns (posR[XYZ] and velR[XYZ])
    # (posSX-posRX)(velRY-velSY) - (posSY-posRY)(velRX-velSX) = 0
    posRX, posRY, posRZ, velRX, velRY, velRZ = sympy.symbols("posRX, posRY, posRZ, velRX, velRY, velRZ")

    equations = []

    for numEquations, stone in enumerate(stones):
        equations.append((posRX-stone["pos"][0])*(stone["vel"][1]-velRY) - (posRY - stone["pos"][1])*(stone["vel"][0]-velRX))
        equations.append((posRY-stone["pos"][1])*(stone["vel"][2]-velRZ) - (posRZ - stone["pos"][2])*(stone["vel"][1]-velRY))
        if numEquations < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break

    return int(answers[0][posRX] + answers[0][posRY] + answers[0][posRZ])

print(partA(inputLines))
print(partB(inputLines))

#example = (
#    "19, 13, 30 @ -2,  1, -2\n",
#    "18, 19, 22 @ -1, -1, -2\n",
#    "20, 25, 34 @ -2, -2, -4\n",
#    "12, 31, 28 @ -1, -2, -1\n",
#    "20, 19, 15 @  1, -5, -3\n"
#)
#
#print(partA(example,7,27))
#print(partB(example))