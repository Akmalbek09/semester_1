import random
num = random.randint(0,100)
for x in range(0,100):
    a = int(input("Type your guess: "))
    if a > num:
        print("The number is lower")
    elif a < num:
        print("The number is higher")
    elif a == num:
        print("You win")
        break
    else:
        print("You lost")
