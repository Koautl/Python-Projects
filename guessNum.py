import random

print("This is a number guessing game")

start = input("are you ready to play?\n")

if start.lower() != "yes" :

    quit()

lowerBound = input("pick the lowest number you want it to be\n")
higherBount = input("pickt the highest number you want it be\n")
num =random.randint(int(lowerBound),int(higherBount))

guess = input("take your first guess\n")
guessCount=0

while int(guess)!=num :
    if int(guess)> num :
        guess = input("The number is lower\n")
        guessCount+=1
    if int(guess)< num :
        guess = input("The number is higher\n")
        guessCount+=1


print("You got it!\n" + "It took you "+ str(guessCount)+" trys\n" + "The number was : " +str(num))
