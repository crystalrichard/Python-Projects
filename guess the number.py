import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a random number between 1 to {x}: "))
        if guess > random_number:
            print("Sorry your guess is too high :( ")
        elif guess < random_number:
            print("Sorry your guess is too low :( ")
    print("Yay congrats you guessed it right!!!!!!!!!!!!!!!!!!!")
guess(10)






