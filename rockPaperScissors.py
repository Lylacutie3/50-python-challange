import random as r

def computer_turn():
    pickC = r.randint(1,3)
    return pickC

def game():
    d = 1
    print("\nThis game is classic Rock, Paper, and Scissor game.")
    print("You can play by picking your move, the CPU is your enemy.")
    while d == 1:
        print("\nPick your move")
        user = int(input("1. ROCK 🪨\n2. PAPER 📄\n3. SCISSORS ✂️\n"))
        cpu = computer_turn()
        if user == 1 and cpu == 1 or user == 2 and cpu == 2 or user == 3 and cpu == 3:
            print("\nIt's a tie!")
        elif user == 1 and cpu == 2 or user == 3 and cpu == 1 or user == 2 and cpu == 3:
            print("\nCPU wins!")
        elif user == 1 and cpu == 3 or user == 2 and cpu == 1 or user == 3 and cpu == 2:
            print("\nYou win!")
        else:
            print("\nInvalid input. Please try again.")
        # when the user pick 1 it will continue again 
        d = int(input("\n\nDo you want to play again?\n1. YES\n2. NO\n"))
    if d == 2:
        exit() #when the player do choose not to play again the code will exit
    else:
        print("invalid input!")
        game()


game()