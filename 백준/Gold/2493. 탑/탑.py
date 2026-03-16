import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))[:]

stack = []
result = []
for i, h in enumerate(top) :
  if i == 0 :
    result.append(0)
    stack.append((i+1, h))
  else :
    flag = False
    for j in range(len(stack)-1, -1, -1) : # stack에는 
      lt_h = stack[j][1]
      lt_i = stack[j][0]
      if lt_h >= h :
        result.append(lt_i)
        stack.append((i+1, h))
        flag = True
        break
      else :
        stack.pop()
    if flag == False :
      result.append(0)
      stack.append((i+1, h))

print(' '.join(map(str, result)))