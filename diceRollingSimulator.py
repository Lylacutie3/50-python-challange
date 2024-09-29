import random as r
import os 

def rollD4():
    return r.randint(1, 4)
def rollD6():
    return r.randint(1, 6)
def rollD8():
    return r.randint(1, 8)
def rollD12():
    return r.randint(1, 12)
def rollD20():
    return r.randint(1, 20)
def pickD():
    os.system("clear")
    print("PICK YOUR DICE:")
    pick = int(input("1. D4\n2. D6\n3. D8\n4. D12\n5. D20\n"))
    return pick
def menu():
    os.system("clear")
    print("DICE SIMULATOR")
    D = 1
    pick = pickD()
    while D == 1:
        if pick == 1:
            print("\nYou rolled a D4: ", rollD4())
        elif pick == 2:
            print("\nYou rolled a D6: ", rollD6())
        elif pick == 3:
            print("\nYou rolled a D8: ", rollD8())
        elif pick == 4:
            print("\nYou rolled a D12: ", rollD12())
        elif pick == 5:
            print("\nYou rolled a D20: ", rollD20())
        else :
            pickD()
        D = int(input("\n1. ROLL AGAIN\n2. CHANGE A DICE\n3. EXIT\n"))
    if D == 2:
        menu()
    else:
        exit()

menu()



    
