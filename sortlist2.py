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

  return(x)

print (f([4]))

