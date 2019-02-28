import random

r = []

while len(r) < 9:
  a = random.randint(1,9)
  if a not in r:
    r.append(a)

b = []
for i in range(9):
  c= random.randint(1,9)
  b.append(c)


print( r[0], r[1], r[2])
print( r[3], r[4], r[5])
print( r[6], r[7], r[8])

print(b)
bingo = False
for z in range(2):
  if r[z] in b and r[z+3] in b and r[z+6] in b:
    print("bingo")
    bingo = True

if not bingo:
  for d in range(2):
    if r[d*3] in b and r[d*3+1] in b and r[d*3+2] in b:
      print("bingo")
