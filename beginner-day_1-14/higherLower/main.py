
from art import logo, vs
from game_data import data
from random import choice


def formatData(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


def checkAnswer(guess, a_followers, b_followers):
    """Take the user guess and followers count and returns True / False"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


#print(logo)
score = 0
game_should_continue = True
account_b = choice(data)

while game_should_continue:
    # Generate random account from data
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: \n\t\t{formatData(account_a)}")
    print(vs)
    print(f"Against B: \n\t\t{formatData(account_b)}")

    # Ask user for guess
    guess = input(f"Who has more followers??? 'A' or 'B':\n\t").lower()

    # Check if user is correct and count followers
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = checkAnswer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, That's wrong. Final Score: {score}")



