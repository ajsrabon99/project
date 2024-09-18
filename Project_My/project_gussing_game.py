import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess what it is?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} correctly.")
                print(f"It took you {attempts} attempts to guess the correct number.")
                break
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
if __name__ == "__main__":
    number_guessing_game()

