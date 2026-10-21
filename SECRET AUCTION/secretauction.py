import os
import time
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

def clear(seconds = 0):
 time.sleep(seconds)
 os.system('clear')

dict={}
temp=True

def entry():
  name=input("Your name : ")
  bid=int(input("your bid : "))
  dict[name]=bid

entry()
  
while(temp):
  any_bidders=input("are there any other bidders yes or no : ")
  if(any_bidders=="yes"):
    clear()
    entry()
    
  else:
    max=0
    person=""
    for key in dict:
      if(dict[key]>max):
        max=dict[key]
        person=key
    print(f"The winner is {person} with bid {max}.")
    break
    