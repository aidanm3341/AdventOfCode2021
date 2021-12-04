with open('day4/input', 'r') as f:
    lines = f.read().split("\n\n")

calledNumbers = lines[0].split(',')
boards = []

gridWidth = 5
gridHeight = 5

for board in lines[1:]:
    boards.append(list(map(lambda x: (x, False), filter(''.__ne__, board.replace("\n", " ").split(" ")))))



def getValueAt(board, x, y):
    return board[x + y * gridWidth]

def setValueAt(board, x, y, val):
    board[x + y * gridWidth] = val

def markNumIfExists(board, num):
    for i in range(gridWidth):
        for j in range(gridHeight):
            value = getValueAt(board, i, j)
            if value[0] == num:
                setValueAt(board, i, j, (num, True))

def callNumber(num):
    for board in boards:
        markNumIfExists(board, num)


def checkRows(board):
    for y in range(gridHeight):
        trueCount = 0
        for x in range(gridWidth):
            val = getValueAt(board, x, y)
            if val[1] == True:
                trueCount += 1
        if trueCount == gridWidth: # Win!
            return True
    return False

def checkCols(board):
    for x in range(gridWidth):
        trueCount = 0
        for y in range(gridHeight):
            val = getValueAt(board, x, y)
            if val[1] == True:
                trueCount += 1
        if trueCount == gridHeight: # Win!
            return True
    return False

def checkForWinners():
    for board in boards:
        if checkRows(board) or checkCols(board):
            return board
    return None



for num in calledNumbers:
    callNumber(num)
    winner = checkForWinners()
    if winner != None:
        print (sum([int(x) for x, y in winner if y == False]) * int(num))
        break



