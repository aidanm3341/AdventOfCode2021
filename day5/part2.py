with open('day5/input', 'r') as f:
    pairs = [a.split("->") for a in f.readlines()]
    parsedPairs = [(b[0].split(","), b[1].split(",")) for b in pairs]   
    lines = [((int(a[0]), int(a[1])), (int(b[0]), int(b[1]))) for (a, b) in parsedPairs]

grid = [[]]

def padGridCols(x):
    while (len(grid[0]) <= x):
        for row in grid:
            row.append(0)

def padGridRows(y):
    while (len(grid) <= y):
        grid.append([0 for _ in range(len(grid[0]))])

def drawSegment(x, y):
    padGridCols(x)
    padGridRows(y)
    grid[y][x] += 1
    

def drawLineOnGrid(line):
    x1, x2 = line[0][0], line[1][0]
    y1, y2 = line[0][1], line[1][1]
    if (x1 == x2): # vertical
        step = 1 if y2 > y1 else -1
        for i in range(y1, y2+step, step):
            drawSegment(x1, i)
    elif (y1 == y2): # horizontal
        step = 1 if x2 > x1 else -1
        for i in range(x1, x2+step, step):
            drawSegment(i, y1) 
    elif ((y2 - y1)/(x2 - x1) == 1 or (y2 - y1)/(x2 - x1) == -1): # diagonal
        xStep = 1 if x2 > x1 else -1
        yStep = 1 if y2 > y1 else -1
        i, j = x1, y1
        for i, j in zip(range(x1, x2+xStep, xStep), range(y1, y2+yStep, yStep)):
            drawSegment(i, j)

def printGrid():
    for row in grid:
        print(''.join([str(x) for x in row]))

for line in lines:
    drawLineOnGrid(line)

count = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[j][i] > 1:
            count += 1

print (count)
