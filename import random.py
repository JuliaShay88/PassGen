import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    # Define character sets based on user input
    character_sets = []
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_numbers:
        character_sets.append(string.digits)
    if include_symbols:
        character_sets.append(string.punctuation)

    # Generate password using selected character sets
    password = ''
    for i in range(length):
        password += random.choice(random.choice(character_sets))

    return password