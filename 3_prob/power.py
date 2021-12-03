import sys

def most_common(lst):
    occur = {1:lst.count('1'), 0:lst.count('0')}
    if occur[1] == occur[0]:
        return '1'
    return str(max(occur, key=occur.get))

def least_common(lst):
    occur = {1:lst.count('1'), 0:lst.count('0')}
    if occur[1] == occur[0]:
        return '0'
    return str(min(occur, key=occur.get))

def builder(content):
    buffer = ''
    for word in content:
        buffer += max(set(word), key=word.count)
    return buffer

def life_support(words, occur_method):
    index = 0
    while len(words) > 1:
        head_string = [word[index] for word in words]
        most = occur_method(head_string)
        words = [word for word in words if word[index] == most]
        index += 1
    return int(words[0], 2)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
    transpose = map(list, zip(*[list(x) for x in content]))
    gamma_str = builder(transpose)
    gamma = int(gamma_str, 2)
    epsilon = int(''.join(['1' if i == '0' else '0' for i in gamma_str]), 2)
    print(f'Epsilon: {gamma}\t Gamma: {epsilon}')
    print(f'Total Power Consumption: {gamma * epsilon}')
    oxygen = life_support(content[:], most_common)
    co2 = life_support(content[:], least_common)
    print(f'Oxygen: {oxygen}\t CO2: {co2}')
    print(f'Life Support Rating: {oxygen * co2}')
    