import sys

with open(sys.argv[1]) as f:
    content = f.read()
poly, raw_subs = content.split('\n\n')
poly = list(poly)

raw_pairs = [raw.split(' -> ') for raw in raw_subs.splitlines()]
substitutions = {x[0]:x[1] for x in raw_pairs}

print('Template: ', ''.join(poly))
for step in range(1,41):
    print('On step: ', step, len(poly))
    new_poly = poly
    for i in range(1,len(poly)*2 - 1,2):
        new_poly.insert(i, substitutions[''.join(poly[i-1:i+1])])

    poly = new_poly
    # print(f'After step {step}: ', ''.join(poly))

counts = [(item,poly.count(item)) for item in set(poly)]
max_tuple = max(counts, key=lambda x: x[1])
min_tuple = min(counts, key=lambda x: x[1])
print('Max tuple: ', max_tuple)
print('Min tuple', min_tuple)
print('Final val: ', max_tuple[1] - min_tuple[1])