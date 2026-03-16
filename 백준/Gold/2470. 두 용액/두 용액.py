# 산성용액 1 ~ 10억
# 알칼리성용액 -1 ~ -10억
# N은 1 ~ 10^5

n = int(input())
drug = list(map(int, input().split()))

# 정렬
# +와 -로 분할 후, +만 존재하면 +끼리만 더하고 -만 존재하면 -끼리만 더하는 형태니까 3가지로 분할
drug = sorted(drug)
minusList = drug[:] # drug 복제
min_val = float('inf')
result = []

# 이진트리 s, e, target
# 절댓값으로 계산
def binarySearch(arr, s, e, target) :
  global min_val

  if s > e :
    return

  mid = (s + e) // 2
  val = arr[mid] + target

  if s == e :
    if abs(val) < min_val :
      result.clear()
      result.append(arr[mid])
      result.append(target)
      min_val = abs(val)
    return

  if abs(val) < min_val :
      result.clear()
      result.append(arr[mid])
      result.append(target)
      min_val = abs(val)
  if val == 0 :
    return
  if val > 0 :
    return binarySearch(arr, s, mid-1, target)
  if val < 0 :
    return binarySearch(arr, mid+1, e, target)
      
result = []
plusList = []

if drug[0] >= 0 : # +만 존재
  result.append(drug[0])
  result.append(drug[1])
elif drug[n-1] <= 0 : # -만 존재
  result.append(drug[n-2])
  result.append(drug[n-1])
else :
  # 먼저 +들을 plusList에 큰값부터 순차적으로 저장 pop()할 때 작은 값부터 뽑아 낼 수 있도록
  for idx in range(len(drug)-1, -1, -1) : # 반대로 돌려서 +를 pop으로 뽑아내기 (list로 구현 해놓았기 때문)
    if drug[idx] > 0 :
      plusList.append(minusList.pop())
    else :
      break

  # 놓친 부분 꼭 -와 +로만 답이 나올 필요가 없다!!
  ml = len(minusList)
  pl = len(plusList)
  if ml >= 2 :
    if abs(minusList[ml-1] + minusList[ml-2]) < min_val :
      min_val = abs(minusList[ml-1] + minusList[ml-2])
      result = [ minusList[ml-2], minusList[ml-1] ]
  if pl >= 2 :
    if abs(plusList[pl-1] + plusList[pl-2]) < min_val :
      min_val = abs(plusList[pl-1] + plusList[pl-2])
      result = [ plusList[pl-1], plusList[pl-2] ]

  # 분할정복 (이진분할탐색)
  # -가 +보다 많다면 (사실 길이가 작은것을 반복문 돌리는 조건을 나누는 게 훨씬 시간복잡도가 낮게 나오는 데 큰 차이가 없다.)
  for p in plusList :
    binarySearch(minusList, 0, len(minusList)-1, p)

print(' '.join(map(str, result)))