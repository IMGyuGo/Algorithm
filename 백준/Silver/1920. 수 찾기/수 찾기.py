n = int(input())
qList = list(map(int, input().split()))
m = int(input())
aList = list(map(int, input().split()))

qList = sorted(qList)

def search(arr, s, e, target) :
  # 중앙값
  mid = (s + e) // 2
  
  # base condition 생각
  if e <= s :
    if arr[mid] == target :
      return 1
    else :
      return 0
  
  if arr[mid] > target :
    return search(arr, s, mid-1, target)
  elif arr[mid] < target :
    return search(arr, mid+1, e, target)
  else :
    return 1
  

for i in range(m) :
  target = aList[i]
  print(search(qList, 0, n-1, target))