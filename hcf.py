def FINDHCF(X,Y):
   if(X>Y):
      Smaller=Y
   else:
      Smaller=X
   for i in range(1,Smaller+1):
       if(X%i==0) and (Y%i==0):
          hcf=i
   print("HCF of Two numbers are",hcf)

A=int(input("Enter First number: "))
B=int(input("Enter second number: "))
FINDHCF(A,B)

