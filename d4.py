# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:42:37 2021

@author: Feyza
"""

#day 4



# WHO'S PAYING ?

import random

# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
print(names)
#Write your code below this line 👇
print(len(names))

num_items=len(names)

random_choice=random.randint(0,num_items-1)
print(random_choice)


print(f"Hesabı {names[random_choice]} ödeyecekkk")

"""

"""

# NESTED LIST


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])




# Treasure Map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal=int(position[0])
vertical=int(position[1])

selected_row=map[vertical-1]
selected_row[horizontal-1]="X"
#print(map[vertical-1])




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



"""





















