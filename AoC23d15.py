inputString = open("input15.txt").readlines()[0]

def hashStep(step):
    total = 0
    for char in step:
        total += ord(char)
        total *= 17
        total %= 256
    return total

def partA(string):
    total = 0
    steps = tuple(string.strip().split(","))

    for step in steps:
        total += hashStep(step)

    return total

def focusingPower(boxes):
    total = 0
    for boxI in range(len(boxes)):
        for slotI in range(len(boxes[boxI])):
            total += (boxI+1)*(slotI+1)*int(boxes[boxI][slotI][1])
    return total

def partB(string):
    boxes = [[] for x in range(256)]
    steps = tuple(string.strip().split(","))
    
    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            boxNum = hashStep(label)
            for labelIndex in range(len(boxes[boxNum])):
                if boxes[boxNum][labelIndex][0] == label:
                    boxes[boxNum].pop(labelIndex)
                    break
        else:
            label, length = step.split("=")
            boxNum = hashStep(label)
            for labelIndex in range(len(boxes[boxNum])):
                if boxes[boxNum][labelIndex][0] == label:
                    boxes[boxNum][labelIndex][1] = length
                    break
            else:
                boxes[boxNum].append([label,length])

    return focusingPower(boxes)

print(partA(inputString))
print(partB(inputString))

#example = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"