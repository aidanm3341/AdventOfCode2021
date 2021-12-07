with open('day6/input', 'r') as f:
    currentLanternFish = [int(x) for x in f.read().split(",")]

def reset(index):
    currentLanternFish[index] = 6
    currentLanternFish.append(8)

def ageFishByOne(index):
    currentLanternFish[index] -= 1
    if currentLanternFish[index] < 0:
        reset(index)

for _ in range(256):
    for i in range(len(currentLanternFish)):
        ageFishByOne(i)

print (len(currentLanternFish))