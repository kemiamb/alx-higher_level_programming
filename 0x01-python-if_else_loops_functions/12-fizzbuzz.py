#!/usr/bin/python3
def fizzbuzz():
    i = 1
    for i in range(2, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f" FizzBuzz", end='')
        elif i % 3 == 0:
            print(f" Fizz", end='')
        elif i % 5 == 0:
            print(f" Buzz", end='')
        else:
            print(" " + "{}".format(i), sep=' ', end='')
    print(" ", end='')
