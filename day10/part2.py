with open('day10/input', 'r') as f:
    lines = [x for x in f.readlines()]

opening = "([{<"
closing = ")]}>"

pointsMap = {")" : 1,
             "]" : 2,
             "}" : 3,
             ">" : 4}

bracketMap = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

stack = []

linesToRemove = []
for line in lines:
    for x in [c for c in line]:
        if x in opening:
            stack.append(x)
        elif x in closing:
            el = stack.pop()
            if el != None and x != bracketMap[el]:
                linesToRemove.append(line)
                break

for line in linesToRemove: lines.remove(line)

stack = []
scores = []
for line in lines:
    endStr = ""
    for x in [c for c in line]:
        if x in bracketMap.keys():
            stack.append(x)
        elif x in bracketMap.values():
            stack.pop()
    while len(stack) > 0:
        endStr += str(bracketMap[stack.pop()])

    score = 0
    for c in endStr:
        score *= 5
        score += pointsMap[c]
    scores.append(score)

print (sorted(scores)[int((len(scores)-1) / 2)])