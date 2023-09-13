#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    sum = 0
    num = 0
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000}
    for n in reversed(roman_string):
        num = digit[n]
        sum += num if sum < num * 5 else -num
    return sum
