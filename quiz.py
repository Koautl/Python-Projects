print("Hello, this is a simple quiz")

start = input("Are you ready to start?\n")

if start.lower() != "yes":
   
    quit()

print("okay the quiz will begin")
score=0

answer = input("What country is the north of the United States?\n")
if answer.lower() == "canada" :
    score+=1

answer = input("What city is the big bean located in?\n")
if answer.lower() == "chicago":
    score+=1

answer = input ("Who was the first President of the United States? first and last name\n")
if answer.lower() == "george washington":
    score+=1

answer = input("What state did the alamo happen in?\n")
if answer.lower() == "texas" :
    score+=1

answer = input("Which state is known as the garden state? full name\n")
if answer.lower() == "new jersey":
    score+=1

print("thanks for playing, below are your scores")

if score==5:
    print(score*20)
    print("congrats you got a perfect score")
   
else:
    print(score)