import string

with open('full.txt') as f:
    content = f.read().split('\n\n')

accum = 0
for group in content:
    lookup = {k:0 for k in string.ascii_lowercase}
    for char in group.replace('\n', ''):
        lookup[char] += 1
    people = group.count('\n') + 1
    accum += len([v for v in lookup.values() if v == people])
print(accum)
