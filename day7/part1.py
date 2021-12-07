with open('day7/input', 'r') as f:
    crabs = [int(x) for x in f.read().split(",")]

maxPos = max(crabs)
minPos = min(crabs)

def calcFuelUsage(pos):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)
    return fuel

minFuel = 9999999999
for i in range(minPos, maxPos):
    minFuel = min(minFuel, calcFuelUsage(i))

print (minFuel)