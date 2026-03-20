from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    start = 0
    airplane = {i: [] for i in range(1, n + 1)}
    for idx in range(m):
        s, e = map(int, input().split())
        if idx == 0:
            start = s
        airplane[s].append(e)
        airplane[e].append(s)

    visited = [start]
    queue = deque()
    queue.appendleft(start)
    result = 0

    while len(queue) != 0:
        vertice = queue.pop()
        airList = airplane[vertice]
        for a in airList:
            if a in visited:
                continue
            else:
                queue.appendleft(a)
                visited.append(a)
                result += 1

    print(result)