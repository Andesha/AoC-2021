import sys

with open(sys.argv[1]) as f:
    tank = [int(fi) for fi in f.read().splitlines()[0].split(',')]

for i in range(80):
    new_pop = []
    for fish in tank:
        if fish == 0:
            new_pop.extend([6, 8])
        else:
            new_pop.append(fish - 1)
    tank = new_pop
print('Total fishy: ', len(tank))