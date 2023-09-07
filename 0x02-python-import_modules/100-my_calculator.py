#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic calculation."""
    from calculator_1 import add, sub, mul, div
    import sys as call

    if len(call.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        call.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if call.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        call.exit(1)

    a = int(call.argv[1])
    b = int(call.argv[3])
    print("{0} {1} {2} = {3}".format(a, call.argv[2], b, ops[call.argv[2]](a, b)))
