with open('day2/input', 'r') as f:
    lines = [x for x in f.readlines()]

depth = 0
distance = 0
aim = 0

for line in lines:
    direction, amount = line.split(" ")
    amount = int(amount)

    if direction == "forward":
        distance += amount
        depth += amount * aim
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

print (depth * distance)