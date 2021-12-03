with open('day3/input', 'r') as f:
    lines = [int(x, 2) for x in f.readlines()]

numCols = 12

def calcBitFrequenciesInColumn(i, input):
    bitCount = [0, 0]
    for line in input:
        bit = (1 << i) & line
        bitCount[bit >> i] += 1
    return bitCount

def getMostCommonBit(i, input):
    bitCount = calcBitFrequenciesInColumn(i, input)
    if(bitCount[1] >= bitCount[0]):
        return 1
    else:
        return 0

def getLeastCommonBit(i, input):
    bitCount = calcBitFrequenciesInColumn(i, input)
    if(bitCount[1] < bitCount[0]):
        return 1
    else:
        return 0

def findRatingWithBitCritera(bitCriteria):
    input = lines.copy()
    for i in range(numCols-1, -1, -1):
        bit = bitCriteria(i, input)
        input = list(filter(lambda num: num & (1 << i) == (bit << i), input))

        if(len(input) == 1):
            return input[0]


oxygenGeneratorRating = findRatingWithBitCritera(getMostCommonBit)
c02ScrubberRating = findRatingWithBitCritera(getLeastCommonBit) 

print(oxygenGeneratorRating * c02ScrubberRating)
