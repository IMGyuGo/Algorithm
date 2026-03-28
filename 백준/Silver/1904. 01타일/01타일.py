import sys

n = int(input())

dp = [0] * 3
dp[1] = 1 % 15746
dp[2] = 2 % 15746

result_idx = 2
for i in range(3, n + 1):
    result_idx += 1
    result_idx %= 3
    dp[result_idx] = (dp[(result_idx + 1) % 3] + dp[(result_idx + 2) % 3]) % 15746

if n == 1:
    result_idx = 1
print(dp[result_idx])