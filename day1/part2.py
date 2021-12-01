with open('day1/input', 'r') as f:
    lines = [int(x) for x in f.readlines()]

count = 0
for i in range(3, len(lines)):
    window1 = lines[i] + lines[i-1] + lines[i-2]
    window2 = lines[i-1] + lines[i-2] + lines[i-3]
    if(window1 > window2):
        count += 1

print (count)
