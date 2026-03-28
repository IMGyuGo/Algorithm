n = int(input())

dp = {0: 0, 1: 1}


def fibonacci(n):
    if n == 0 or n == 1:
        return dp[n]

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


print(fibonacci(n))