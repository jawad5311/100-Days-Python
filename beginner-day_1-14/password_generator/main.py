
import random
import string


alphabets = string.ascii_lowercase + string.ascii_uppercase
characters = [_ for _ in alphabets]

digits = [_ for _ in string.digits]

symbols = ['!', '#', '$', '%', '(', ')', '*', '+']

print("Password Generator\n\nChoose the number of letters, symbols, and numbers for your password>")
nr_letters = int(input("\tLetters: "))
nr_symbols = int(input("\tSymbols: "))
nr_numbers = int(input("\tNumbers: "))

random_letters = []

for _ in range(nr_letters):
    random_letters.append(random.choice(characters))

for _ in range(nr_symbols):
    random_letters.append(random.choice(symbols))

for _ in range(nr_numbers):
    random_letters.append(random.choice(digits))

random.shuffle(random_letters)
password = ""
for _ in random_letters:
    password += _

print(f"Grab your password below:\n{password}")

