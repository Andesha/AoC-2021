def partition(ss, lower=0, upper=127):
    if lower == upper:
        if len(ss) > 1:
            return lower, partition(ss, 0, 7)
        return lower
    else:
        dist = (upper - lower) // 2
        if ss[0] == 'F' or ss[0] == 'L':
            return partition(ss[1:], lower, upper - dist - 1)
        else:
            return partition(ss[1:], lower + dist + 1, upper)

with open('full.txt') as f:
    content = f.read().splitlines()
seat_ids = list(map(lambda x: x[0]*8 + x[1], [partition(seat) for seat in content]))
missing = [ids for ids in range(min(seat_ids), max(seat_ids)) if ids not in seat_ids]
print(f'Max seat ID: {max(seat_ids)}\nMissing seats in range: {missing}' )
