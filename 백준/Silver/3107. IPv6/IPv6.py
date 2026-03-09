ipv6 = input()
ipv6List = ipv6.split(":")

size = len(ipv6List)

if size == 9 :
  if len(ipv6List[0]) == 0 :
    ipv6List.pop(0)
    for _ in range(9-size) :
      ipv6List[0] = "0000"
  elif len(ipv6List[-1]) == 0 :
    ipv6List.pop(8)
    for _ in range(9-size) :
      ipv6List[7] = "0000"

else :
  noIdx = 0
  for idx in range(size) :
      if len(ipv6List[idx]) == 0 :
        noIdx = idx
  for _ in range(8-size) :
    ipv6List.insert(noIdx, "0000")

for idx in range(8) :
  ipv6List[idx] = ipv6List[idx].zfill(4)

print(':'.join(ipv6List))