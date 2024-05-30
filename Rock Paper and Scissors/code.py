import random
option=("rock","paper","scissors")
running=True

while running:
    player=None
    computer=random.choice(option)
    while player not in option:
        player=input("\nEnter a choice(rock,paper,scissors)")
    print(f"player:{player}")
    print(f"computer:{computer}")
    if player==computer:
        print("Tie")
    elif player=="rock" and computer=="scissors":
        print("You Win")
    elif player=="paper" and computer=="rock":
        print("You Win")
    elif player=="scissors" and computer=="paper":
        print("You Win")
    else:
        print("You Lose")
    if not input("play again?(y/n)\n").lower()=="y":
        running=False
print("Thank you")



