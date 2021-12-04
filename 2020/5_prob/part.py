import sys
import math

def partition(ss, lower=0, upper=127):
    if lower == upper:
        if len(ss) > 1:
            return lower, partition(ss, 0, 7)
        return lower
    else:
        dist = (upper - lower) // 2
        if ss[0] == 'F' or ss[0] == 'L':
            return partition(ss[1:], lower, upper - dist - 1)
        else:
            return partition(ss[1:], lower + dist + 1, upper)

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
seat_ids = map(lambda x: x[0]*8 + x[1], [partition(seat) for seat in content])
print('Max seat ID: ', max(seat_ids))
