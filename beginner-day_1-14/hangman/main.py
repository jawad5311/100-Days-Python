
from random import choice
from words import word_list
import art
import clear

# word_list = ['Aardvark', 'baboon', 'camel']
chosen_word = choice(word_list).lower()
word_length = len(chosen_word)

lives = 6
end_of_game = False

print(art.logo)

# Create Blanks for the chosen word
display = []
for _ in range(word_length):
    display.append("_")


while not end_of_game:
    guess = input(f"Guess a letter: ").lower()

    if guess in display:
        print(f"You have already have guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: "
             # f"{letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # print(display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The right word is \n \t{chosen_word}")

    if "_" not in display:
        end_of_game = True
        print(f"You win.")

    print(f"{art.stages[lives]}")
