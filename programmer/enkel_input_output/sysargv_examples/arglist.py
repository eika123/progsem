import sys

# ------------------------------------------------------------------
# REMEMEMBER! text behind a hashtag (#) is a comment!
# comments are ignored when the code is executed!

# comments help yourself and other programmers 
# read and understand your code!
# ------------------------------------------------------------------

# the purpose of this code snippet is to demonstrate that
# sys.argv is a list. Lets do some exploring
# ------------------------------------------------------------------


# print the name of the program: the first parameter passed into
# the python interpreter
print(sys.argv[0])

# print an empty line
print(' ')


print('all arguments...')
# print all of sys.argv
print(sys.argv)


print(' ')
# print all arguments except name of the program
print(sys.argv[1:])

# you will learn more about the slicing syntax sys.argv[1:] when we
# start learning about lists more thoroughly