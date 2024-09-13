class Calculator:

    # create addNumbers static method
    #here we dont create any objects or keep self init thats the usse of static
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))
