import random
number = random.randint(1,10)
chances = 5
print("Number Guessing Game")
print("Guess a number (between 1 and 10)")

if chances == 5:
    guess = input("Enter your guess: ") 
    chances = chances - 1
    if guess == number:
        print("Congratulations YOU WON!")
          
if chances == 4:
    guess = input("Wrong guess.Try Again : ") 
    chances = chances - 1
    if guess == number:
        print("Congratulations YOU WON!")

if chances == 3:
    guess = input("Wrong guess.Try Again : ") 
    chances = chances - 1
    if guess == number:
        print("Congratulations YOU WON!")
        
if chances == 2:
    guess = input("Wrong guess.Try Again : ") 
    chances = chances - 1
    if guess == number:
        print("Congratulations YOU WON!")

if chances == 1:
    guess = input("Wrong guess.Try Again : ") 
    chances = chances - 1
    if guess == number:
        print("Congratulations YOU WON!")

if  chances == 0:
        print("YOU LOSE! The number is", number)
else :
        print("YOU LOSE! The number is", number)        