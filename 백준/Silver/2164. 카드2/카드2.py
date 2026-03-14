from collections import deque

n = int(input())

queue = deque()

for i in range(1, n+1) :
  queue.append(i)

order = 1
while len(queue) != 1 :
  if order % 2 != 0 :
    queue.popleft()
  else :
    queue.append(queue.popleft())

  order += 1

print(queue.pop())