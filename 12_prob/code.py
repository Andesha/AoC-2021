import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    content = [x.split('-') for x in f.read().splitlines()]

rename = {'start': '1', 'end': '0'}
graph = defaultdict(list)
for left,right in content:
    left = rename[left] if left in rename.keys() else left
    right = rename[right] if right in rename.keys() else right
    graph[left].append(right)
    graph[right].append(left)

visit_limiter = [k for k in graph.keys() if k.islower()]
valid_paths = []
def dfs(path, current, freebie):
    if current == '0':
        visit_counts = [path.count(x) for x in visit_limiter]
        if visit_counts.count(2) > 1:
            return
        valid_paths.append(path+'0')
    else:
        for neigh in graph[current]:
            if neigh.islower():
                if path.count(neigh) < 1:
                    dfs((path + current + ','), neigh, freebie)
                elif path.count(neigh) == 1 and freebie:
                    dfs((path + current + ','), neigh, False)

            elif neigh != '1':
                dfs((path + current + ','), neigh, freebie)

dfs('', '1', True)
print(valid_paths)
print(len(valid_paths))