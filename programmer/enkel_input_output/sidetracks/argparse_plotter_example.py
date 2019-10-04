from pylab import *
import argparse


parser = argparse.ArgumentParser(description='Plot a function')

parser.add_argument('expressions', metavar='N', type=str, nargs='+',
                    help='an expression for the function')

parser.add_argument('--sameplot', action='store_true',
                    help='give this option if you want to draw '\
                        +'the graphs in the same plot')

args = parser.parse_args()
expressions = args.expressions



# safety: forbid python and bash code
forbidden_words = [
    'if',
    'else',
    'elif',
    'and',
    'or',
    'with',
    'yield',
    'while',
    'for',
    'continue',
    'finally',
    'class',
    'is',
    'import',
    'global',
    'eval',
    'dir',
    '[',
    ']',
    '{',
    '}',
    'def',
    'del',
    'return',
    'lambda',
    'assert',
    'False',
    'True',
    'os',
    'sys',
    'rm',
    'rmdir',
    '-f',
    'try',
    'except',
    'break',
    'pass',
    'raise',
    ';',
    ':',
    'list',
    'dict',
    'print'
]

# check for python keywords and code in input
for word in forbidden_words:
    for expression in expressions:
        if word in expression:
            feedback_message = "got a false input \n"
            feedback_message += "Python executable code is \n" +\
                                    "unacceptable input\n"
            raise ValueError(feedback_message)

#TODO: use regular expressions to change python math notation
# into latex notation for pretty labels
x = linspace(-10, 10, 1001)
ys = []
y_labels = []
for expression in expressions:
    y_label = expression
    expression = eval(expression)
    ys.append(expression)
    y_labels.append(y_label)

for y, label in zip(ys, y_labels):

    plot(x, y)
    grid()
    print(label)

    if not args.sameplot:
        ylabel(label)
        show()
        figure()
    else:
        ylabel('y')
        legend(y_labels)
        show()