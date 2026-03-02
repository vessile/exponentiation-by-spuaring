def power(base, exp):
  result = 1

  while exp > 0:
    if exp % 2==1:
       result *= base

   base *= base
   exp//=2
return result

#Örnek test
print(power(2,10)) 
