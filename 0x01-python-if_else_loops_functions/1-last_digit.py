#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str_rep = repr(number)

if number < 0:
    last_digit = ((-1 * number) % 10) * -1
else:
    last_digit = number % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and not 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")