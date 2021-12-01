with open('day1/input', 'r') as f:
    lines = [int(x) for x in f.readlines()]

count = 0
for i in range(1, len(lines)):
    if(lines[i] > lines[i-1]):
        count += 1

print (count)
