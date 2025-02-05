import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
pyc=True
while ((pyc)):
    print("Enter your Choice:")
    print("1:Rock\n2:Paper\n3:Sissors")
    ch=int(input("Enter Your Choice:"))
    print("  ")
    def choice(ch):
        if ch==1:
            return "Rock"
        if ch==2:
            return "Paper"
        if ch==3:
            return "Sissors"
    print("User's Choice:",choice(ch))
    def computer():
        k=random.randint(1,3)
        return k
    temp=computer()
    def computer_choice(te):
        if te==1:
            print("Computer's choice is:Rock")
        if te==2:
            print("Computer's choice is:Paper")
        if te==3:
            print("Computer's choice is:Sissors")
    computer_choice(temp)
    def process(t,us):
        if t==1 and us==3:
            print(choice(t),"VS",choice(us),sep=" ")
            print("<---Computer Wins--->")
        if t==3 and us==1:
            print(choice(us),"VS",choice(t),sep=" ")
            print("<---Player Wins--->")
        if t==1 and us==2:
            print(choice(us),"VS",choice(t),sep=" ")
            print("<---Player Wins--->")
        if t==2 and us==1:
            print(choice(t),"VS",choice(us),sep=" ")
            print("<---Computer Wins--->")
        if t==2 and us==3:
            print(choice(t),"VS",choice(us),sep=" ")
            print("<---Player Wins--->")
        if t==3 and us==2:
            print(choice(us),"VS",choice(t),sep=" ")
            print("<---Computer Wins--->")
        if t==us:
            print("<--Draw-->")
    process(temp,ch)
    a=input("Do you want to play again (y/n):")
    if a=="y":
        pyc=True
    if a=="n":
        pyc=False
    if a!="y" and a!="n":
        print("Invalid input")
        a=input("Do you want to play again (y/n):")



