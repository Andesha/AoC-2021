frontier = {}
with open('full.txt') as f:
    for line in [','.join(p.split(' -> ')) for p in f.read().splitlines()]:
        points = [int(x) for x in line.split(',')]
        xdiff = points[2] - points[0]; ydiff = points[3] - points[1]
        steps = max(abs(xdiff), abs(ydiff))
        for i in range(steps + 1):
            point = (points[0] + (xdiff // steps) * i,
                        points[1] + (ydiff // steps) * i)
            frontier[point] = frontier.get(point, 0) + 1
print('Collisions: ', len([values for values in frontier.values() if values > 1]))
