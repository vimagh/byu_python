# - Added a limited number of 6 guesses to increase challenge.
# - Randomly selects a secret word from a predefined list.
# - Provides extra hints: correct letters in correct place vs. correct letters in wrong place.

import random

# List of possible secret words (all 5 letters)
word_list = ["Jesus", "Faith", "Grace", "Mercy", "Cross", "Light", "Truth", "Peace", "Hope", "Glory"]
secret_word = random.choice(word_list).lower()
word_length = len(secret_word)
guesses = 0
max_guesses = 6

print("🔤 Welcome to the Word Puzzle Challenge!")
print("You have 6 tries to guess the 5-letter secret word.")
print("For each guess, you'll get hints:")
print("- UPPERCASE letter: correct position")
print("- lowercase letter: correct letter, wrong position")
print("- _ : letter not in the word")
print("Let's begin!")
print("Word length:", "_ " * word_length)

while guesses < max_guesses:
    guess = input(f"\nEnter guess {guesses + 1}/{max_guesses}: ").lower()

    if len(guess) != word_length:
        print(f"⚠️ Your guess must be {word_length} letters long.")
        continue

    guesses += 1

    if guess == secret_word:
        print(f"🎉 Congratulations! You guessed the word '{secret_word.upper()}' in {guesses} tries.")
        break

    # Build hint
    hint = ""
    correct_pos = 0
    correct_letter_wrong_pos = 0

    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
            correct_pos += 1
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
            correct_letter_wrong_pos += 1
        else:
            hint += "_ "

    print("Hint: ", hint.strip())
    print(f"🔎 Letters in correct place: {correct_pos}, correct letters wrong place: {correct_letter_wrong_pos}")

else:
    print(f"\n❌ Game Over! You've used all {max_guesses} guesses.")
    print(f"The secret word was: {secret_word.upper()}")