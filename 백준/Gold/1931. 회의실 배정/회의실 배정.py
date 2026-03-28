import sys

input = sys.stdin.readline

n = int(input())

meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((e, s))

meetings.sort()

for idx, meeting in enumerate(meetings):
    e, s = meeting
    meetings[idx] = (s, e)

start = meetings[0]
result = 1
for idx, meeting in enumerate(meetings):
    if idx != 0:
        e = start[1]
        s = meeting[0]

        if e <= s:
            result += 1
            start = meeting

print(result)