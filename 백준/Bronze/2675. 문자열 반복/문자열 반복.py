n = int(input())
for _ in range(n) :
  q = input().split()
  iterNum = int(q[0])
  text = q[1]

  textList = text[:]

  result = ""
  for t in textList :
    result += t*iterNum

  print(result)