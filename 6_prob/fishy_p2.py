import sys

with open(sys.argv[1]) as f:
    content = [int(fi) for fi in f.read().splitlines()[0].split(',')]

tank = {i:content.count(i) for i in range(9)}
for step in range(256):
    new_tank = {k:0 for k in range(0,9)}
    for i in range(1,9):
        new_tank[i-1] = tank[i]

    new_tank[8] += tank[0]; new_tank[6] += tank[0]
    tank = new_tank

print('Total fishy: ', sum(tank.values()))