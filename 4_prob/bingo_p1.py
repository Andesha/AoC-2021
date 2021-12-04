import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
draw_order = [item for item in content.pop(0).split(',')]
blanks = ([i for i, x in enumerate(content) if x == ''])

boards = []
for l,r in zip(blanks, blanks[1:]):
    boards.append([[[x,False] for x in row.split()] for row in content[l+1:r]])

windex = -1
wmove = -1
for move in draw_order:
    for bid, board in enumerate(boards):
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if move == item[0]:
                    board[i][j][1] = True

        for mirror, row in enumerate(map(list, zip(*[list(x) for x in board]))): # Win rows
            if (all([pair[1] for pair in row]) or
                    all([pair[1] for pair in board[mirror]])):
                windex = bid
                wmove = move

    if windex != -1:
        break

accum = 0
for i,row in enumerate(boards[windex]):
    for j,item in enumerate(row):
        if not item[1]:
            accum += int(item[0])
print(f'Winner score: {accum * int(wmove)}')
