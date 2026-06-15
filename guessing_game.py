import random
number = random.randint(1, 10)
guesses = 0

while True:
    print(f"You are about to do attempt number {guesses + 1}.")
    while True:
        try:
            guess = int(input("Guess: "))
            guesses += 1
            break
        except ValueError:
            print("Please input a number between 1 and 10.")
    if guess == number:
        print("You win!")
        break
    else:
        if guesses < 3:
            print("Try again!")
            if guess < number:
                print("Your guess was too small.")
            else:
                print("Your guess was too large.")
        else:
            print("You lose!")
            break