import sys

with open(sys.argv[1]) as f:
    puzzle = f.read().splitlines()

slope_pairs = [(1,1), (3,1), (5,1), (7,1), (1,2)]
accum = 1
for sled_right, sled_down in slope_pairs:
    pos = [0,0]
    doh = 0
    while pos[1] < len(puzzle):
        if puzzle[pos[1]][pos[0]] == '#':
            doh += 1
        pos[1] += sled_down
        pos[0] = (pos[0] + sled_right) % len(puzzle[0])
    accum *= doh
print('Accum: ', accum)
