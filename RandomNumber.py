
# Program to generate a random number
# importing the random module
import random
def Mynumber(x):
    Randomone= random.randint(1,x)
    Mynumber=0
    while Mynumber!=Randomone:
        Mynumber=int(input("Enter any number for matching = "))
        if Mynumber < Randomone:
            print("Sorry,guess again.Too low")
        elif Mynumber > Randomone:
            print("Sorry,guess again.Too High")

    print("Yay, congrats. You have guessed the correct one",Randomone)
        
Mynumber(10)
 
