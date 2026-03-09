text = input()
text = text.upper()
textList = text[:]

info = {}
for i in range(len(textList)) :
  if textList[i] in info.keys() :
    info[textList[i]] += 1
  else :
    info[textList[i]] = 1

max = max(info.values())

result = ''
dupli = 0
for k in info.keys() :
  if info[k] == max :
    dupli+=1
    result = k

if dupli != 1 :
  print('?')
else :
  print(result)