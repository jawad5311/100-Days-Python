
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input(f"Choose Difficulty: \n\t Hard --> H\n\t Easy --> E\n").lower()

    if difficulty == "h":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def check_answer(guess, answer, turn):
    if guess > answer:
        print("Too High")
        return turn - 1
    elif guess < answer:
        print("Too low")
        return turn - 1
    else:
        print(f"You guessed the Secret Number '{answer}' right...")




def game():
    answer = random.randint(1, 100)
    print(answer)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\n\tRemaining Attempts: {turns}\n")
        guess = int(input("Make a Guess: \n\t"))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, You Lose")
            return


game()