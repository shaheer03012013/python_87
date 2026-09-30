import random
playing = True
sec_num = random.randint(1,9)
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 and 9. Can you guess it?")
while playing:
    guess = int(input("Enter a number: "))
    if guess == sec_num:
        print("Congratulations! You guessed the number!")
        playing = False
    else:
        print("Try again!")