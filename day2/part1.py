with open('day2/input', 'r') as f:
    lines = [x for x in f.readlines()]

depth = 0
distance = 0

for line in lines:
    direction, amount = line.split(" ")
    amount = int(amount)

    if direction == "forward":
        distance += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

print (depth * distance)