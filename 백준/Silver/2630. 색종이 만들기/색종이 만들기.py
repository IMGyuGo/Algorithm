import sys
input = sys.stdin.readline

n = int(input())
paper = []

for _ in range(n) :
  paper.append(list(map(int, input().split())))

# 하얀색 색종이 개수
paperWhite = 0
# 파란색 색종이 개수
paperBlue = 0

def check(r_s, r_e, c_s, c_e) :
  global paperWhite
  global paperBlue

  if r_s == r_e or c_s == c_e :
    if paper[r_s][c_e] == 0 :
      paperWhite += 1
    else :
      paperBlue += 1
    return

  count = 0
  targetCount = (r_e - r_s + 1) * (r_e - r_s + 1)
  flag = False
  for i in range(r_s, r_e+1) :
    for j in range(c_s, c_e+1) :
      if paper[i][j] == 0 :
        flag = True
        count += 1
      else :
        pass
  
  if flag :
    if count != targetCount :
      check(r_s, (r_s + r_e) // 2, c_s, (c_s+c_e) // 2) # 좌측상단
      check(r_s, (r_s + r_e) // 2, (c_s+c_e) // 2 + 1, c_e) # 좌측하단
      check((r_s+r_e) // 2 + 1, r_e, c_s, (c_s+c_e) // 2) # 우측 상단
      check((r_s+r_e) // 2 + 1, r_e, (c_s+c_e) // 2 + 1, c_e) # 우측하단
    else :
      paperWhite += 1
  else :
    # return에 안걸리고 잘 통과하면
    # 색종이를 돌려서 1이면 추가
    paperBlue += 1

check(0, n-1, 0, n-1)

print(paperWhite)
print(paperBlue)