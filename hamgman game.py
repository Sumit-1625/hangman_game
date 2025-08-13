import random

HANGMAN_PICS = [
    '''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='''
]

def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            return [word.strip().lower() for word in file.readlines()]
    except FileNotFoundError:
        return ["apple", "banana", "tiger", "chair", "table"]

def get_random_word(words):
    return random.choice(words)

def display_game_state(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    display = ""
    for letter in secret_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word: ", display.strip())
    print("Missed letters: ", " ".join(missed_letters))

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Enter only one letter.")
        elif not guess.isalpha():
            print("Only letters are allowed.")
        elif guess in already_guessed:
            print("You already guessed that letter.")
        else:
            return guess

def play_game():
    words = load_words()
    secret_word = get_random_word(words)
    missed_letters = []
    correct_letters = []
    game_over = False

    while not game_over:
        display_game_state(missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)
            if all(letter in correct_letters for letter in secret_word):
                print(f"\nYes! The secret word was '{secret_word}'! You win!")
                game_over = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(missed_letters, correct_letters, secret_word)
                print(f"\nYou’ve run out of guesses! The word was '{secret_word}'.")
                game_over = True

    if input("\nPlay again? (y/n): ").lower().startswith("y"):
        play_game()

if __name__ == "__main__":
    print("=== Welcome to Hangman! ===")
    play_game()
