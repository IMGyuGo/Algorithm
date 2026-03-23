import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


visited = [False] * (n + 1)

dfs_list = []


def dfs(start, visited):
    dfs_list.append(start)
    visited[start] = True

    node_list = graph[start]
    node_list.sort()
    for node in node_list:
        if not visited[node]:
            visited[node] = True
            dfs(node, visited)


bfs_list = []


def bfs(start, visited):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(start)
    bfs_list.append(start)
    visited[start] = True

    while queue:
        cur = queue.popleft()
        li = graph[cur]
        li.sort()
        for i in li:
            if visited[i]:
                continue
            else:
                bfs_list.append(i)
                visited[i] = True
                queue.append(i)


dfs(v, visited)
bfs(v, visited)
print(" ".join(map(str, dfs_list)))
print(" ".join(map(str, bfs_list)))