import random
import string

def generate_password(length=8):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols

    password = ''.join(random.choices(all_chars, k=length))

    return password

length = int(input("Enter the desired length of the password: "))

password = generate_password(length)
print("Your new password is:", password)


print("21DCE052")
