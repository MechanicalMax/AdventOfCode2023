inputLines = open("input1.txt").readlines()

def partA(lines):
    total = 0
    for line in lines:
        numOne, numTwo = "", ""
        for char in line:
            if char.isnumeric():
                numOne = char
                break
                
        for char in reversed(line):
            if char.isnumeric():
                numTwo = char
                break
        num = int(numOne + numTwo)
        total += num
    return total

def partB(lines):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for line in lines:
        numOne, numTwo = "", ""

        indexes = []
        for i, char in enumerate(line):
            if char.isnumeric():
                indexes.append((i,char))

        for i, num in enumerate(digits):
            firstOccurance = line.find(num)
            if firstOccurance != -1:
                indexes.append((firstOccurance,str(i+1)))
                secondOccurance = line.rfind(num)
                if secondOccurance != firstOccurance:
                    indexes.append((line.rfind(num),str(i+1)))

        indexes.sort()
        numOne = indexes[0][1]
        numTwo = indexes[-1][1]

        num = int(numOne + numTwo)
        total += num
    
    return total

print(partA(inputLines))
print(partB(inputLines))