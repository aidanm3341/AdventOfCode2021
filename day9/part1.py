with open('day9/input', 'r') as f:
    lines = [x for x in ([int(char) for char in y.strip()] for y in f.readlines())]

width = len(lines[0])
height = len(lines)

def isLessThanNeighbours(x, y):
    top, down, left, right = 0, 0, 0, 0
    top   = lines[y-1][x] if y > 0 else height+1
    down  = lines[y+1][x] if y < height-1 else height+1
    left  = lines[y][x-1] if x > 0 else width+1
    right = lines[y][x+1] if x < width-1 else width+1

    return left > lines[y][x] < right and down > lines[y][x] < top
    

sum = 0
for x in range(width):
    for y in range(height):
        if isLessThanNeighbours(x, y):
            sum += lines[y][x] + 1

print (sum)