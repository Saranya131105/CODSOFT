import random
import string
password_length = int(input("Enter the desired length for the password: "))
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation
all_characters = uppercase_letters + lowercase_letters + digits + special_characters
password = ''.join(random.choice(all_characters) for _ in range(password_length))
print("Generated Password:", password)