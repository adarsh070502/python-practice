from art import logo
print(logo)

def add(a,b):
  print(f"{a}+{b} = ",a+b,end="")
  return a+b
def multiply(a,b):
  print(f"{a}*{b} = ",a*b,end="")
  return a*b
def division(a,b):
  print(f"{a}/{b} = ",a/b,end="")
  return a/b
def subtract(a,b):
  print(f"{a}-{b} = ",a-b,end="")
  return a-b

result=int(input("what is first number: "))
while(True):
  operation=input("pick operation from +,-,*,/ : ")
  b=int(input("what is next number: "))

  if(operation=="+"):
    result=add(result,b)
  elif(operation=="-"):
    result=subtract(result,b)
  elif(operation=="*"):
    result=multiply(result,b)
  else:
    result=division(result,b)
  print("")
  con=input("do you want to continue yes or no : ")
  if(con=="no"):
    break