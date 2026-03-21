from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    n1, n2 = map(int, input().split())

    graph[n1].append(n2)
    graph[n2].append(n1)

queue = deque()
queue.appendleft(1)
visited[1] = True

result = [0] * (n + 1)
while len(queue) != 0:
    root = queue.pop()
    node_list = graph[root]
    for node in node_list:
        if visited[node]:
            continue
        else:
            queue.appendleft(node)
            visited[node] = True
            result[node] = root

for i in range(2, n + 1):
    print(result[i])