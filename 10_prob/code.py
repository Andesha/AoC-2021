import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

scores = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}
pair_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
accum = 0
finished = []
for nav in content:
    stack = []
    valid = True
    for char in nav:
        if char in pair_map.keys():
            stack.append(pair_map[char])
        elif stack[-1] == char:
            stack.pop()
        else: # No match, no open
            accum += scores[char][0]
            valid = False
            break

    if valid:
        mult_accum = 0
        while stack:
            mult_accum *= 5
            mult_accum += scores[stack.pop()][1]
        if mult_accum:
            finished.append(mult_accum)

print('Total error score: ', accum)
print('Middle score: ', sorted(finished)[len(finished) // 2])