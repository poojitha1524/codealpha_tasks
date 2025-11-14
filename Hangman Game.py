import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "computer", "developer", "programming"]
    
    # Randomly select a word
    word_to_guess = random.choice(words)
    
    # Initialize the game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_display = ['_'] * len(word_to_guess)
    
    # Start the game
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        print("Word: " + " ".join(word_display))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has been guessed already
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            # Update the word display
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    word_display[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the word is completely guessed
        if '_' not in word_display:
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    
    # If the player has run out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word_to_guess}")

# Run the game
if __name__ == "__main__":
    hangman()
