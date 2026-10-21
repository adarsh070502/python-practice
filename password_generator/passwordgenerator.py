#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lis=[]
lis.append(letters[random.randint(0,len(letters)-1)])

for i in range(nr_letters-1):
    ranpos=random.randint(0,len(lis)-1)
    ranlett=letters[random.randint(0,len(letters)-1)]
    lis.insert(ranpos,ranlett)
    
for i in range(nr_symbols):
    ranpos=random.randint(0,len(lis)-1)
    rannumb=numbers[random.randint(0,len(numbers)-1)]
    lis.insert(ranpos,rannumb)
    
for i in range(nr_numbers):
    ranpos=random.randint(0,len(lis)-1)
    ransym=symbols[random.randint(0,len(symbols)-1)]
    lis.insert(ranpos,ransym)


res="".join(lis)
print(f"password : {res}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P