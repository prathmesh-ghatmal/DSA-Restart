import random
def guess_game():
    random_no=random.randint(1,10)
    while True:
        no=int(input("guess no from 1 to 10"))
        if no==random_no:
            print("yay you got this")
            break
        else:
            print("opps try again")

guess_game()