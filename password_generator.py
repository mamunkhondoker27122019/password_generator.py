import random
import string

def generate_password(length):
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_chars) for i in range(length))
    return password

password_length = int(input("How many characters do you want in your password? "))
print("Your new password is: " + generate_password(password_length))
