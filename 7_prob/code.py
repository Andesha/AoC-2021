import sys

with open(sys.argv[1]) as f:
    content = [int(item) for item in f.read().splitlines()[0].split(',')]

least = None
move_to = -1
for root in range(max(content)):
    accum = 0
    for crab in content:
        for incr in range(abs(crab - move_to)+1):
            accum += (incr)
    if least == None or accum < least:
        least = accum
        move_to = root

print(least)
print(move_to)