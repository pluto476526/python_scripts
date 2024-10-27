import random
import string

def gen_password(length: int = 12) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = lowercase + uppercase + digits + special
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__" :
    print(gen_password())
