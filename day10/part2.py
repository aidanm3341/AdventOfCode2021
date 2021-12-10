with open('day10/input', 'r') as f:
    lines = [x for x in f.readlines()]

pointsMap = {")" : 1,
             "]" : 2,
             "}" : 3,
             ">" : 4}

bracketMap = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

scores = []
for line in lines:
    ignore = False
    stack = []
    endStr = ""
    for x in [c for c in line]:
        if x in bracketMap.keys():
            stack.append(x)
        elif x in bracketMap.values():
            el = stack.pop()
            if x != bracketMap[el]:
                ignore = True
                break
    if not ignore:
        while len(stack) > 0:
            endStr += str(bracketMap[stack.pop()])

        score = 0
        for c in endStr:
            score *= 5
            score += pointsMap[c]
        scores.append(score)

print (sorted(scores)[int((len(scores)-1) / 2)])