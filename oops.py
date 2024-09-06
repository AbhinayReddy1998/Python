class Player:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def introduce(self):
        print(f"I am {self.name} and I'm level {self.level} ")

    def play(self):
        self.level +=1

player=Player("Harry",100)
player.introduce()
player.play()
print("Name:",player.name)
print("level:",player.level)

Player2=Player("Abhi",101)
Player2.introduce()
Player2.play()
Player3=Player("Reddy",300)
Player3.introduce()
Player3.play()
