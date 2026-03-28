import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    appliers = []
    for _ in range(n):
        one, two = map(int, input().split())
        appliers.append((one, two))

    appliers.sort()

    standard = (n + 1, n + 1)

    result = 0
    for i in range(n):
        f, s = standard

        a_f = appliers[i][0]
        a_s = appliers[i][1]

        if s > a_s:
            result += 1
            standard = appliers[i]

    print(result)