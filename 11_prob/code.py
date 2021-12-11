import sys

with open(sys.argv[1]) as f:
    pop = [[int(y) for y in x] for x in f.read().splitlines()]
width, height = len(pop[0]), len(pop)

grid_size = width * height
accum = 0
for step in range(1, 10_000): # it better happen before then...
    flashes = 0
    pop = [[x + 1 for x in row] for row in pop]
    stack = []
    for i, row in enumerate(pop):
        for j, item in enumerate(row):
            if item > 9:
                stack.append((i,j))
    while stack:
        i, j = stack.pop()
        flashes += 1
        for offi in range(-1,2,1):
            for offj in range(-1,2,1):
                newi = i + offi
                newj = j + offj
                if newi >= 0 and newj >= 0 and newi < height and newj < width:
                    pop[newi][newj] += 1
                    if pop[newi][newj] == 10:
                        stack.append((newi, newj))
    accum += flashes
    pop = [[0 if x > 9 else x for x in row] for row in pop]

    if flashes == grid_size:
        break
print(f'Synch: {step}')