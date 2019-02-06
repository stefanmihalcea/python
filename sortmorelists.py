def f(x,y):
  a = x + y
  b = []
  for d in range (len(a)):
    d= a[0]
    for i in a:
      if d > i:
        d = i
  
    if d not in b:
      b.append(d)
    a.remove(d)

  return(b)


print(f([1,2,3,4,5],[8,5,7,2,3]))
