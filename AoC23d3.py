inputLines = open("input3.txt").readlines()

def getNumberCoords(lines):
    coords = []

    for row,line in enumerate(lines):
        numStart = 0
        inNumber = False
        for col,char in enumerate(line):
            if not inNumber:
                if char.isnumeric():
                    numStart = col
                    inNumber = True
            else:
                if not char.isnumeric():
                    #(numRow, startCol, endCol)
                    coords.append((row,numStart,col))
                    inNumber = False
                elif col == 139:
                    coords.append((row,numStart,col+1))

    # Testing if numberCoords gives what we want
    #for number in coords:
    #    print(lines[number[0]][number[1]:number[2]])

    return coords

def partA(lines):
    total = 0
    #Grid is 140x140
    lines = [i.strip() for i in lines]

    #(numRow, startCol, endCol)
    numberCoords = getNumberCoords(lines)
    
    for number in numberCoords:
        numRow, startCol, endCol = number
        minRow = numRow-1 if numRow>0 else 0
        maxRow = numRow+2 if numRow<139 else 140
        minCol = startCol-1 if startCol>0 else 0
        maxCol = endCol+1 if endCol<140 else 140
        
        #if numRow == 139:
        #    print("Num: "+lines[numRow][startCol:endCol])
        #    print(number)
        #    print(minRow, maxRow, minCol, maxCol)
        #    print()
        currentPartNumber = int(lines[numRow][startCol:endCol])
        valid = False

        for searchRow in range(minRow,maxRow):
            for searchCol in range(minCol,maxCol):
                char = lines[searchRow][searchCol]
                if not char.isnumeric() and not char == ".":
                    total += currentPartNumber
                    valid = True
                    break
            if valid:
                break

    return total

def partB(lines):
    total = 0
    #Grid is 140x140
    lines = [i.strip() for i in lines]

    #(numRow, startCol, endCol)
    numberCoords = getNumberCoords(lines)
    gears = {}
    
    for number in numberCoords:
        numRow, startCol, endCol = number
        minRow = numRow-1 if numRow>0 else 0
        maxRow = numRow+2 if numRow<139 else 140
        minCol = startCol-1 if startCol>0 else 0
        maxCol = endCol+1 if endCol<140 else 140
        
        currentPartNumber = int(lines[numRow][startCol:endCol])

        for searchRow in range(minRow,maxRow):
            for searchCol in range(minCol,maxCol):
                char = lines[searchRow][searchCol]
                if char == "*":
                    if (searchRow,searchCol) in gears.keys():
                        gears[(searchRow,searchCol)].append(currentPartNumber)
                    else:
                        gears[(searchRow,searchCol)] = [currentPartNumber]

    for gear in gears.values():
        if len(gear) == 2:
            total += gear[0] * gear[1]

    return total

print(partA(inputLines))
print(partB(inputLines))