first = int(input("enter the FIrst number:  "))
second = int(input("enter second number:  "))
for num in range(first,second):
 if num >1:
  for i in range (2,num):
   if(num % i)==0:
       break
  else:
       print(num)
