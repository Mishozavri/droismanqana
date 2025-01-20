import random

def select_word():
    words = ["python", "hangman", "programming", "cheating", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_attempts(remaining_attempts, incorrect_guesses):
    print(f"Remaining attempts: {remaining_attempts}")
    print("Incorrect guesses:", ", ".join(incorrect_guesses) if incorrect_guesses else "None")

def get_user_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        print("Invalid or repeated input. Try again.")
def update_game_state(word, guess, guessed_letters, incorrect_guesses, remaining_attempts):
    guessed_letters.append(guess)
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry! '{guess}' is not in the word.")
        incorrect_guesses.append(guess)
        remaining_attempts -= 1
    return guessed_letters, incorrect_guesses, remaining_attempts

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def check_game_over(remaining_attempts):
    return remaining_attempts <= 0
def main():
    word = select_word()
    guessed_letters = []
    incorrect_guesses = []
    remaining_attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while not game_over:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        display_attempts(remaining_attempts, incorrect_guesses)

        guess = get_user_guess(guessed_letters)
        guessed_letters, incorrect_guesses, remaining_attempts = update_game_state(word, guess, guessed_letters,
                                                                                   incorrect_guesses,
                                                                                   remaining_attempts)

        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            game_over = True
        elif check_game_over(remaining_attempts):
            print(f"\nGame Over! The word was: {word}")
            game_over = True

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        main()


if __name__ == "__main__":
    main()