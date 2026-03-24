import sys
from collections import deque

input = sys.stdin.readline

n, target = map(int, input().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))

coins = list(coins)
coins.sort()

queue = deque()
queue.append(0)
visited = set()


coin_cnt = 0
while queue:

    length = len(queue)
    flag = False

    for _ in range(length):
        coin = queue.popleft()
        for c in coins:
            if coin + c in visited:
                continue
            if coin + c < target:
                queue.append(coin + c)
                visited.add(coin + c)
            elif coin + c == target:
                flag = True
                break
        if flag:
            break
    coin_cnt += 1
    if flag:
        break

    if not queue:
        if not flag:
            coin_cnt = -1

print(coin_cnt)