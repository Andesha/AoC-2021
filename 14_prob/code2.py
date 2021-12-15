import sys
from collections import Counter

with open(sys.argv[1]) as f:
    content = f.read()
poly, raw_subs = content.split('\n\n')

raw_pairs = [raw.split(' -> ') for raw in raw_subs.splitlines()]
substitutions = {x[0]:x[1] for x in raw_pairs}

poly_map = Counter()
for i in range(len(poly)-1):
    poly_map.update((poly[i:i+2],))

fall_off_count = Counter(poly)
for step in range(40):
    poly_map_new = Counter()
    for char_pair,new_char in substitutions.items():
        try_sub = poly_map[char_pair]
        if try_sub == 0:
            continue
        left_pair = char_pair[0] + new_char
        right_pair = new_char + char_pair[1]
        poly_map_new.update({left_pair: try_sub, right_pair: try_sub})
        fall_off_count.update({new_char: try_sub})

    poly_map = poly_map_new

fall_off_count = fall_off_count.most_common()
print(fall_off_count[0][1] - fall_off_count[-1][1])