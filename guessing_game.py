import random

def main():
    while True:
        counter = 0
        number = random.randint(1, 10)
        while counter < 3:
            myguess, counter = guess(counter)
            counter = evaluate(myguess, number, counter)
        player_choice = again()
        if player_choice == 1:
            continue
        elif player_choice == 2:
            return

def guess(counter):
    print(f"This is attempt number {counter + 1}")
    while True:
        try:
            myguess = int(input("Guess: "))
            if myguess < 1 or myguess > 10:
                print("Please input a number between 1 and 10.")
            else:
                counter += 1
                return myguess, counter
        except ValueError:
            print("Please input a number between 1 and 10.")

def evaluate(myguess, number, counter):
    if myguess == number:
        print("You win!")
        counter = 3
    elif counter == 3:
        print("You lose!")
    else:
        if myguess < number:
            print("Your guess is too small. Try again!")
            return counter
        else:
            print("Your guess is too high. Try again!")
            return counter
    input("Press any button to continue.")
    return counter

def again():
    while True:
        choice = input("Do you want to play again? 1 = yes, 2 = no: ")
        if choice in ("1", "2"):
            player_choice = int(choice)
            break
        else:
            print("Please choose either 1 or 2.")
    return player_choice



main()
