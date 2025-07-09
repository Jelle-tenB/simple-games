import random

def choose_number():
    number = random.randint(1, 100)
    return number

right_number = choose_number()

print("I'm thinking of a number between 1 and 100.")
#print(f"correct answer is {right_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

def guesser(guesses):
    try:
        print(f"you have {guesses} guesses left")
        guess = int(input("make a guess: "))
        return guess
    except:
        print("That's not a number")
        return guesser()
   
guess = guesser(guesses)   

while guesses > 0:
    if guess == right_number:
        print("you guessed right")
        break
    elif guess > right_number:
        print("Too high")
    else:
        print("Too low")
    guesses -= 1
    if guesses == 0:
        print("You lost")
        break
    guess = guesser(guesses)