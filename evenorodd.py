#Here in this code i have used def function in order to print even and odd numbers separately.

def even(A,B):
   for i in range(A,B+1):
    if i%2 ==0:
        print(i ,end=" , ")
def odd(A,B):
   for i in range(A,B+1):
    if i%2 !=0:
        print(i,end=" , ")
A=int(input("Enter First number:  "))
B=int(input("Enter Second  number: "))
print("Printing Even numbers")
even(A,B)
print("\nPrinting Odd numbers")
odd(A,B)

    
    
   