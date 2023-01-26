import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# set the number of guesses allowed
guesses = 5

# start the game
print("Welcome to the guessing game! You have", guesses, "guesses to guess a number between 1 and 100.")

# loop for the number of guesses
for i in range(guesses):
    # get player's guess
    guess = int(input("Make a guess: "))

    # check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", i + 1, "guesses!")
        break
    # check if the guess is too high or too low
    elif guess < number:
        print("Too low. You have", guesses - (i + 1), "guesses left.")
    else:
        print("Too high. You have", guesses - (i + 1), "guesses left.")

# if the player runs out of guesses
if guess != number:
    print("Sorry, you ran out of guesses. The number was", number)

