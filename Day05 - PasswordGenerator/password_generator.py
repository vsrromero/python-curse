"""Password Generator Project"""
import random
import aux_pass_gen as aux

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password?"))
numbers = int(input("How many numbers would you like in your password?"))
symbols = int(input("How many special characters would you like in your password?"))

password = ""

for _ in range (letters):
    password += random.choice(aux.LETTERS)
for _ in range (numbers):
    password += random.choice(aux.NUMBERS)
for _ in range (symbols):
    password += random.choice(aux.SYMBOLS)

password_to_list = list(password)
random.shuffle(password_to_list)
password = ''.join(password_to_list)
print(f"Here is your password: {password}")
