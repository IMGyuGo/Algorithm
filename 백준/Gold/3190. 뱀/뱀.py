
from collections import deque

n = int(input()) # NxN 좌표
k = int(input()) # 사과 개수

appleList = []
for _ in range(k) :
  tmp_list = list(map(int, input().split()))
  appleList.append([tmp_list[0]-1, tmp_list[1]-1])

locationList = []
l = int(input()) # 방향개수
for _ in range(l) :
  locationList.append(list(input().split()))


# 방향
location = 0 # 0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위쪽
cord_queue = deque() # [[0, 0], [0, 1]] ... 이렇게 좌표가 들어가 있는 큐
cur_position = [0,0] # 현재 head 위치

# 만약 사과를 만나 길이가 늘어난다면, 현재 위치를 queue에 추가
# 만약 사과가 없다면, 새로운 위치를 queue에 추가하고 queue에서 leftpop

# 초기 cord_queue에 0,0 추가
cord_queue.append(cur_position[:])

# 몇초 동안 살아남았는지를 측정한 변수
s = 0


def move1() :
  global s
  if location == 0 : # 오른쪽
    cur_position[1] += 1
  elif location == 1 : # 아래
    cur_position[0] += 1
  elif location == 2 : # 왼쪽
    cur_position[1] -= 1
  else : # 위
    cur_position[0] -= 1
  
  # 벽 충돌
  if cur_position[0] < 0 or cur_position[0] >= n or cur_position[1] < 0 or cur_position[1] >= n:
      s += 1
      return True
  # 몸 충돌
  if cur_position in cord_queue :
      s+=1
      return True

  # 현재 이동한 위치를 append로 추가
  if cur_position in appleList :
    cord_queue.append(cur_position[:])
    appleList.remove(cur_position)
  else :
    cord_queue.popleft()
    cord_queue.append(cur_position[:])
    
  s+=1
  
  return False
    

def Rotate(C) :
  global location

  if C == 'D' :
    location = (location + 1) % 4
  else :
    if location == 0 :
      location = 3
    else :
      location = (location - 1)

# 조건 1 : 사과가 없다고 가정하고, 구현 (하지만 길이는 5개정도로 생각해보자)
prev = 0
for idx, li in enumerate(locationList):
    X = int(li[0])
    C = li[1]

    for _ in range(X - prev):
        flag = move1()
        if flag:
            print(s)
            exit()

    Rotate(C)
    prev = X

while True:
    flag = move1()
    if flag:
        print(s)
        break