import sys
from queue import PriorityQueue
from collections import defaultdict

with open(sys.argv[1]) as f:
    content = [list(x) for x in f.read().splitlines()]


length = len(content)
print(content[length - 1][length - 1])

D = defaultdict(lambda: float('inf'))
D[(0,0)] = 0
pq = PriorityQueue()
pq.put((0, (0,0)))
frontier = set()

while not pq.empty():
    (dist, current_vertex) = pq.get()
    frontier.update(current_vertex)

    for neighbor in [(current_vertex[0]+1,current_vertex[1]), (current_vertex[0]-1,current_vertex[1]), (current_vertex[0],current_vertex[1]+1), (current_vertex[0],current_vertex[1]-1)]:
        if (neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < length and neighbor[1] < length):
            distance = int(content[neighbor[0]][neighbor[1]])
            if neighbor not in frontier:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost

print('Top left to bottom right: ', D[(length - 1,length - 1)])