import sys

# Ugly and copied from SO, but hey..

def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

with open(sys.argv[1]) as f:
    content = [int(x) for x in f.read().splitlines()]
content.sort()
for item in content:
    lookup = 2020 - item
    if lookup in content:
        print(item*lookup)

print(subsetsum(content, 2020))