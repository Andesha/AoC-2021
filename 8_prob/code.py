import sys

with open(sys.argv[1]) as f:
    content =[[x.split(), y.split()] for x,y in
                [line.split(' | ') for line in f.read().splitlines()]]

valid_len = [(1,2), (7,3), (4,4), (8,7)]
accum = 0
for left,right in content:
    mapper = {}
    for word in left:
        for actual, seg_len in valid_len:
            if len(word) == seg_len:
                mapper[actual] = word
    left = [item for item in left if item not in mapper.values()]

    for word in left:
        if set(mapper[4]).issubset(set(word)):
            mapper[9] = word; left.remove(word)
    for word in left:
        word_len = len(word)
        if word_len == 6 and set(mapper[1]).issubset(set(word)):
            mapper[0] = word; left.remove(word)
    for word in left:
        word_len = len(word)
        if word not in mapper.values() and word_len == 6:
            mapper[6] = word; left.remove(word)
    for word in left:
        if not set(word).issubset(set(mapper[9])):
            mapper[2] = word; left.remove(word)
    for word in left:
        if not set(word).issubset(set(mapper[6])):
            mapper[3] = word; left.remove(word)
    for word in left:
        if word not in mapper.values():
            mapper[5] = word; left.remove(word)

    flip_map = {''.join(sorted(v)):str(k) for k,v in mapper.items()}
    buffer = ''
    for word in right:
        buffer += flip_map[''.join(sorted(word))]
    accum += int(buffer)

print('Final accum: ', accum)
