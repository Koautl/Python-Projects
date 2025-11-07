import random

points = 0
num = random.randint(1,3)
choices = ['rock','paper','scissor']

start = input("Would you like to start?\n")

if start.lower()!= 'yes':

    quit()

gameCounter=0
wins=0
computerWins=0


while True:

    print("Rock Paper Scissors Says Shoot")
    playerchoice = input().lower()
    if playerchoice=='q':
        break
    if playerchoice not in choices :
        print("please give a valid choice")
        continue
   

    num = random.randint(0,2)
    ComputerChoice=choices[num]
    print("Computer has thrown", ComputerChoice+ ".")

    if playerchoice =='rock' and ComputerChoice=='scissor':
        print("You win")
        wins+=1
    elif playerchoice =='sicissor' and ComputerChoice=='paper':
        print("You win")
        wins+=1
    elif playerchoice=='paper' and ComputerChoice=='rock':
        print("You win")
        wins+=1
    else :
        if playerchoice==ComputerChoice:
            print("Draw")
            gameCounter+=1
        else:
            print("You lost")
            computerWins+=1

gameCounter=gameCounter+computerWins+wins

print("You played",gameCounter,"games\n" "You Won",wins,"times""\nThe Computer won",computerWins,"times")








    
