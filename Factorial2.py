Number =int(input("Enter any number : "))
print("Given factorial number is" , Number)
print("Showing how factorial works ")
factorial=1
for i in range(1,Number+1):
    print(factorial ,"*" ,i , "= ",end= "")
    factorial = factorial * i
    
    print( factorial)
