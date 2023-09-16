from art import logo
import random
    
answer = random.randint(1,100)
win_flag = 0

def check_num(guess):
    global answer, win_flag
    if guess < 1 or guess > 100:
        print("Please input a number between 1 to 100. Chance deducted.")
    elif answer < guess:
        print("Too high.")
    elif answer > guess:
        print("Too low.")
    elif answer == guess:
        win_flag += 1

print(logo)
print(
    """
Welcome to the Number Guessing Game!
I am thinking of a number between 1 to 100."""
)
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempt = 10
elif difficulty == 'hard':
    attempt = 5
else:
    print("You did not choose correct difficulty. Please restart the game.")
    exit()

while attempt > 0 and win_flag == 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_num(guess=guess)
    if win_flag == 0:
        attempt = attempt - 1
        print("Guess again.")
    else:
        print("Correct! You guess the correct number.")
        exit()
print(f"You have {attempt} attempt left. The answer is {answer}. Good luck next time!")
