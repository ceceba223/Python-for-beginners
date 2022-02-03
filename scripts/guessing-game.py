from random import randint

while True:
    guesses = 1
    randnum = randint(1, 10)
    print("I made up a number between 1 and 10. Guess it!")

    while guesses <= 5:
        guess = int(input("Guess: "))

        if guess == randnum:
            print(f"Yes! You guessed the number in {guesses} tries")
            break
        elif guess < randnum:
            print("Your guess is too low")
        elif guess > randnum:
            print("Your guess is too high")
        guesses += 1 
    print("You used all your guesses! Try again:")
