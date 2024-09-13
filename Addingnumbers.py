class Calculator:
    def __init__(self) :
        pass
    def add (self,num1,num2):
        return num1 + num2
if __name__ == "__main__":
     calculator = Calculator()
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
     result=calculator.add(num1,num2)
     print("Regular method")
     print("Sum",result)
    