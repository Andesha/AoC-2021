import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
depth, width = len(content), len(content[0])

accum = 0; basin_roots = []
for i,row in enumerate(content):
    for j,indiv in enumerate(row):
        assume = True
        for point in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (point[0] >= 0 and point[1] >= 0 and
                    point[0] < depth and point[1] < width):
                if int(indiv) >= int(content[point[0]][point[1]]):
                    assume = False
        if assume:
            accum += 1 + int(indiv)
            basin_roots.append((i,j))
print('Height roots risk: ', accum)

size_list = []
for root in basin_roots:
    frontier = {root}
    queue = [root]
    while queue:
        i,j = queue.pop()
        for point in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (point[0] >= 0 and point[1] >= 0 and
                    point[0] < depth and point[1] < width):
                if (int(content[point[0]][point[1]]) != 9 and
                        point not in frontier):
                    frontier.add(point)
                    queue.append(point)
    size_list.append(len(frontier))
mult_accum = 1
for item in sorted(size_list)[-3:]:
    mult_accum *= item
print(mult_accum)
