import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

result = 0
while coins:
    max_coin = coins.pop()

    coin_num = k // max_coin

    if coin_num != 0:
        result += coin_num
        k %= max_coin

        if k == 0:
            break

print(result)