import random

print("Welcome to the Simple Coin Toss Game!")

while True:
    guess = input("Guess heads or tails: ").lower()

    while guess not in ["heads", "tails"]:
        print("Invalid input!")
        guess = input("Guess heads or tails: ").lower()

    toss = random.choice(["heads", "tails"])

    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    play = input("Do you want to play again? (yes/no): ").lower()

    if play == "no":
        print("Thanks for playing!")
        break