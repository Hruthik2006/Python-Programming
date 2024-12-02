# Developing HangMan game

import random

WORDS = ["python", "java", "kotlin", "javascript", "hangman", "programming", "development"]

def choose_word():
    return random.choice (WORDS)

def display_word (word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else for letter in word])

def play_hangman():
    word choose_word()
    guessed_letters = set()
    attempts = 6
    print("Welcome to Hangman!")
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts)")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        guess input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print (f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess.")
            attempts = 1
            
        if attempts == 0:
            print(f"Game over! The word was: {word}")
    
while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break

