with open('day7/input', 'r') as f:
    crabs = [int(x) for x in f.read().split(",")]

maxPos = max(crabs)
minPos = min(crabs)

def calcFuelUsage(pos):
    fuel = 0
    for crab in crabs:
        distance = abs(crab - pos) + 1
        fuel += (distance * (distance-1)) / 2
    return fuel

minFuel = 9999999999
for i in range(minPos, maxPos):
    minFuel = min(minFuel, calcFuelUsage(i))

print (minFuel)