def common(lst, case, tie_val):
    occur = {'1':lst.count('1'), '0':lst.count('0')}
    if occur['1'] == occur['0']:
        return tie_val
    return case(occur, key=occur.get)

def life_support(words, method):
    index = 0
    while len(words) > 1:
        head_string = [word[index] for word in words]
        most = common(head_string, *method)
        words = [word for word in words if word[index] == most]
        index += 1
    return int(words[0], 2)

with open('small_input.txt') as f:
    content = f.read().splitlines()
gamma_buf = ''
for word in map(list, zip(*[list(x) for x in content])):
    gamma_buf += max(set(word), key=word.count)
epsilon = int(''.join(['1' if i == '0' else '0' for i in gamma_buf]), 2)
oxygen = life_support(content[:], (max, '1'))
co2 = life_support(content[:], (min, '0'))
print(f'Total Power Consumption: {int(gamma_buf, 2) * epsilon}')
print(f'Life Support Rating: {oxygen * co2}')
    