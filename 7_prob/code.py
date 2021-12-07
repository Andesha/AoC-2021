with open('full.txt') as f:
    content = [int(item) for item in f.read().split(',')]

least_fuel, best_move = None, -1
for root in range(max(content)):
    accum = 0
    for crab in content:
        interm = abs(crab - root) + 1
        accum += (interm*(interm - 1)) // 2
    if least_fuel == None or accum < least_fuel:
        least_fuel = accum; best_move = root

print(f'Move to: {best_move}\tFuel Cost: {least_fuel}')
