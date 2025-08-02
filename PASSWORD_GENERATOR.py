import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None
    
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("=== Password Generator ===")
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Please enter a length of at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    pwd = generate_password(length)
    if pwd:
        print("Generated password:", pwd)

if __name__ == "__main__":
    main()
