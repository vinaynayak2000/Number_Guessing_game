import random


print("Welcome to Number Guessing game")
#Computer randomly generates the number between the given range .
c_no=random.randint(1,11)

#Takes the user input and checks whether the given number entered by user is in given range or not.
user_no=int(input("\nGuess the number between 1-10: "))
while(user_no > 10):
    print("Sorry :-( ...But Please guess the number between the given range....")
    user_no=int(input("Guess the number between 1-10: "))

if(user_no==c_no):
    print("Congo... You Guessed the number.")
elif(user_no > c_no):
    print("Your number is greater....\nComputer's number is",c_no)
elif(user_no < c_no):
    print("Your number is smaller....\nComputer's number is",c_no)

