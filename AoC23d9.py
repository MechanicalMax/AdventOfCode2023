inputLines = open("input9.txt").readlines()

def partA(lines):
    total = 0
    for line in lines:
        numArr = [int(x) for x in line.strip().split(" ")]
        differenceEndIndex = len(numArr)

        while differenceEndIndex > 1:
            for i in range(0,differenceEndIndex-1):
                numArr[i] = numArr[i+1] - numArr[i]
            differenceEndIndex -= 1

        total += sum(numArr[differenceEndIndex:])

    return total

def findPrevNum(numArr):
    num = 0
    for index in range(len(numArr)-1,-1,-1):
        num = numArr[index] - num

    return num

def partB(lines):
    total = 0
    for line in lines:
        numArr = [int(x) for x in line.strip().split(" ")]
        numberLength = len(numArr)
        differenceStartIndex = 1

        while differenceStartIndex < numberLength:
            for i in range(numberLength-1,differenceStartIndex-1,-1):
                numArr[i] = numArr[i] - numArr[i-1]
            differenceStartIndex += 1

        total += findPrevNum(numArr)

    return total

#partA(["10 13 16 21 30 45\n"])
#partB(["10 13 16 21 30 45\n"])

print(partA(inputLines))
print(partB(inputLines))