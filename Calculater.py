print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 -Divide")
option= int(input("Choose an operation:  "))
if(option in [1,2,3,4]):
     num1=float(input("Enter First Number:  "))
     num2=float(input("Enter Second Number:  "))

     if(option==1):
          Result=num1+num2
     elif(option==2):
          Result=num1-num2
     elif(option==3):
          Result=num1*num2
     elif(option==4):
       Result=num1/num2
     print(Result)
else:
    print("Not valid input")
     
