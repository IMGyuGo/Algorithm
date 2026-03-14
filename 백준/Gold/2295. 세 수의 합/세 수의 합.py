import sys
input = sys.stdin.readline

n = int(input())
group = []
for _ in range(n) :
  group.append(int(input()))

group = sorted(group)

dic = {}

for i in range(n) :
  for j in range(i, n) :
    key = group[i] + group[j]
    dic[key] = True

flag = False
for k in range(n-1, -1, -1) :
  if flag :
    break
  for j in range(k+1) :
    key = group[k] - group[j]
    if key in dic :
      # key가 존재하면
      print(group[k])
      flag = True
      break