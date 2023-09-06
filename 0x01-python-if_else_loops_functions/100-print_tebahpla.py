#!/usr/bin/python3

count = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - count)), end="")
    count = 32 if count == 0 else 0
