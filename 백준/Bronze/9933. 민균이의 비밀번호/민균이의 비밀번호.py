n = int(input())

strList = [input() for _ in range(n)]

stack = []

# 반대로 돌리기가 존재하면 바로 출력
flag = False
for i in range(len(strList)) : 
  if flag :
    break
  if strList[i] == ''.join(reversed(strList[i])) :
    
    print(len(strList[i]), strList[i][len(strList[i])//2])
    break
  else :
    if len(stack) != 0 :
      for j in range(len(stack)) :
        if ''.join(reversed(stack[j])) == strList[i] :
          print(len(strList[i]), strList[i][len(strList[i])//2])
          flag = True
          break
    stack.append(strList[i])