import random
print("welcome to the number guessing game")
player_tried = 0
points = 0
number_left = 10
end = None
def randomize():
    global first_number,sec_number,numnber
    first_number = random.randint(1,25)
    sec_number = random.randint(25,50)
    numnber = random.randint(first_number,sec_number)
def user_guess():
    while player_tried < 1:
        if number_left <= 0:
            break
        elif number_left > 0:
            print(numnber)
            print(f"The number is between:{first_number} and :{sec_number}")
            user_guess = input("enter your guess: ")
            int(user_guess)
            if user_guess == numnber:
                print("You are right!")
                points += 1
                player_tried = player_tried + 1
                randomize()
            elif user_guess != numnber:
                how_close = numnber - user_guess
                if how_close < 0:
                    print("The number should be smaller")
                elif how_close > 0:
                    print("The number should be bigger")
randomize()

            



