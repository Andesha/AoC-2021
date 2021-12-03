import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

candidates = []
for text in content:
    all_info = text.split(':')
    pw_info = {'pw': all_info[1].strip()}
    valid_info = all_info[0].split()
    pw_info['char'] = valid_info[1]
    pw_info['range'] = tuple([int(x) for x in valid_info[0].split('-')])
    candidates.append(pw_info)

count_p1 = 0
count_p2 = 0
for candidate in candidates:
    if candidate['range'][0] <= candidate['pw'].count(candidate['char']) <= candidate['range'][1]:
        count_p1 += 1

    if (candidate['char'] == candidate['pw'][candidate['range'][0] - 1]) ^ (candidate['char'] == candidate['pw'][candidate['range'][1] - 1]):
        count_p2 += 1

print('Valid p1 pws: ', count_p1)
print('Valid p2 pws: ', count_p2)
