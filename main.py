# Game
""" 0 for Rock """
""" 1 for Paper """
""" 2 for Scissor """
import random
def game():
    bot=random.randint(0,2)
    user=input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: ")
    gamedict={0:"Rock",
              1:"Rock",
              2:"Rock"
    }
    print(f"Yot Choose {gamedict[int(user)]}")

    if bot==int(user):
        print("Draw")

    else :
        if bot==0 and int(user)==1:
            print("You Win")
        elif bot==0 and int(user)==2:
            print("You Lose")
        elif bot==1 and int(user)==0:
            print("You Lose")
        elif bot==1 and int(user)==2:
            print("You Win")
        elif bot==2 and int(user)==0:
            print("You Win")
        elif bot==2 and int(user)==1:
            print("You Lose")

        if user not in ["0","1","2"]:
            print("Invalid Input")

        play_again=input("Do You want to play again? (y/n): ")
        if play_again.lower() !="y":
            print("Thanks for Playing")
            quit()
        else:
            game()

game()