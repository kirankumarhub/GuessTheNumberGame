
import random

rounds = 0
while rounds == 0:
    try:
        num = input("Number of games to play")
        rounds = int(num)
    except:
        print('Enter a integer number for  number of games to play')
        continue
         
round = 0
i = 0
while rounds > i:
    
    guesscount = 0
    guess = -1
    rand = random.randint(1,100)
    while guess == -1:
        try:
            
            guess = int(input("Guess a number between 1 to 100 or 0 to break"))
            guesscount = guesscount + 1
            if(guess == 0) :
                print("Thanks for playing game")
                break
            elif(guess == rand) : 
                print("Success , you tried %d time(s) Correct guess is %d " % (guesscount,rand) )
                rand = random.randint(1,100)
                break
            elif(guess > rand) :
                print("Your guess is very high")
                guess = -1
            elif(guess < rand) :
                print("Your guess is very low")
                guess = -1                
        except:
            print('Enter a integer number as your guess')
            continue
        
    i = i + 1
