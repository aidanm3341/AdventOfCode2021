with open('day8/input', 'r') as f:
    lines = [(x, y.strip()) for x, y in map(lambda line: line.split(" | "), f.readlines())]

def crossoverCount(xs, ys):
    return len(set(xs).intersection(ys))

def findZero(map):
    one = map[1][0]
    
    charsNotInZero = map[4][0].replace(one[0], '').replace(one[1], '')
    toRemove = []
    for str in map[0]:
        if charsNotInZero[0] in str and charsNotInZero[1] in str:
            toRemove.append(str)
    for t in toRemove:
        map[0].remove(t)
    map[6].remove(map[0][0])
    map[9].remove(map[0][0])

def findThree(map):
    if crossoverCount(map[3][0], map[3][1]) == 3:
        three = map[3][2]
    elif crossoverCount(map[3][2], map[3][1]) == 3:
        three = map[3][0]
    else:
        three = map[3][1]

    map[3] = list(filter(three.__eq__, map[3]))
    map[2].remove(map[3][0])
    map[5].remove(map[3][0])

def findNine(map):
    if crossoverCount(map[9][0], map[3][0]) == 5:
        map[9].remove(map[9][1])
    else:
        map[9].remove(map[9][0])
    map[6].remove(map[9][0])

def findFive(map):
    if crossoverCount(map[5][0], map[6][0]) == 5:
        map[5].remove(map[5][1])
    else:
        map[5].remove(map[5][0])
    map[2].remove(map[5][0])

def calculateMapping(data):
    map = [[], [], [], [], [], [], [], [] ,[], []]
    characters = data.split(' ')
    for char in characters:
        if len(char) == 2: map[1].append(char) 
        if len(char) == 4: map[4].append(char)  
        if len(char) == 3: map[7].append(char) 
        if len(char) == 7: map[8].append(char)
        if len(char) == 5: 
            map[2].append(char) 
            map[3].append(char) 
            map[5].append(char) 
        if len(char) == 6: 
            map[0].append(char) 
            map[6].append(char) 
            map[9].append(char) 
    findZero(map) 
    findThree(map)
    findNine(map)
    findFive(map)
    return [x for [x] in map]

total = 0
for (data, output) in lines:
    num = ""
    map = calculateMapping(data)
    for val in output.split(' '):
        for i in range(10):
            if len(val) == len(map[i]) and len(set(val).intersection(map[i])) == len(val):
                num += str(i)
    total += int(num)

print (total)

