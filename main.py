import random
from game_data import data
game_end=False
score=0
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    account_followers = account["follower_count"]
    return f"{account_name} is a/an {account_descr}, from {account_country}"
while game_end==False:
    account_a=random.choice(data)
    account_b=random.choice(data)
    while account_b==account_a:
        account_b=random.choice(data)

    print(f"Compare A:{format_data(account_a)}\nVS.")
    print(f"Compare B:{format_data(account_b)}")
    if account_a["follower_count"]>account_b["follower_count"]:
        higher=0
    else:
        higher=1
    answer=input("Who has more followers? Type 'A' or 'B'").lower()
    if answer is "a":
        if higher==1:
            score+=1
            print("\nCorrect!\n")
        else:
            print(f"Wrong! You Lose! Score:{score}")
            game_end=True
    else:
        if higher==0:
            score+=1
            print(" \nCorrect!\n")
        else:
            print(f"Wrong! You Lose! Score:{score}")
            game_end=True