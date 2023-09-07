#!/usr/bin/python3

if __name__ == "__main__":
    """Print all arguments added."""
    import sys

    count = 0
    len = len(sys.argv)

    for i in range(1, len):
        count += int(sys.argv[i])
    print("{0}".format(count))
