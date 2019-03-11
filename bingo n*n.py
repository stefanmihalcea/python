import random
b = True
while b:
  d = input("welcher Zahlenbereich?:")
  dg = int(d)
  n = input("wie viele zahlen?(n*n):")
  ng = int(n)
  if dg <= ng*ng:
    print("die erste Zahl muss größer als das Quadrat der zweiten")
  else:
    b = False


r = []


while len(r) < ng*ng:
  a = random.randint(1,dg)
  if a not in r:
    r.append(a)

b = []
while len(b) < ng*ng:
  c= random.randint(1,dg)
  if c not in b:
    b.append(c)

print(b)

for i in range(ng):
  m = ''
  for j in range(ng):
    m += (' %3s' % str(r[i*ng+j]))
  print(m)

bingo = False
for i in range(ng):
  if not bingo:
    gh = True
    for j in range(ng):
      if not bingo:
        if r[i*ng+j] not in b:
          gh = False
    if gh:
      bingo = True
      print("bingo1")

if not bingo:
  for i in range(ng):
    if not bingo:
      gh = True
      for j in range(ng):
        if not bingo:
          if r[i+j*ng] not in b:
            gh = False
      if gh:
        bingo = True
        print("bingo2")
