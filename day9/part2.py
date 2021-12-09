from collections import Counter
from math import prod

with open('day9/input', 'r') as f:
    lines = [x for x in ([int(char) for char in y.strip()] for y in f.readlines())]

width = len(lines[0])
height = len(lines)

def isLessThanNeighbours(x, y):
    top, down, left, right = 0, 0, 0, 0
    top   = lines[y-1][x] if y > 0 and str(lines[y-1][x]).isnumeric() else height+1
    down  = lines[y+1][x] if y < height-1 and str(lines[y+1][x]).isnumeric() else height+1
    left  = lines[y][x-1] if x > 0 and str(lines[y][x-1]).isnumeric() else width+1
    right = lines[y][x+1] if x < width-1 and str(lines[y][x+1]).isnumeric() else width+1

    return left > lines[y][x] < right and down > lines[y][x] < top

def getGreaterThanNeighbours(x, y):
    top, down, left, right = 0, 0, 0, 0
    top   = lines[y-1][x] if y > 0 else 9
    down  = lines[y+1][x] if y < height-1 else 9
    left  = lines[y][x-1] if x > 0 else 9
    right = lines[y][x+1] if x < width-1 else 9

    neighbours = []
    val = lines[y][x]
    if str(left).isnumeric() and val < left  and left  != 9: neighbours.append((x-1, y))
    if str(right).isnumeric() and val < right and right != 9: neighbours.append((x+1, y))
    if str(top).isnumeric() and val < top   and top   != 9: neighbours.append((x, y-1))
    if str(down).isnumeric() and val < down  and down  != 9: neighbours.append((x, y+1))

    return neighbours
    
def checkAndMarkNeighbours(x, y, marker):
    if str(lines[y][x]).isnumeric():
        for (i, j) in getGreaterThanNeighbours(x, y):
            if str(lines[j][i]).isnumeric():
                checkAndMarkNeighbours(i, j, marker)
    lines[y][x] = marker


marker = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
i, j = 0, 0
for x in range(width):
    for y in range(height):
        if(str(lines[y][x]).isnumeric()):
            if isLessThanNeighbours(x, y):
                checkAndMarkNeighbours(x, y, marker[j] + marker[i])
                i += 1
                if i >= len(marker):
                    j += 1
                    i = 0

lines = [str(c) for row in lines for c in row]
counter = Counter(lines)
counter.pop('9')
vals = sorted([y for (x, y) in counter.items()])

print (prod(vals[-3:]))
