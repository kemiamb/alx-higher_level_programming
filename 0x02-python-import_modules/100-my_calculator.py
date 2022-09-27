#!/usr/bin/python3
from ast import operator


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]

    if count != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif (operator != '+' or operator != '-' or operator != '*' or operator != '/'):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        if operator == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif operator == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif operator == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif operator == '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))