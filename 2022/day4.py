from common import read_input
input = read_input("day4/input.txt")
input2 = read_input("day4/input2.txt")
splittedInput = input.split("\n")
splittedInput2 = input2.split("\n")

def compare(list1, list2):
    var1len = len(list1)
    matches = 0
    for numbers in list1:
        if numbers in list2:
            matches += 1
    if matches == var1len:
        return 1
    elif matches > 0: 
        return -1
    else:
        return 0
        

    
def part1():
    rangeList = []
    total = 0
    
    for line in splittedInput:
        sepLine = line.split(",")        
        firstRange = sepLine[0].split("-")
        secondRange = sepLine[1].split("-")
        minumberFirRan = int(firstRange[0])
        minumberSecRan = int(secondRange[0])
        maxNumFirRan = int(firstRange[1])
        maxNumSecRan = int(secondRange[1])
        rangeNumbers = int(minumberFirRan)
        
        
        
        while rangeNumbers <= int(maxNumFirRan):
            rangeList.append(rangeNumbers)
            rangeNumbers = rangeNumbers + 1
        rangeList1 = [i for i in range(minumberFirRan, maxNumFirRan + 1)]
        rangeList2 = [i for i in range(minumberSecRan, maxNumSecRan + 1)]
        if compare(rangeList1,rangeList2) == 1 or compare(rangeList2, rangeList1) == 1:
            total += 1
    
    return total
        
print(part1())
def part2():
    total = 0
    for line in splittedInput:
        sepLine = line.split(",")        
        firstRange = sepLine[0].split("-")
        secondRange = sepLine[1].split("-")
        minumberFirRan = int(firstRange[0])
        minumberSecRan = int(secondRange[0])
        maxNumFirRan = int(firstRange[1])
        maxNumSecRan = int(secondRange[1])
        rangeNumbers = int(minumberFirRan)
        rangeList1 = [i for i in range(minumberFirRan, maxNumFirRan + 1)]
        rangeList2 = [i for i in range(minumberSecRan, maxNumSecRan + 1)]
        
        if compare(rangeList1,rangeList2) == 1 or compare(rangeList1,rangeList2) == -1 or compare(rangeList2,rangeList1) == 1 or compare(rangeList2,rangeList1) == -1:
            total += 1
    
    return total

print(part2())
