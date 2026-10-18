#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
# random.shuffle(letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# random.shuffle(numbers)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# random.shuffle(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))  # ---- i REMOVE int from all of this inputs 

password=""
for char in range(0, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters
    
for char1 in range(0, nr_symbols +1):
    random_symbols = random.choice(symbols)
    password += random_symbols

for char2 in range(0, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers


pass1 = list(password)
random.shuffle(pass1)

str1 = ""
for str in pass1:
    str1 += str
    
print(f"here is password: {str1}")
