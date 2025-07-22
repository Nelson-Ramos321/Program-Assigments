# Guessing game - nelson ramos
import random
def generate_random_number():
    return random.randint(1, 100)
def get_user_guess():
    number_to_guess = generate_random_number()
    while True:
        try:
            get_user_guesser = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if get_user_guesser == number_to_guess:
            print("Congratulations! You guessed the number!")
            break
        elif get_user_guesser < number_to_guess:
            print("Too low! Try again.")
            user_exit = input("Enter 'exit' to quit or continue guessing")
            if user_exit.lower() == 'exit':
                print("exiting game. Goodbye.")
                break   
            else:
                continue
        elif get_user_guesser > number_to_guess:
            print("Too high! Try again.")
            user_exit = input("Enter 'exit' to quit or continue guessing.")
            if user_exit.lower() == 'exit':
                print("exiting game. Goodbye.")
                break   
            else:
                continue
        else:
            print("Wrong guess, try again!")
            user_exit = input("Enter 'exit' to quit")
            if user_exit.lower() == 'exit':
                print("exiting game. Goodbye.")
                break   
            else:
                continue
def play_guessing_game():
    while True:
        print("Welcome to the Guessing Game!")
        get_user_guess()
        print("Thanks for playing!")
        break
def game_loop():
    play_guessing_game()
game_loop()

