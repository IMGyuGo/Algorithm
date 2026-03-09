import math

n = int(input())

def isPrime(num) :

  if num == 0 or num == 1 :
    return False

  for i in range(2, int(math.sqrt(num))+1) :
    if num % i == 0 : 
      return False
  return True

for _ in range(n) :

  num = int(input())

  # 1. 나누기 2가 소수인가
  divide = int(num/2)
  if isPrime(divide) :
    print(divide, divide)
  else :
  # 2. 3부터 (n/2)-1 까지 두 값이 소수인지 확인을 역순으로 체크
    for i in range(int(num/2)-1, 2, -1) :
      a = i
      b = num-i
      if isPrime(a) and isPrime(b) :
        print(a, b)
        break