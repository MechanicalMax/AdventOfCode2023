from heapq import heappush, heappop
inputLines = open("input17.txt").readlines()

# Thanks HyperNeutrino for the tutorial
# I did not know how to implement Dijkstra's
# for this problem:
# https://youtu.be/2pDSooPLLkI?si=NAw0wDJaoY1UgAiw

def partA(lines):
    city = [list(map(int, line.strip())) for line in lines]
    start = (0,0)
    end = (len(city)-1,len(city[0])-1)
    visited = set()
    # heatLoss, row, col, rowDirection, colDirection, nStepsInDirection
    pq = [(0, start[0], start[1], 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        if r == end[0] and c == end[1]:
            return hl

        if (r,c,dr,dc,n) in visited:
            continue

        visited.add((r,c,dr,dc,n))

        if n < 3 and (dr, dc) != (0,0):
            nRow = r + dr
            nCol = c + dc
            if nRow in range(len(city)) and nCol in range(len(city[0])):
                heappush(pq, (hl + city[nRow][nCol], nRow, nCol, dr, dc, n+1))

        for ndr, ndc in ((0,1), (1,0), (0,-1), (-1,0)):
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr,-dc):
                nRow = r + ndr
                nCol = c + ndc
                if nRow in range(len(city)) and nCol in range(len(city[0])):
                    heappush(pq, (hl+city[nRow][nCol],nRow, nCol, ndr,ndc,1))

# Only difference between part A and B are the conditions
def partB(lines):
    city = [list(map(int, line.strip())) for line in lines]
    start = (0,0)
    end = (len(city)-1,len(city[0])-1)
    visited = set()
    # heatLoss, row, col, rowDirection, colDirection, nStepsInDirection
    pq = [(0, start[0], start[1], 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        if r == end[0] and c == end[1] and n >= 4:
            return hl

        if (r,c,dr,dc,n) in visited:
            continue

        visited.add((r,c,dr,dc,n))

        if n < 10 and (dr, dc) != (0,0):
            nRow = r + dr
            nCol = c + dc
            if nRow in range(len(city)) and nCol in range(len(city[0])):
                heappush(pq, (hl + city[nRow][nCol], nRow, nCol, dr, dc, n+1))
        
        if n >= 4 or (dr, dc) == (0,0):
            for ndr, ndc in ((0,1), (1,0), (0,-1), (-1,0)):
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr,-dc):
                    nRow = r + ndr
                    nCol = c + ndc
                    if nRow in range(len(city)) and nCol in range(len(city[0])):
                        heappush(pq, (hl+city[nRow][nCol],nRow, nCol, ndr,ndc,1))

print(partA(inputLines))
print(partB(inputLines))

#example=(
#    "2413432311323\n",
#    "3215453535623\n",
#    "3255245654254\n",
#    "3446585845452\n",
#    "4546657867536\n",
#    "1438598798454\n",
#    "4457876987766\n",
#    "3637877979653\n",
#    "4654967986887\n",
#    "4564679986453\n",
#    "1224686865563\n",
#    "2546548887735\n",
#    "4322674655533\n"
#)