# import python.py file from another python.py document
#Generate a random account from the game data
#format the account data into printable format
# ask user for a guess
#check if user is correct 
#get follower count of each account
#use if statement to check if user is correct
#give user feedback on their guess
#score keeping
# make the game repeatable. 
#making account at position B become the next account at position A.


import random

#print(data)
#c=random.choice(data)
#print(c)
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }

]





score=0
#print(data)
#c=random.choice(data)
#print(c)
game_should_continue=True
account_b=random.choice(data)
while game_should_continue:

    def format_data(account):
      #format the account data into printable format
    #Take the account data and returns the printable format.
        account_name=account["name"]
        account_descr=account["description"]
        account_country=account["country"]


        return (f"{account_name},a,{account_descr},from {account_country}")

    def check_answer(guess,a_followers,b_followers):
      """Take the user guess and follower counts and returns if they got it right"""
      if a_followers> b_followers:
          return guess=="a"
      else:
          return guess=="b"


    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
      account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.") #format_data içinde fonksiyonu çağırdık
  
    print(f"Against B: {format_data(account_b)}.")

    guess=input("Who has more followers Please Type A or B        ").lower()


    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correct=check_answer(guess,a_follower_count,b_follower_count)
 

    if is_correct:
      score+=1
      print(f"You are right Final Score {score} ")
    else:
      game_should_continue=False
      print("Sorry ,that's wrong")

