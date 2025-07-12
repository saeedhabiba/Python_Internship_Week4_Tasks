import random
#used for all string sets of characters
import string

#password contains ascii, digits, punctuation etc etc
characters = string.ascii_letters + string.digits + string.punctuation

# Randomly choose 8 characters
password = ''.join(random.choice(characters) for _ in range(8))

print("Generated random password:", password)