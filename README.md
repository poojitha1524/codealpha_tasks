# codealpha_tasks
import random

# Step 1: Predefined list of words
words = ["python", "banana", "hangman", "computer", "guitar"]

# Step 2: Randomly choose a word
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

# Step 3: Display intro message
print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {attempts_left} incorrect guesses allowed.\n")

# Step 4: Game loop
while attempts_left > 0:
    # Display current progress
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())

    # Check if player has guessed all letters
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break

    # Get player input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print("✅ Good guess!\n")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

# Step 5: Game over
if attempts_left == 0:
    print("💀 Game over! The word was:", word_to_guess)
