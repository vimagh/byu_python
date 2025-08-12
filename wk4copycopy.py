import random

secret_word = "Jesus"
word_length = len(secret_word)
guesses = 0

print("Welcome to the Word Game!")
print("Try to guess the secret word.")
print("Word length:", "_ " * word_length)

while True:
    guess = input("Enter your guess: ")
    
    if len(guess) != word_length:
        print(f"Your guess must be {word_length} letters long.")
        continue
    
    guesses += 1
    
    if guess == secret_word:
        print(f"Congratulations! You guessed the word in {guesses} tries.")
        break
    
    
    hint = ""
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "
    
    print("Hint:", hint.strip())