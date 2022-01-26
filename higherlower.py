#importing the necessary packages and modules 
from random import randint

def game():
    value=randint(1,10)
    count=0
    print("I have chosen a random number from 1-10")
    while count!=2:
        guess = int(input("Make your guess:"))
        
        if guess>value:
            print("Oops, the number I guessed is lower than this, try again!")
            count=count+1
        elif guess<value:
            print("Uhoh, the number I guessed is higher than this, try again!")
            count=count+1
        else:
            print("Bang on! You guessed correctly.")
            exit()
    print("I chose %i!" %value)  # değer atamasının farklı bir gösterimi
    
def main():
    print("*************************WELCOME TO THE HIGHER-LOWER GAME*************************")
    print("Instructions: \n1. The computer will randomly choose a number between 1-10\n2. It will ask you to guess which number it chose")
    print("3.You will then make your guess and the computer will tell you if your guess was hugher, lower or equal to its choice\n4. You will get two chances!")
    response = input("Do you wish to play? Respond with y/n: ")
    if response=="y":
        game()
    elif response=="n":
        exit()
    else:
        print("Response invalid!")

main()
            


