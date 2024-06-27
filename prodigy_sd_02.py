import random

def guessing_game():
    number_to_guess = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
