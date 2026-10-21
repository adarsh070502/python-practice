from art import logo
import random
print(logo)

def anotherblackjack():
  temp=input("do you want to play another game y or n : ")
  if(temp=="y"):
    blackjack()
  else:
    print("game ended")

def end_game(user_cards,computer_cards):
  print(f"Your final cards : {user_cards}, current score:{sum(user_cards)}")
  computer_cards.append(cards[random.randint(0,12)])
  print(f"computer last hand : {computer_cards}, computer final score : {sum(computer_cards)}")
  print("you over went\n game over")
  anotherblackjack()

def end_game_computer(user_cards,computer_cards):
  print(f"Your final cards : {user_cards}, current score:{sum(user_cards)}")
  print(f"computer last hand : {computer_cards}, computer final score : {sum(computer_cards)}")
  print("computer over went, YOU WON!!!!")
  anotherblackjack()

def compare(a,b):
  if(a>b):
    return 1
  elif(b>a):
    return 2
  else:
    return 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  user_cards=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
  computer_cards=[cards[random.randint(0,12)]]
  
  print(f"Your cards : {user_cards}, current score : {sum(user_cards)}")
  print(f"computer first card : {computer_cards[0]}")

  while(True):
    another_card=input("type y to get another card or n for no :") 
    
    if(another_card=="y"):
      user_cards.append(cards[random.randint(0,12)])
      print(f"Your cards : {user_cards}, current score : {sum(user_cards)}")
      print(f"computer first card : {computer_cards[0]}")
      if(sum(user_cards)>21):
        end_game(user_cards,computer_cards)
                       
    else:
      print(f"Your cards : {user_cards}, final current score : {sum(user_cards)}")
  
      computer_cards.append(cards[random.randint(0,12)])
      while(sum(computer_cards)<17):
          computer_cards.append(cards[random.randint(0,12)])

      if(sum(computer_cards)>21):
        end_game_computer()
        anotherblackjack()
      res=compare(sum(user_cards),sum(computer_cards))
      if(res==0):
        print(f"Your final cards : {user_cards}, current score:{sum(user_cards)}")
        print(f"computer last hand : {computer_cards}, computer final score : {sum(computer_cards)}")
        print("draw")

      elif(res==1):
        print(f"Your final cards : {user_cards}, current score:{sum(user_cards)}")
        print(f"computer last hand : {computer_cards}, computer final score : {sum(computer_cards)}")
        print("you won")

      else:
        print(f"Your final cards : {user_cards}, current score:{sum(user_cards)}")
        print(f"computer last hand : {computer_cards}, computer final score : {sum(computer_cards)}")
        print("computer won")
      anotherblackjack()
        
      
blackjack()      

    
    