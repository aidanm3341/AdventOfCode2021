with open('day6/input', 'r') as f:
    fish = [int(x) for x in f.read().split(",")]

pop = [1]*256
for i in range(256):
    pop[i] = pop[i-9] + pop[i-7]

def getPopAfterXDays(days):
    return sum(pop[days-i] for i in fish)

print(getPopAfterXDays(256))