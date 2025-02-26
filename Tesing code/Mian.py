import random
import time

# Starting the game
print("Welcome to the number guessing game")

# File for high score

HIGH_SCORE_FILE = "Tesing code\high_score.txt"


# Load high score
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0  # Default high score if the file doesn't exist or is invalid


# Save high score if it's higher
def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
        print(f" New high score: {score}!")


# Number guessing game
def play_game():
    attempts = 10  # Number of attempts per round
    total_score = 0  # Player's score
    rounds_left = 10  # Number of rounds


    print(" Welcome to the Number Guessing Game!")
    print(f" High Score: {load_high_score()}\n")


    while rounds_left > 0:
        rounds_left -= 1
        number = random.randint(1, 50)  # Random number to guess
        print("\n Loading...")
        time.sleep(1.2)
        print(" Number is ready! Try to guess it.")


        total_score += guess_number(number, attempts)


    print(f"\n Game Over! Your final score: {total_score}")
    save_high_score(total_score)


# Guessing function
def guess_number(number, attempts):
    print(f" The number is between 1 and 50. You have {attempts} tries!\n")


    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f" Attempt {attempt}: Your guess? "))
        except ValueError:
            print(" Invalid input! Please enter a number.")
            continue


        if guess == number:
            print(f" Correct! The number was {number}.")
            return attempts - attempt + 1  # Higher score for fewer attempts


        print(" Wrong guess!", "Too high!" if guess > number else " Too low!")
        
        if abs(number - guess) <= 5:
            print(" Very close!")
        elif abs(number - guess) <= 10:
            print(" Getting closer!")


    print(f" Out of attempts! The number was {number}.")
    return 0  # No points if all attempts are used


# Start the game
play_game()



