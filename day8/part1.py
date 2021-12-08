with open('day8/input', 'r') as f:
    lines = [(x, y.strip()) for x, y in map(lambda line: line.split(" | "), f.readlines())]


count = 0
for (_, output) in lines:
    characters = output.split(' ')
    for i in range(4):
        segs = len(characters[i])
        if segs == 2 or segs == 4 or segs == 3 or segs == 7:
            count += 1

print (count)