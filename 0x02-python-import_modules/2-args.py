#!/usr/bin/python3
import sys
count = len(sys.argv) - 1

if count == 1:
    print("{} argument:".format(count))
elif count == 0:
    print("{} arguments.".format(count))
else:
    print("{} arguments:".format(count))

if count >= 1:
    count = 0
    for arg in sys.argv:
        if count != 0:
            print("{}: {}".format(count, arg))
        count += 1