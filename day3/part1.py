with open('day3/input', 'r') as f:
    lines = [int(x, 2) for x in f.readlines()]

def calcBitFrequenciesInColumn(i):
    bitCount = [0, 0]
    for line in lines:
        bit = (1 << i) & line
        bitCount[bit >> i] += 1
    return bitCount


gammaRate = 0
epsilonRate = 0

for i in range(12):
    bitCount = calcBitFrequenciesInColumn(i)

    if(bitCount[1] >= bitCount[0]):
        gammaRate |= (1 << i)
    else:
        epsilonRate |= (1 << i)


print (gammaRate * epsilonRate)