import random

def number_guessing_game():
    print(" Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get user guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check guess
            if guess < secret_number:
                print(" Too low! Try higher.")
            elif guess > secret_number:
                print(" Too high! Try lower.")
            else:
                print(f" Congratulations! You guessed it in {attempts} attempts!")
                break
            
            # Show remaining attempts
            print(f"Attempts left: {max_attempts - attempts}")
            
        except ValueError:
            print(" Please enter a valid number!")
    
    # If player runs out of attempts
    if attempts >= max_attempts and guess != secret_number:
        print(f"\n Game Over! The number was {secret_number}")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
