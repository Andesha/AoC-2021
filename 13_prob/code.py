import sys

with open(sys.argv[1]) as f:
    content = f.read()
dots, folds = content.split('\n\n')
pair_dots = [(int(a), int(b)) for a,b in [x.split(',') for x in dots.splitlines()]]

for fold in folds.splitlines():
    new_dots = set()
    amount = int(fold.split('=')[1])
    for dot in pair_dots:
        if 'x' in fold:
            new_dots.add((dot[0] if dot[0]<amount else amount*2-dot[0],dot[1]))
        else:
            new_dots.add((dot[0],dot[1] if dot[1]<amount else amount*2-dot[1]))

    pair_dots = new_dots
    print('Dots left: ', len(pair_dots))

max_x, max_y = max(pair_dots, key=lambda x: x[0]), max(pair_dots, key=lambda x: x[1])
matrix = [['.' for x in range(max_x[0] + 1)] for y in range(max_y[1] + 1)]
for dot in pair_dots:
    matrix[dot[1]][dot[0]]='#'
for line in matrix:
    print(''.join(line))