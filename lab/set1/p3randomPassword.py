import random
import string

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

passwordLength = int(input("Enter the length of the password: "))
if passwordLength <= 0:
    print("Invalid password length. Please enter a positive integer.")

randomPassword = password(passwordLength)
print(f"Random Password: {randomPassword}")


