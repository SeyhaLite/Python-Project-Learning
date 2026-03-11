import random

result = random.randint(1, 10)
life = 5
print("Welcome To Casino Win WIn")
print("Chouse Your Lucky Number 1-10")

while True:
  Number = int(input("Please Enter Number 1-10\n"))
  if Number < 1 and Number > 1:
    print("The Number Can Only 1-10")
    continue

  if Number == result:
    print(f"You Won\nThe Result : {Number}")
    break
  elif Number < result:
    print("Your Number is smaller thna result")
    life = life - 1
    print(f"Your Life Now : {life}")
  elif Number > result:
    print("Your Number is bigger than result")
    life = life - 1
    print(f"Your Life Now : {life}")
    
               
