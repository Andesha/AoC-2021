def life_support(words, method, tie_val):
    index = 0
    while len(words) > 1:
        head_str = [word[index] for word in words]
        occur = {'1':head_str.count('1'), '0':head_str.count('0')}
        most = method(occur, key=occur.get)
        if occur['1'] == occur['0']:
            most = tie_val # Overwrite in tie case
        words = [word for word in words if word[index] == most]
        index += 1
    return int(words[0], 2)

with open('small_input.txt') as f:
    content = f.read().splitlines()
gamma_buf = '' # Below is the transpose of content list
for word in map(list, zip(*[list(x) for x in content])):
    gamma_buf += max(set(word), key=word.count)
epsilon = int(''.join(['1' if i == '0' else '0' for i in gamma_buf]), 2)
oxygen = life_support(content[:], max, '1')
co2 = life_support(content[:], min, '0')
print(f'Total Power Consumption: {int(gamma_buf, 2) * epsilon}')
print(f'Life Support Rating: {oxygen * co2}')
