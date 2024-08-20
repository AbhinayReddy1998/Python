Questions=("1.What is the captial of England?",
           "2.What is captial of India ?",
           "3.What is capital of SouthAfrica?",
           "4.Higest ODI batting averge in cricket(min 200 matches)")
Options=(("A.London","B.Bristol","C.Cambridge","D.Bath"),
        ("A.Hyderabad","B.Delhi","C.Mumbai","D.Kolkata"),
        ("A.East London","B.Port ELizabeth","C.Alice","D.Cape Town"),
        ("A.Gill","B.Babar","C.Virat","D.Rohit"))
Answers=("A","B","D","C")
question_no=0
Guesses  = []
Score=0
for question in Questions:
    print(question)
    for option in Options[question_no]:
        print (option)

    Guess =input("Enter (A,B,C,D): ").upper()
    Guesses.append(Guess)
    if Guess == Answers[question_no]:
       Score +=10000 
       print("Correct")
       print ("Congratulations !You won " ,Score, "rupees")
    else:
        print("Sorry Your answer is wrong. Thanks for participating in the game ")
        print ("Your take away is" ,Score, "rupees")
        print(f"{Answers[question_no]} is the correct answer")
        break

    question_no+=1