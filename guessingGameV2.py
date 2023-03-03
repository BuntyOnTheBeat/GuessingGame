import random

highest = 10
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}:".format(highest))

guess = int(input())

if guess == answer:
    print("Well done, first try")

while guess != answer:
    if guess < answer:
        print("You guessed to low")
        guess = int(input())
    if guess > answer:
        print("You guessed to high")
        guess = int(input())
    if guess == answer:
        print("You guessed correctly")
        break
