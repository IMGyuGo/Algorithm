from collections import deque

n = int(input())
m = int(input())

node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())

    node[s].append(e)
    node[e].append(s)

queue = deque()
queue.appendleft(1)
visited[1] = True

result = 0
while len(queue) != 0:
    vertice = queue.pop()
    li = node[vertice]
    for l in li:
        if visited[l]:
            continue
        else:
            queue.appendleft(l)
            visited[l] = True
            result += 1

print(result)