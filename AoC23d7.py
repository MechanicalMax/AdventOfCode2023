inputLines = open("input7.txt").readlines()

strengths = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
jokerStrengths = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]


def identifyType(hand):
    uniqueCards = set(hand)
    if len(uniqueCards) == 1:
        return 7
    elif len(uniqueCards) == 2:
        occurances = hand.count(uniqueCards.pop())
        if occurances == 1 or occurances == 4:
            return 6
        else:
            return 5
    elif len(uniqueCards) == 3:
        previousSingleOccurance = False
        for card in uniqueCards:
            if hand.count(card) == 2:
                return 3
            elif hand.count(card) == 3:
                return 4
            else:
                if previousSingleOccurance:
                    return 4
                else:
                    previousSingleOccurance = True
    elif len(uniqueCards) == 4:
        return 2
    else:
        return 1

def compareHands(a, b, joker):
    aBetter = False
    a = a[0]
    b = b[0]
    if joker:
        stronglist = jokerStrengths
        typeA = jokerType(a)
        typeB = jokerType(b)
    else:
        stronglist = strengths
        typeA = identifyType(a)
        typeB = identifyType(b)

    if typeA > typeB:
        aBetter = True
    elif typeA == typeB:
        for index, cardA in enumerate(a):
            cardB = b[index]
            if cardA == cardB:
                continue
            if stronglist.index(cardA) < stronglist.index(cardB):
                aBetter = True
                break
            else:
                break

    return aBetter

def insertionSort(arr, joker):
    n = len(arr)

    for i in range(1, n):
        current = arr[i]
        j = i-1
        while j >= 0 and compareHands(arr[j], current, joker):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current

def partA(lines):
    total = 0
    inputPairs = [tuple(x.strip().split(" ")) for x in lines]
    
    insertionSort(inputPairs, joker=False)

    for rank, pair in enumerate(inputPairs):
        total += (1+rank) * int(pair[1])

    return total

def jokerType(hand):
    if "J" not in hand:
        return identifyType(hand)

    jokerNum = hand.count("J")
    if jokerNum >= 4:
        return 7

    uniqueCards = set(hand)
    uniqueCards.remove("J")
    if len(uniqueCards) == 1:
        return 7
    if len(uniqueCards) == 3:
        return 4
    if jokerNum == 1:
        if len(uniqueCards) == 4:
            return 2
        else:
            if hand.count(uniqueCards.pop()) == 2:
                return 5
            else:
                return 6
    else:
        return 6

def partB(lines):
    total = 0
    inputPairs = [tuple(x.strip().split(" ")) for x in lines]

    insertionSort(inputPairs, joker=True)

    for rank, pair in enumerate(inputPairs):
        total += (1+rank) * int(pair[1])

    return total

print(partA(inputLines))
print(partB(inputLines))