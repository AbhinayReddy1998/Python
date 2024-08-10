number = int(input("enter the number:"))
flag = False
for i in range(2,number):
   if(number % i ==0):
      flag = True
      break
if flag:
   print("Entered number {} is not a prime number".format(number))
else:

   print("Entered number {} is  a prime number".format(number))