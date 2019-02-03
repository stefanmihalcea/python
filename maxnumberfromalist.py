
def f(x):
  c = x[0]
  
  for i in x:
    if c < i:
      c = i
  
  return(c)
      
        
   
  
print(f([5,6,9,7,4,10]))
