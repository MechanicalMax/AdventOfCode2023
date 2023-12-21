from collections import deque
inputLines = open("input21.txt").readlines()

moves = {
    "N": (-1,0),
    "S": (1,0),
    "E": (0,1),
    "W": (0,-1)
}

def findLocation(grid, char="S"):
    for row in range(len(grid)):
        col = grid[row].find(char)
        if col != -1:
            return (row,col)

def rockPoints(grid):
    rocks = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                rocks.add((row,col))
    return rocks

def partA(lines, steps=64):
    grid = [line.strip() for line in lines]
    ignoredPoints = rockPoints(grid)
    possibilities = set()
    startLocation = findLocation(grid)
    possibilities.add(startLocation)

    for _ in range(steps):
        newSpots = set()
        for point in possibilities:
            for change in moves.values():
                nextPoint = (point[0]+change[0], point[1]+change[1])
                if nextPoint in ignoredPoints:
                    continue
                if len(grid)<=nextPoint[0]<0:
                    continue    
                if len(grid[0])<=nextPoint[1]<0:
                    continue
                newSpots.add(nextPoint)
        possibilities = newSpots

    return len(possibilities)

# Hyper-Neutrino for Part B
# https://youtu.be/9UOMZSL0JTg?si=E9tjnWRzO46nZcA7

def fill(startRow, startCol, startSteps, grid):
    ans = set()
    seen = {(startRow,startCol)}
    q = deque([(startRow, startCol, startSteps)])

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            ans.add((r,c))
        if s == 0:
            continue

        for change in moves.values():
            nr = r + change[0]
            nc = c + change[1]
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            q.append((nr, nc, s-1))

    return len(ans)

def partB(lines):
    grid = [line.strip() for line in lines]
    startLocation = findLocation(grid)

    steps = 26501365

    assert startLocation[0] == startLocation[1] == len(grid) // 2
    assert steps % len(grid) == len(grid) // 2
    
    gridWidth = steps // len(grid) - 1

    odd = (gridWidth // 2*2 +1) **2
    even = ((gridWidth +1)//2*2) **2

    oddPoints = fill(startLocation[0], startLocation[1], len(grid)*2+1, grid)
    evenPoints = fill(startLocation[0], startLocation[1], len(grid)*2, grid)

    cornerN = fill(len(grid)-1, startLocation[1], len(grid)-1, grid)
    cornerE = fill(startLocation[0], 0, len(grid)-1, grid)
    cornerS = fill(0, startLocation[1], len(grid)-1, grid)
    cornerW = fill(startLocation[0], len(grid)-1, len(grid)-1, grid)

    smallNE = fill(len(grid) -1,0,len(grid) // 2-1, grid)
    smallNW = fill(len(grid)-1,len(grid)-1,len(grid) // 2-1, grid)
    smallSE = fill(0,0,len(grid) // 2-1, grid)
    smallSW = fill(0,len(grid)-1,len(grid) // 2-1, grid)

    largeNE = fill(len(grid) -1,0,len(grid)*3 // 2-1, grid)
    largeNW = fill(len(grid)-1,len(grid)-1,len(grid)*3 // 2-1, grid)
    largeSE = fill(0,0,len(grid)*3 // 2-1, grid)
    largeSW = fill(0,len(grid)-1,len(grid)*3 // 2-1, grid)

    return (
        odd * oddPoints +
        even * evenPoints +
        cornerN + cornerE + cornerS + cornerW +
        (gridWidth + 1) * (smallNE + smallNW + smallSE + smallSW) +
        gridWidth * (largeNE + largeNW + largeSE + largeSW)
    )

print(partA(inputLines))
print(partB(inputLines))

#example = [
#    "...........\n",
#    ".....###.#.\n",
#    ".###.##..#.\n",
#    "..#.#...#..\n",
#    "....#.#....\n",
#    ".##..S####.\n",
#    ".##..#...#.\n",
#    ".......##..\n",
#    ".##.#.####.\n",
#    ".##..##.##.\n",
#    "...........\n"
#]

#print(partA(example, 6))