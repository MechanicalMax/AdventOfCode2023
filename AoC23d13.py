inputLines = open("input13.txt").readlines()

def getPatterns(lines):
    patterns = [[]]
    for line in lines:
        if line == "\n":
            patterns.append([])
        else:
            patterns[-1].append(line.strip())
    return patterns

palendromeCache = {}

# Recursively check for a palindrome
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
# Implement memoization for speed after doing research inspired by day 12
def recursiveIsPalindrome(st, s, e):
    if st[s:e+1] in palendromeCache:
        return palendromeCache[st[s:e+1]]

    # One character should be a palindrome
    if s == e:
        palendromeCache[st[s:e+1]] = True
        return True

    if st[s] != st[e]:
        palendromeCache[st[s:e+1]] = False
        return False

    if s < e + 1:
        return recursiveIsPalindrome(st, s+1, e-1)
    
    palendromeCache[st[s:e+1]] = True
    return True

def patternRefLineNumber(pattern, oldResult=0):
    verticalLines = len(pattern[0])-1

    for i in range(1,verticalLines*2,2):
        s = i-verticalLines if i-verticalLines >= 0 else 0
        e = i if i < len(pattern[0]) else verticalLines #1,3,5,7,9,11,13,15

        for row in pattern:
            if recursiveIsPalindrome(row, s, e):
                continue
            else:
                break
        else:
            new = (i+1)//2
            if oldResult != new:
                return new
        
    horizontalLines = len(pattern)-1
    for i in range(1,horizontalLines*2,2):
        s = i-horizontalLines if i-horizontalLines >= 0 else 0
        e = i if i < len(pattern) else horizontalLines
        
        for colNum in range(len(pattern[0])):
            colString = "".join([row[colNum] for row in pattern])
            if recursiveIsPalindrome(colString, s, e):
                continue
            else:
                break
        else:
            new = ((i+1)//2)*100
            if oldResult != new:
                return new

    return 0

def partA(lines):
    total = 0
    patterns = getPatterns(lines)

    for pattern in patterns:
        total += patternRefLineNumber(pattern)

    return total

def tryAllFlips(pattern):
    oldScore = patternRefLineNumber(pattern)
    newScore = oldScore

    for flipRow in range(len(pattern)):
        for flipCol in range(len(pattern[0])):
            originalChar = pattern[flipRow][flipCol]
            flippedChar = "#" if originalChar == "." else "."
            pattern[flipRow] = pattern[flipRow][:flipCol] + flippedChar + pattern[flipRow][flipCol+1:]
            newScore = patternRefLineNumber(pattern,oldScore)
            pattern[flipRow] = pattern[flipRow][:flipCol] + originalChar + pattern[flipRow][flipCol+1:]
            
            if newScore != 0 and newScore != oldScore:
                break
        if newScore != 0 and newScore != oldScore:
            break
    else:
        return oldScore
    
    return newScore

def partB(lines):
    total = 0
    patterns = getPatterns(lines)

    for pattern in patterns:
        total += tryAllFlips(pattern)
    
    return total

print(partA(inputLines))
print(partB(inputLines))