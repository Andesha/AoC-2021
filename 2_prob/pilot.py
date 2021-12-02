import sys

def eval_path(data):
    pos = depth = aim = 0
    for direction, amount in data:
        if direction == 'forward':
            pos += amount
            depth += (aim * amount)
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
    return pos * depth

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
    pathing = [(x, int(y)) for x, y in [raw.split() for raw in content]]
    print(f'Total path: {eval_path(pathing)}')
