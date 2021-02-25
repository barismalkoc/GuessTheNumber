import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess,  answer, turns):
    """Checks answer.Return the number of turns"""
    if guess > answer:
        print("Too high...")
        return turns - 1
    elif guess < answer:
        print("Too low...")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a diffuculty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    answer = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
             print("You've run out of guesses, you lose...")
             print(f"The number I keep in mind is {answer}")
             return
        elif guess != answer:
            print("One more again !!!!")
game()
