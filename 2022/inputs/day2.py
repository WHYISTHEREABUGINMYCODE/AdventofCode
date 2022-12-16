from common import read_input

input = read_input('day2/input.txt')
splittedInput = input.split('\n')

print(splittedInput)
def Cases(line):
    totalScore = 0
    
    if line == 'A Y':
        totalScore += 8
    elif line == 'B Z':
        totalScore += 9
    elif line == 'C X':
        totalScore += 7
    elif line == 'A X':
        totalScore += 4
    elif line == 'B Y':
        totalScore += 5
    elif line == 'C Z':
        totalScore += 6
    elif line == 'A Z':
        totalScore += 3
    elif line == 'B X':
        totalScore += 1
    elif line == 'C Y':
        totalScore += 2
    return totalScore

def Cases2(line):
    totalScore = 0
    
    if line == 'A Y':
        totalScore += 4
    elif line == 'B Z':
        totalScore += 9
    elif line == 'C X':
        totalScore += 2
    elif line == 'A X':
        totalScore += 3
    elif line == 'B Y':
        totalScore += 5
    elif line == 'C Z':
        totalScore += 7
    elif line == 'A Z':
        totalScore += 8
    elif line == 'B X':
        totalScore += 1
    elif line == 'C Y':
        totalScore += 6
    return totalScore
        

def part1():
    total = 0

    for line in splittedInput: 
        total +=  Cases(line)

    
    print(total)
       
       
part1()

def part2():
    total = 0
    
    for line in splittedInput:
        total += Cases2(line)
    print(total)
    
part2()