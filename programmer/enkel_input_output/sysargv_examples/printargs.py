import sys

# this program prints "hello world!", and reads 2 arguments from the
# command line and prints them to the user

# write a greeting to the terminal
print('hello, world!')


arg1, arg2 = sys.argv[1], sys.argv[2]

print("argument 1: ", arg1)
print("argument 2: ", arg2)


# kjøre-eksempel
"""
(main) PS C:...> python .\printargs.py dust mikkel
hello, world!
argument 1:  dust
argument 2:  mikkel
"""


