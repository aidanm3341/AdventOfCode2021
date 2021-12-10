with open('day10/input', 'r') as f:
    lines = [x for x in f.readlines()]

opening = "([{<"
closing = ")]}>"

pointsMap = {")" : 3,
             "]" : 57,
             "}" : 1197,
             ">" : 25137}

bracketMap = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

stack = []

total = 0
for line in lines:
    for x in [c for c in line]:
        if x in opening:
            stack.append(x)
        elif x in closing:
            el = stack.pop()
            if el != None and x != bracketMap[el]:
                total += pointsMap[x]
                break

print (total)