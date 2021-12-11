with open('day11/input', 'r') as f:
    octs = [x for x in ([int(char) for char in y.strip()] for y in f.readlines())]

width = len(octs[0])
height = len(octs)

flashes = 0

def increase():
    for x in range(width):
        for y in range(height):
            octs[y][x] += 1

def getNeighbours(x, y):
    neighbours = []
    if x > 0:
        neighbours.append((x-1, y))   # left
    if x > 0 and y > 0:
        neighbours.append((x-1, y-1)) # top-left
    if x > 0 and y < height-1:
        neighbours.append((x-1, y+1)) # bottom-left
    if x < width-1:
        neighbours.append((x+1, y))   # right
    if x < width-1 and y > 0:
        neighbours.append((x+1, y-1)) # top-right
    if x < width-1 and y < height-1:
        neighbours.append((x+1, y+1)) # bottom-right
    if y > 0:
        neighbours.append((x, y-1))   # top
    if y < height-1:
        neighbours.append((x, y+1))   # bottom

    return neighbours

def flash(x, y):
    global flashes
    flashes += 1

    octs[y][x] = -1

    neighbours = getNeighbours(x, y)
    for (i, j) in neighbours:
        if octs[j][i] > -1 : octs[j][i] += 1
        if octs[j][i] > 9:
            flash(i, j)

def findAnyFlashers():
    for x in range(width):
        for y in range(height):
            if octs[y][x] > 9:
                flash(x, y)

def reset():
    for x in range(width):
        for y in range(height):
            if octs[y][x] == -1:
                octs[y][x] = 0


def step():
    increase()
    findAnyFlashers()

stepCount = 0
found = False
while not found:
    found = True
    step()
    for x in range(width):
        for y in range(height):
            if octs[y][x] != -1:
                found = False
    reset()
    stepCount += 1

print (stepCount)
