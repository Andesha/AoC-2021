import sys

with open(sys.argv[1]) as f:
    content =[[x.split(),y.split()] for x,y in [line.split(' | ') for line in f.read().splitlines()]]

valid_len = [2, 3, 4, 7]
valid_map = [1, 7, 4, 8]
accum = 0
for left,right in content:
    mapper = {k:0 for k in range(10)}
    for word in left:
        word_len = len(word)
        lookup = -1
        if word_len in valid_len:
            lookup = valid_len.index(word_len)
        if lookup != -1:
            mapper[valid_map[lookup]] = word

    for word in left:
        if set(mapper[4]).issubset(set(word)) and word not in mapper.values():
            mapper[9] = word
    for word in left:
        word_len = len(word)
        if word_len == 6 and set(mapper[1]).issubset(set(word)) and word not in mapper.values():
            mapper[0] = word
    for word in left:
        word_len = len(word)
        if word not in mapper.values() and word_len == 6:
            mapper[6] = word
    for word in left:
        if not set(word).issubset(set(mapper[9])) and word not in mapper.values():
            mapper[2] = word
    for word in left:
        if not set(word).issubset(set(mapper[6])) and word not in mapper.values():
            mapper[3] = word
    for word in left:
        if word not in mapper.values():
            mapper[5] = word

    flip_map = {''.join(sorted(v)):str(k) for k,v in mapper.items()}
    buffer = ''
    for word in right:
        buffer += flip_map[''.join(sorted(word))]
    accum += int(buffer)

print('Final accum: ', accum)
