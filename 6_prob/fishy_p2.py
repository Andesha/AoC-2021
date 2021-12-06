import sys

with open(sys.argv[1]) as f:
    tank = [int(fi) for fi in f.read().splitlines()[0].split(',')]

tank_frontier = {}
for i in range(9):
    tank_frontier[i] = tank.count(i)

for step in range(256):
    forward_spawn = tank_frontier[0]
    new_frontier = {k:0 for k in range(0,9)}
    for i in range(1,9):
        new_frontier[i-1] = tank_frontier[i]

    new_frontier[8] += forward_spawn
    new_frontier[6] += forward_spawn

    tank_frontier = new_frontier

print(tank_frontier.values())
print(sum(tank_frontier.values()))
