

from random import choice


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    """Take list of cards as input and calculate sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_scoree, computer_scoree):
    if user_scoree == computer_scoree:
        return "Draw :)"
    elif computer_scoree == 0:
        return "You Lose! Opponent has blackJack"
    elif user_scoree == 0:
        return "Win with BlackJack"
    elif user_scoree > 21:
        return "You went over. You Lose"
    elif computer_scoree > 21:
        return "You Won. Opponent went over"
    elif user_scoree > computer_scoree:
        return "You Won"
    else:
        return "You Lose"


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def play_game():
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: \n \t{user_cards}\nCurrent score: \n\t{user_score}")
        print(f"Computer's first card: \n\t{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            deal_again = input(f"Type 'Y' to get another card, "
                               f"type 'N' to pass\n").lower()
            if deal_again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Play BlackJack? Type 'Y' or 'N': ") == 'y':
    play_game()
