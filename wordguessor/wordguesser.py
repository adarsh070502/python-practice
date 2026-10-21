#Step 1 
import random
from hangman_words import word_list
from hangman_art import  stages,logo

print(logo)

rn=random.randint(0,len(word_list)-1)
chosen_word=word_list[rn]
word_length=len(chosen_word)
temp_lenght=0
total_attempts=6
list1=[]

for i in range(word_length):
  list1.append("_")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while(temp_lenght!=word_length and total_attempts>0):
  guessed_char=input("guess any aplhabet : ")
    
  if(guessed_char in chosen_word):
    for i in range(0,len(chosen_word)):
      if(chosen_word[i] == guessed_char ):
        list1[i]=guessed_char
        temp_lenght+=1
    print("".join(list1))
      
  else:
    print(stages[total_attempts])
    total_attempts-=1
    
if(temp_lenght==word_length and total_attempts>0):
  print("you won")
else:
  print("you lost")
    