from math import sqrt, ceil
inputLines = open("input6.txt").readlines()

def getInputPairs(lines):
    data = []
    for line in lines:
        current = line[line.find(":")+1:].strip().split(" ")
        data.append([int(x) for x in current if x])

    return tuple(zip(data[0],data[1]))

def findWinningRaces(race):
    time, dist = race
    minimum = (-time+sqrt(time**2-4*dist))/(-2)
    maximum = (-time-sqrt(time**2-4*dist))/(-2)

    return ceil(maximum)-ceil(minimum)

def partA(lines):
    races = getInputPairs(lines)
    winningRaces = 1

    for race in races:
        winningRaces *= findWinningRaces(race)

    return winningRaces

def partB(lines):
    race = []
    for line in lines:
        number = []
        for char in line:
            if char.isnumeric():
                number.append(char)
        race.append(int("".join(number)))

    return findWinningRaces(race)

print(partA(inputLines))
print(partB(inputLines))
# This was a fun one
# I knew immediatly that this would need to be optimized.
# So, i tried to find an equation that could describe how
# the distance and time relate to each other.
# This turned out to be a quadratic equation, so using
# the quadratic formula in findWinningRaces(race)
# allows us to find the zeros in the equation.
# subtracting the ceiling of both endpoints
# gives us the number of races won in the range of winning numbers
# The rest was simply parsing the input :D