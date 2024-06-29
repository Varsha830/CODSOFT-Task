import random
import string

def generate_password(length):
    # Define the character sets for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))

        if length <= 0:
            print("Error: Password length must be greater than zero.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for password length.")


main()