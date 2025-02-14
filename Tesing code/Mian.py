import random
print("welcome to the number guessing game")
player_tried = 0
points = 0
number_left = 10

def randomize():
    first_number = random.randint(1,50)
    sec_number = random.randint(1,50)
    numnber = random.randint(first_number,sec_number)
    user_guess(first_number,sec_number,numnber,points,player_tried,number_left)

def user_guess(first_number,sec_number,number,points,player_tried,number_left):
    print(f"The number is between:{first_number} and :{sec_number}")
    user_guess = input("Enter your guess:")
    if user_guess == number:
        print("You are right!")
        points += 1
    elif user_guess != number:
        how_close = number - user_guess
        if how_close < 0:
            print("The number should be smaller")
            
randomize()