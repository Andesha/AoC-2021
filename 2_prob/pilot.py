import sys

def eval_path(data):
    pos = 0
    depth = 0
    aim = 0
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
    pathing = []
    for command in content:
        pair = command.split()
        pathing.append((pair[0], int(pair[1])))
    path_cost = eval_path(pathing)
    print(f'Total path: {path_cost}')