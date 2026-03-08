C = int(input())
for _ in range(C) :
  nums = list(map(int, input().split()))
  n = nums[0]
  scores = nums[1:]

  mean = sum(scores)/n
  up = 0
  for score in scores :
    if mean < score :
      up+=1
  
  percent = up / float(n) * 100
  print(f"{percent:.3f}%")