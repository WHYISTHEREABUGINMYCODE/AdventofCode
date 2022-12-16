from common import read_input
input = read_input('day3/input.txt')
input2 = read_input('day3/input2.txt')
splittedInput = input.split("\n")
splittedInput2 = input2.split("\n")

def priorityCases(alphabet):
    totalScore = 0
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
    A = 27
    B = 28
    C = 29
    D = 30
    E = 31
    F = 32
    G = 33
    H = 34
    I = 35
    J = 36
    K = 37
    L = 38
    M = 39
    N = 40
    O = 41
    P = 42
    Q = 43
    R = 44
    S = 45
    T = 46
    U = 47
    V = 48
    W = 49
    X = 50
    Y = 51
    Z = 52
    
    if alphabet == "a":
        totalScore += a
        
    elif alphabet == "b":
        totalScore += b
    
    elif alphabet == "c":
        totalScore += c
        
    elif alphabet == "d":
        totalScore += d
    
    elif alphabet == "e":
        totalScore += e
    
    elif alphabet == "f":
        totalScore += f
    
    elif alphabet == "g":
        totalScore += g
    
    elif alphabet == "h":
        totalScore += h
    
    elif alphabet == "i":
        totalScore += i
    
    elif alphabet == "j":
        totalScore += j
        
    elif alphabet == "k":
        totalScore += k
        
    elif alphabet == "l":
        totalScore += l
        
    elif alphabet == "m":
        totalScore += m
        
    elif alphabet == "n":
        totalScore += n
        
    elif alphabet == "o":
        totalScore += o

    elif alphabet == "p":
        totalScore += p
        
    elif alphabet == "q":
        totalScore += q
        
    elif alphabet == "r":
        totalScore += r

    elif alphabet == "s":
        totalScore += s
        
    elif alphabet == "t":
        totalScore += t
        
    elif alphabet == "u":
        totalScore += u
    
    elif alphabet == "v":
        totalScore += v
    
    elif alphabet == "w":
        totalScore += w
    
    elif alphabet == "x":
        totalScore += x
        
    elif alphabet == "y":
        totalScore += y
        
    elif alphabet == "z":
        totalScore += z
    
    if alphabet == "A":
        totalScore += A
        
    elif alphabet == "B":
        totalScore += B
    
    elif alphabet == "C":
        totalScore += C
        
    elif alphabet == "D":
        totalScore += D
    
    elif alphabet == "E":
        totalScore += E
    
    elif alphabet == "F":
        totalScore += F
    
    elif alphabet == "G":
        totalScore += G
    
    elif alphabet == "H":
        totalScore += H
    
    elif alphabet == "I":
        totalScore += I
    
    elif alphabet == "J":
        totalScore += J
        
    elif alphabet == "K":
        totalScore += K
        
    elif alphabet == "L":
        totalScore += L
        
    elif alphabet == "M":
        totalScore += M
        
    elif alphabet == "N":
        totalScore += N
        
    elif alphabet == "O":
        totalScore += O

    elif alphabet == "P":
        totalScore += P
        
    elif alphabet == "Q":
        totalScore += Q
        
    elif alphabet == "R":
        totalScore += R

    elif alphabet == "S":
        totalScore += S
        
    elif alphabet == "T":
        totalScore += T
        
    elif alphabet == "U":
        totalScore += U
    
    elif alphabet == "V":
        totalScore += V
    
    elif alphabet == "W":
        totalScore += W
    
    elif alphabet == "X":
        totalScore += X
        
    elif alphabet == "Y":
        totalScore += Y
        
    elif alphabet == "Z":
        totalScore += Z
    
    return totalScore
    
def part1():
    total = 0
    
    for rucksacks in splittedInput2:
        compartment1 =  rucksacks[0:int(len(rucksacks)/2)]
        compartment2 =  rucksacks[int(len(rucksacks)/2):int(len(rucksacks))]
        for letter1 in compartment1:
            isMatch = False
            for letter2 in compartment2:
                if letter1 == letter2:

                    total += (priorityCases(letter1))
                    isMatch = True
                    break
            if isMatch:
                break


   
    print(total)


    
def match(thing, thing2):
    matches = []
    for letter in thing:
        if letter in thing2:
            matches.append(letter)
    return matches
                
        


def part2():
    total = 0
    
    for i in range(0, len(splittedInput2), 3):
        rucksack = splittedInput[i]
        rucksack2 = splittedInput[i+1]
        rucksack3 = splittedInput[i+2]
        
        
        groupLetter = match(match(rucksack, rucksack2), rucksack3)[0]
        total += priorityCases(groupLetter)
        
    print(total)
            
part2()