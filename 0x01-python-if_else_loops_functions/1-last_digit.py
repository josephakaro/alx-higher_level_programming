#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str_rep = repr(number)
n = 10

if number < 0:
    last = ((-1 * number) % n) * -1
else:
    last = number % n

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and not 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
