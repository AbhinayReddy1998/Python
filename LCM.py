N1=int(input("Enter First number: "))
N2=int(input("Enter Second number: "))
if(N1>N2):
  Greater=N1
else:
  Greater=N2
Value = Greater
while(True):
 if(Greater%N1==0 and Greater%N2==0):
   LCM=Greater
   break
 else:
  Greater = Greater+Value # Here we can use +1 also in place of Value but it takes more itarations

print("LCM of" ,N1, "and", N2 ,"is",LCM)