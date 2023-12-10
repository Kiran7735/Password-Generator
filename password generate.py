import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))

        # Check if the password length is valid
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
