#Password Generator Project
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# 
letters = ['a', 'b','c', 'd', 'e']
numbers = ['0', '1']
symbols = ['!', '#', '$']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password=""
random_char=[]

# nr_letters=4
for char in range(1,nr_letters+1):
     s=random.choice(letters)
     #password=password+s
     random_char.append(s)

for char in range(1,nr_numbers+1):
     s=random.choice(numbers)
     #password=password+s
     random_char.append(s)
     
for char in range(1,nr_symbols+1):
     s=random.choice(symbols)
     #password=password+s
     random_char.append(s)


a=str(random.shuffle(random_char))
     
print(random_char)


    
    