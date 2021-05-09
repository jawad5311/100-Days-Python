# Alphabets a - z
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

should_continue = True


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "D":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction} text is: \n {end_text}")


while should_continue:
    direction = input(f"Type 'E' to encrypt, \n type 'D' to " f"decrypt:\n").upper()
    text = input(f"Type you message:\n").lower()
    shift = int(input(f"Type the shift number:\n")) % 26
    ceasar(text, shift, direction)

    result = input(f"Type 'Y' if you want to go again. Otherwise type 'N'\n")
    if result == "n":
        should_continue = False
        print(f"Finished")
