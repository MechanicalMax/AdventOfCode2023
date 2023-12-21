from math import lcm
from collections import deque
inputLines = open("input20.txt").readlines()

# Considering you could get on the two-star leaderboard in nearly 50 minutes,
# and I barely understood the question at 10:00 PM when I started,
# I decided that today I would go straight to the tutorial and hopefully learn
# some more Python technique
# Hyper-Neutrino
# https://youtu.be/lxm6i21O83k?si=IehWRtFp3xFObLC5

class Module:
    def __init__(self, name, type, outputs) -> None:
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

def parseInput(lines):
    modules = {}
    broadcastTargets = []

    for line in lines:
        l, r = line.strip().split(" -> ")
        outputs = r.split(", ")
        if l == "broadcaster":
            broadcastTargets = outputs
        else:
            type = l[0]
            name = l[1:]
            modules[name] = Module(name, type, outputs)  

    for name, module in modules.items():
        for out in module.outputs:
            if out in modules and modules[out].type == "&":
                modules[out].memory[name] = "lo"

    return modules, broadcastTargets

def partA(lines):
    modules, broadcastTargets = parseInput(lines)

    lo = hi = 0

    for _ in range(1000):
        lo += 1

        # Origin, target, pulse
        q = deque([("broadcaster", x, "lo") for x in broadcastTargets])

        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                lo += 1
            else:
                hi += 1

            if target not in modules:
                continue

            targetModule = modules[target]

            if targetModule.type == "%":
                if pulse == "lo":
                    targetModule.memory = "on" if targetModule.memory == "off" else "off"
                    resultantOutput = "hi" if targetModule.memory == "on" else "lo"
                    for x in targetModule.outputs:
                        q.append((targetModule.name, x, resultantOutput))
            else:
                targetModule.memory[origin] = pulse
                resultantOutput = "lo" if all(x=="hi" for x in targetModule.memory.values()) else "hi"
                for x in targetModule.outputs:
                    q.append((targetModule.name, x, resultantOutput))

    return lo*hi

def partB(lines):
    modules, broadcastTargets = parseInput(lines)

    (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]
    cycleLengths = {}
    seen = {name:0 for name,module in modules.items() if feed in module.outputs}

    presses = 0

    while True:
        presses += 1
        # Origin, target, pulse
        q = deque([("broadcaster", x, "lo") for x in broadcastTargets])

        while q:
            origin, target, pulse = q.popleft()

            if target not in modules:
                continue

            targetModule = modules[target]

            if targetModule.name == feed and pulse == "hi":
                seen[origin] += 1

                if origin not in cycleLengths:
                    cycleLengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycleLengths[origin]

                if all(seen.values()):
                    return lcm(*cycleLengths.values())

            if targetModule.type == "%":
                if pulse == "lo":
                    targetModule.memory = "on" if targetModule.memory == "off" else "off"
                    resultantOutput = "hi" if targetModule.memory == "on" else "lo"
                    for x in targetModule.outputs:
                        q.append((targetModule.name, x, resultantOutput))
            else:
                targetModule.memory[origin] = pulse
                resultantOutput = "lo" if all(x=="hi" for x in targetModule.memory.values()) else "hi"
                for x in targetModule.outputs:
                    q.append((targetModule.name, x, resultantOutput))

print(partA(inputLines))
print(partB(inputLines))