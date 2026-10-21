from art import logo,vs
from game_data import data
import random
import os

final_score=0
rn=random.randint(0,len(data)-1)
compare=data[rn]
def comparing(compare,against,answer):
    if(compare["follower_count"]>against["follower_count"]):
        return "A"
    else:
        return "B"

while(True):
    print(logo)
    print(f"You are right!     current score : {final_score}")
    
    rn=random.randint(0,len(data)-1)
    against=data[rn]

    print(f"Comapare A : {compare['name']}, {compare['description']}")
    print(vs)
    print(f"Against B : {against['name']}, {against['description']}")
    answer=input("Guess A or B : ")

    res=comparing(compare,against,answer)

    if(answer==res and res=="B"):
        os.system('cls')
        final_score+=1
        compare=against
        
    elif(answer==res):
        os.system('cls')
        final_score+=1
    else:
        print(f"You lost   final_score : {final_score}")
        break
    

