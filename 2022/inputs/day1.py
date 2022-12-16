from common import read_input

input = read_input('day1/input.txt') 
input2 = read_input('day1/input2.txt')   
splittedList = input.split("\n")
splittedList2 = input2.split("\n")



def part1():   
    temp = 0
    output = []
    
    for line in splittedList:
        try:
            temp += int(line)
        except:
            output.append(temp)
            temp = 0
    output.sort()
    biggestCalorieEaterElf = output[len(output)-1]
    return biggestCalorieEaterElf

def part2():   
    temp = 0
    output = []
    
    for line in splittedList:
        try:
            temp += int(line)
        except:
            output.append(temp)
            temp = 0
    output.sort()
    topThreeBiggestCalorieEaterElfTotal = output[len(output)-1] + output[len(output)-2] + output[len(output)-3]
    return topThreeBiggestCalorieEaterElfTotal
        
                     
print(part1())
print(part2())