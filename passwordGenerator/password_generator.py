import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    #punctuation = string.punctuation
    punctuation = "!@#$%&"  # Custom punctuation set to avoid issues with certain characters
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Fill the remaining length with a mix of all character sets
    all_characters = lowercase + uppercase + digits + punctuation
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure randomness and convert to a string
    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)



if __name__ == "__main__":
    main()