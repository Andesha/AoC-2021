import sys

def increasing(data):
    current = data[0]
    count = 0
    for item in data[1:]:
        if item > current:
            count += 1
        current = item
    return count

def sliding_window(size, data):
    to_zip = []
    for i in range(size):
        to_zip.append(data[i:])
    zippers = zip(*to_zip)
    return list(zippers)

def sum_groups(data):
    sum_list = []
    for grouping in data:
        sum_list.append(sum(list(grouping)))
    return sum_list

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
    depth_data = [int(x) for x in content]
    windows = sliding_window(3, depth_data)
    summations = sum_groups(windows)
    increases = increasing(summations)
    print(f'Number of increasing depths: {increases}')
