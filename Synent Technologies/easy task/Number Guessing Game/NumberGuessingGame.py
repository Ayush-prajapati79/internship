import  random

number = random.randint( 1,100)
guess = 0
attempt = 1


while guess != number:
  guess = int(input("guess the Number: "))
  attempt +=1

  if (guess< number):
   print("guess the  higher number: ")
  elif (guess > number):
   print("guess the lower number: ")
  else:
   print("!!!congratulation you guss the number")

print(f"you guess the numbber in {attempt} attempt ")





