import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

result = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    queue = deque()
    queue.append(i)
    visited[i] = True

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    result += 1

print(result)