import random
import string

def random_pass_generator():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special   = input("Include special characters? (yes/no): ").strip().lower()
    include_digits    = input("Include digits? (yes/no): ").strip().lower()

    if length < 6:
        print("Password must be at least 6 characters")
        return

    # character sets
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special   = string.punctuation if include_special == "yes" else ""
    digits    = string.digits if include_digits == "yes" else ""

    all_characters = lower + uppercase + special + digits

    if not all_characters:
        print("You must select at least one character type.")
        return

    password_chars = []

    # ensure at least one from each selected type
    if include_uppercase == "yes":
        password_chars.append(random.choice(uppercase))
    if include_special == "yes":
        password_chars.append(random.choice(special))
    if include_digits == "yes":
        password_chars.append(random.choice(digits))

    remaining_len = length - len(password_chars)

    for _ in range(remaining_len):
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)

    return "".join(password_chars)


password = random_pass_generator()
if password:
    print("Generated Password:", password)
