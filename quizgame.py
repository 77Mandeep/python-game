print(" welocme to the quiz game")

playing = input( "do you want to play the game? ") 
# here playing is declare as a variable 


if playing.lower() != "yes" :  # playing.lower() turns every answer of user into lower case as they might type YeS ,yES.
    quit() # quit is a inbuilt function which stops the program if the statemet is correct.

print("okay lets play the game") 
score=0 
# here the score is set to zero so that it gets add on later 
answer = input("what does CPU stands for? ")
if answer.lower() == "central proccessing unit":
    print('correct!')
    score +=1 # the score gets on adding if the answer given by user is correct.
else:
    print('incorrect!')
answer= input("what does GPU stands for? ")
if answer.lower() == "graphics proccessing unit":
    print("correct")
    score +=1 # the score gets on adding if the answer given by user is correct.
else:
    print('incorrect!')

answer= input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score +=1 # the score gets on adding if the answer given by user is correct.
else:
    print('incorrect!')


print("You got " + str(score) + " questions correct!") # str le score lai string ma lane kaam garxa 
print("You got " + str((score / 3) * 100) + "%.")