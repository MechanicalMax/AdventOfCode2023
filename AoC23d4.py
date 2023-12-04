inputLines = open("input4.txt").readlines()

def getNumberSets(line):
    line = line[line.find(":")+2:]
    winningN, cardN = line.split(" | ")
    winningN = winningN.split(" ")
    winningN = [i for i in winningN if i]
    cardN = cardN.split(" ")
    cardN = [i for i in cardN if i]

    return winningN, cardN

def partA(lines):
    totalPoints = 0
    lines = [i.strip() for i in lines]

    for line in lines:
        winningN, cardN = getNumberSets(line)
        points = 0
        for win in winningN:
            if win in cardN:
                if not points:
                    points = 1
                else:
                    points *= 2
        totalPoints += points

    return totalPoints

def partB(lines):
    totalCards = 0
    lines = [i.strip() for i in lines]
    repeats = [1 for i in range(len(lines))]

    for cardNum, line in enumerate(lines):
        winningN, cardN = getNumberSets(line)
        wins = 0
        for win in winningN:
            if win in cardN:
                wins += 1
        for i in range(wins):
            repeats[i+1+cardNum] += repeats[cardNum]

    totalCards = sum(repeats)

    return totalCards

print(partA(inputLines))
print(partB(inputLines))