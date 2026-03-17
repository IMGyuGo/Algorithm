import sys
# input = sys.stdin.readline
data = sys.stdin.buffer.read().split() # 개행 문자로 나누기
it = iter(data)

N = int(next(it))
M = int(next(it))

station_list = [int(next(it)) for _ in range(N)]

prev = [0] * 1000001
nxt = [0] * 1000001

for idx, station in enumerate(station_list) :
  if idx == 0 :
    prev[station] = station_list[len(station_list)-1]
    nxt[station] = station_list[idx+1]
  elif idx == len(station_list)-1 :
    prev[station] = station_list[idx-1]
    nxt[station] = station_list[0]
  else :
    prev[station] = station_list[idx-1]
    nxt[station] = station_list[idx+1]

"""
공사방법
BN i j : i 앞에 있는 역을 출력하고 j 역 설립
BP i j : i 뒤에 있는 역을 출력하고 j 역 설립
CN i : i를 가진 역의 다음 역을 폐쇄하고 폐쇄한 역의 고유 번호 출력
CP i : i를 가진 역의 이전 역을 폐쇄하고 폐쇄한 역의 고유 번호 출력
"""

result = []
# print(dic)
for _ in range(M) :
  # c는 공사방법, i는 현재 역, j는 새로 설립할 역
  c = next(it)

  if c == b'BN' :
    i = int(next(it))
    j = int(next(it))

    N = nxt[i] # 현재 역의 다음역 가져오기
    result.append(str(N)) # 다음 역 출력하기
    nxt[i] = j # 현재 역의 다음 역을 j역으로 변경
    prev[j], nxt[j] = i, N # j역의 이전 역을 i, 다음 역을 N로 생성
    prev[N] = j # 다음역의 이전 역을 j로 변경

  elif c == b'BP' :
    i = int(next(it))
    j = int(next(it))

    P = prev[i] # 현재 역의 이전역 가져오기
    result.append(str(P)) # 이전 역 출력하기
    prev[i] = j # 현재 역의 이전 역을 j역으로 변경
    prev[j], nxt[j] = P, i # j역의 이전 역을 P, 다음 역을 i로 생성
    nxt[P] = j # 이전역의 다음 역을 j로 변경

  elif c == b'CP' :
    i = int(next(it))

    P = prev[i] # 현재 역의 이전역 가져오기
    P1 = prev[P] # 이전 역의 이전역 가져오기
    result.append(str(P)) # 이전 역 출력 하기
    # prev[P], nxt[P] = 0, 0 # 이전 역 삭제
    prev[i] = P1 # 현재 역의 이전 역을 P1으로 변경
    nxt[P1] = i # 이이전 역의 다음 역을 i로 변경
    
  else :
    i = int(next(it))

    N = nxt[i] # 현재 역의 다음역 가져오기
    N1 = nxt[N] # 다음 역의 다음역 가져오기
    result.append(str(N)) # 다음 역 출력 하기
    # prev[N], nxt[N] = 0, 0 # 다음 역 삭제
    nxt[i] = N1 # 현재 역의 다음 역을 N1으로 변경
    prev[N1] = i # 다다음 역의 이전 역을 i로 변경

sys.stdout.write('\n'.join(result))