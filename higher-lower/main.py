import art
from game_data import data
import random
import os

A = random.choice(data)
B = random.choice(data)


def check(A, B):
    """Checks to see if A is equal to B"""
    while A == B:
        B = random.choice(data)
    return B


def compare(a, b):
    if a['follower_count'] > b['follower_count']:
        return True
    else:
        return False


score = 0
B = check(A, B)


def game(A, B, score):
    os.system('cls')
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    else:
        pass
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == "a":
        comp = compare(A, B)
    else:
        comp = compare(B, A)
    if comp == True:
        score += 1
        A = B
        B = random.choice(data)
        B = check(A, B)
        game(A, B, score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return


game(A, B, score)
