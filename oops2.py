class Dog:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def speak(self):
        print("my name is {} and my age is {}".format(self.name,self.age))

abhi=Dog("abhi",26)
Sanju=Dog("Sanju",24)
abhi.speak()
Sanju.speak()

    