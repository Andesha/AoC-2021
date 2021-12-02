with open('depth_input.txt') as f:
    data = [int(x) for x in f.read().splitlines()]
summations = [sum(list(group)) for group in zip(data, data[1:], data[2:])]
current = summations[0]; count = 0
for item in summations[1:]:
    if item > current:
        count += 1
    current = item
print(f'Number of increasing depths: {count}')
