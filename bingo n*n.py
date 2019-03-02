import random

n = 3
r = []

while len(r) < n*n:
  a = random.randint(1,n*n)
  if a not in r:
    r.append(a)

b = []
while len(b) < n*n:
  c= random.randint(1,n*n)
  if c not in b:
    b.append(c)

print(b)

for i in range(n):
  m = ''
  for j in range(n):
    m += (' %3s' % str(r[i*n+j]))
  print(m)

bingo = False
for i in range(n):
  if not bingo:
    gh = True
    for j in range(n):
      if not bingo:
        if r[i*n+j] not in b:
          gh = False
    if gh:
      bingo = True
      print("bingo1")

if not bingo:
  for i in range(n):
    if not bingo:
      gh = True
      for j in range(n):
        if not bingo:
          if r[i+j*n] not in b:
            gh = False
      if gh:
        bingo = True
        print("bingo2")
