with open('input.txt') as f:
    pathing = [(x, int(y)) for x, y in [raw.split() for raw in f.read().splitlines()]]
    pos = depth = aim = 0
    for direction, amount in pathing:
        if direction == 'forward':
            pos += amount
            depth += (aim * amount)
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
    print(f'Total path: {pos*depth}')
