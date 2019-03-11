def f(x):
  g = True
  while g:
    g = False
    for i in range(len(x)-1):
      if x[i] > x[i+1] :
        c = x[i]
        x[i] = x[i+1]
        x[i+1] = c
        g = True
  b = []
  for k in range(len(x)):
    if x[k] not in b:
      b.append(x[k])
  return(b)

print (f([4,4,5,6,7,8,9,3]))
