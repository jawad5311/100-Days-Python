
"""
    Mail Merge - Creating letters for users

    Open names file and read names from it.
    Open letter file and read letter format.
    Replace the letter with the user name from names file.
    Creates new file and writes new formatted letter to it.

"""

with open("invited_names.txt") as names_file:
    names = names_file.readlines()  # Returns list of names

with open("starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()  # Read all the content from file
    for name in names:
        f_name = name.strip()  # Strip empty spaces from the string
        # Replace [name] with user name
        new_letter = starting_letter.replace("[name]", f_name)
        print(new_letter)
        with open(f"output/letter_for_{f_name}.txt", "w") as user_file:
            user_file.write(new_letter)  # Write new formatted letter 





