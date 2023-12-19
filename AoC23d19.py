inputLines = open("input19.txt").readlines()

partRatingIndexes = ["x","m","a","s"]

def getWorkflows(lines):
    workflows = {}
    endIndex = lines.index("\n")
    for line in lines[:endIndex]:
        name, rules = line.strip("}\n").split("{")
        rules = rules.split(",")
        workflows[name] = rules

    return workflows

def getParts(lines):
    parts = []
    startIndex = lines.index("\n")
    for line in lines[startIndex+1:]:
        line = line.strip("}{\n")
        nums = []
        inNum = False
        for char in line:
            if char.isnumeric():
                if inNum:
                    nums[-1] += char
                else:
                    inNum = True
                    nums.append(char)
            else:
                inNum = False
        parts.append(tuple(map(int, nums)))
    return parts

def partA(lines):
    workflows = getWorkflows(lines)
    parts = getParts(lines)
    total = 0

    for part in parts:
        curW = "in"
        while curW not in ["A", "R"]:
            rules = workflows[curW]
            for rule in rules[:-1]:
                condition, result = rule.split(":")
                param = condition[0]
                opp = condition[1]
                thresh = int(condition[2:])
                if opp == ">":
                    if part[partRatingIndexes.index(param)] > thresh:
                        curW = result
                        break
                else:
                    if part[partRatingIndexes.index(param)] < thresh:
                        curW = result
                        break
            else:
                curW = rules[-1]
        
        if curW == "A":
            total += sum(part)
    
    return total

# Instead of using my entire day to work on part B like I did yesterday,
# I decided to look at the Hyper-Neutrino video so I can better understand
# how to approach this type of problem since it seems like this kind of 
# optimization problem is frequent this year
# https://youtu.be/3RwIpUegdU4?si=EQ-Kg5CCpojFqtyb

def count(ranges,  workflows, name="in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules = workflows[name]
    total = 0

    for rule in rules[:-1]:
        condition, result = rule.split(":")
        param = condition[0]
        opp = condition[1]
        thresh = int(condition[2:])

        lo, hi = ranges[param]
        if opp == "<":
            TRange = (lo, min(thresh-1, hi))
            FRange = (max(thresh, lo), hi)
        else:
            TRange = (max(thresh + 1, lo), hi)
            FRange = (lo, min(thresh,hi))
        if TRange[0] <= TRange[1]:
            copy = dict(ranges)
            copy[param] = TRange
            total += count(copy, workflows, name=result)
        if FRange[0] <= FRange[1]:
            ranges = dict(ranges)
            ranges[param] = FRange
        else:
            break
    else:
        total += count(ranges, workflows, name=rules[-1])

    return total

def partB(lines):
    workflows = getWorkflows(lines)
    return count({rating: (1, 4000) for rating in partRatingIndexes}, workflows)

print(partA(inputLines))
print(partB(inputLines))

#example = [
#    "px{a<2006:qkq,m>2090:A,rfg}\n",
#    "pv{a>1716:R,A}\n",
#    "lnx{m>1548:A,A}\n",
#    "rfg{s<537:gd,x>2440:R,A}\n",
#    "qs{s>3448:A,lnx}\n",
#    "qkq{x<1416:A,crn}\n",
#    "crn{x>2662:A,R}\n",
#    "in{s<1351:px,qqz}\n",
#    "qqz{s>2770:qs,m<1801:hdj,R}\n",
#    "gd{a>3333:R,R}\n",
#    "hdj{m>838:A,pv}\n",
#    "\n",
#    "{x=787,m=2655,a=1222,s=2876}\n",
#    "{x=1679,m=44,a=2067,s=496}\n",
#    "{x=2036,m=264,a=79,s=2244}\n",
#    "{x=2461,m=1339,a=466,s=291}\n",
#    "{x=2127,m=1623,a=2188,s=1013}\n"
#]
#
#print(partA(example))
#print(partB(example))