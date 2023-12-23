inputLines = open("input23.txt").read().splitlines()

# Part A didn't seem too hard, but there might be some 
# edge cases that are not obvious at first glance.
# Watching the video first to ensure I have time for other
# things today.
# https://youtu.be/NTLYL7Mg2jU?si=UhkIESeDj1J8zRjc

def dfs(pt, seen, end, graph):
    if pt == end:
        return 0
    
    m = -float("inf")

    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx, seen, end, graph) + graph[pt][nx])
    seen.remove(pt)

    return m

# Using "edge collapsing"
def partA(grid):
    start = (0, grid[0].index("."))
    end = (len(grid)-1,grid[-1].index("."))

    points = [start, end]

    # Add all the points that have more than two options
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "#":
                continue
            neighbors = 0
            for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                    neighbors +=1
            if neighbors >= 3:
                points.append((r,c))
    
    graph = {pt: {} for pt in points}

    directions = {
        "^": [(-1,0)],
        "v": [(1,0)],
        "<": [(0,-1)],
        ">": [(0,1)],
        ".": [(-1,0),(1,0),(0,-1),(0,1)]
    }

    for sr,sc in points:
        stack = [(0,sr,sc)]
        seen = {(sr,sc)}

        while stack:
            n,r,c = stack.pop()

            if n != 0 and (r,c) in points:
                graph[(sr, sc)][(r,c)] = n
                continue

            for dr,dc in directions[grid[r][c]]:
                nr = r + dr
                nc = c + dc
                if 0<= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n+1, nr, nc))
                    seen.add((nr, nc))

    dfsSeen = set()

    return dfs(start, dfsSeen, end, graph)

# DFS are inherently inefficient, only one change from part A
def partB(grid):
    start = (0, grid[0].index("."))
    end = (len(grid)-1,grid[-1].index("."))

    points = [start, end]

    # Add all the points that have more than two options
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "#":
                continue
            neighbors = 0
            for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                    neighbors +=1
            if neighbors >= 3:
                points.append((r,c))
    
    graph = {pt: {} for pt in points}

    for sr,sc in points:
        stack = [(0,sr,sc)]
        seen = {(sr,sc)}

        while stack:
            n,r,c = stack.pop()

            if n != 0 and (r,c) in points:
                graph[(sr, sc)][(r,c)] = n
                continue
            
            # No more Directions dictionary, all non-forest tiles are the same
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr = r + dr
                nc = c + dc
                if 0<= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n+1, nr, nc))
                    seen.add((nr, nc))

    dfsSeen = set()

    return dfs(start, dfsSeen, end, graph)

print(partA(inputLines))
print(partB(inputLines))