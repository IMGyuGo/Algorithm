n = int(input())
li = list(map(int, input().split()))

visited = [False] * n
max = 0
def dfs(visited, depth, s, e, result) :
  global max

  if depth == n :
    if max < result :
      max = result
    return

  t_e = e
  t_result = result

  for i in range(n) :
    if visited[i] == False :
      visited[i] = True
      if depth == 0 :
        dfs(visited, depth+1, li[i], 0, 0)
      else :
        e = li[i]
        result += abs(s-e)
        dfs(visited, depth+1, e, 0, result)
      visited[i] = False
      e = t_e
      result = t_result
    


dfs(visited, 0, 0, 0, 0)

print(max)