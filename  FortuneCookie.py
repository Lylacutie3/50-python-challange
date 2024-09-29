#exercise no.1 (if/else)
import random as r

def generate_random():
    pick = r.randint(1,8)
    if pick == 1:
        return print("Everyone agrees. You are the best.")
    elif pick == 2:
        return print("If you have something worth fighting for, then fight for it")
    elif pick == 3:
        return print("It’s better to be alone sometimes.")
    elif pick == 4:
        return print("You are stronger than you think.")
    elif pick == 5:
        return print("Never give up. Always find a reason to keep trying.")
    elif pick == 6:
        return print("You are very talented in many ways.")
    elif pick == 7:
        return print("You must try, or hate yourself for not trying.")
    else:
        return print("Come back later, I am sleeping. Yes cookies need their sleep too.")
    
print("Do you want to open the cookie?")
ans = int(input("1. YES\n2. NO\n\n"))
if ans == 1:
    generate_random()
else:
    print("okay.")
