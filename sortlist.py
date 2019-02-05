def f(x):
  
  b=[]
  for d in range (len(x)):
    c= x[0]
    for i in x:
      if c > i:
        c = i
  
    b.append(c)
    x.remove(c)

  return(b)
        
   
  
print(f([5,6,9,7,4,10,8]))
