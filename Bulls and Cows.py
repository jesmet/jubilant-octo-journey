import random

# Generate random 4-digit number with unique digits 1-9
digits = list('123456789')
random.shuffle(digits)
secret = digits[:4]

print("Welcome to Bulls and Cows!")
print("Guess the 4-digit number (digits 1-9, no duplicates).")

while True:
    guess = input("Enter your guess: ").strip()

    # Validate guess
    if len(guess) != 4:
        print("Your guess must be exactly 4 digits.")
        continue
    if not guess.isdigit():
        print("Your guess must contain only digits.")
        continue
    if '0' in guess:
        print("Digits must be from 1 to 9 (no zero).")
        continue
    if len(set(guess)) != 4:
        print("Digits must not repeat.")
        continue

    # Calculate bulls and cows
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    if bulls == 4:
        print("Congratulations! You guessed it right:", ''.join(secret))
        break
    else:
        print(f"{bulls} Bulls, {cows} Cows")
