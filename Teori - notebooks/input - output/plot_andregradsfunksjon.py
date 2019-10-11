
from pylab import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--a', type=float)
parser.add_argument('--b', type=float)
parser.add_argument('--c', type=float)

parser.add_argument('--xmin', type=float)
parser.add_argument('--xmax', type=float)

args = parser.parse_args()
a, b, c, xmin, xmax = args.a, args.b, args.c, args.xmin, args.xmax

N = round(abs(xmax - xmin)*100) # hundre punkter i et intervall med bredde 1

x = linspace(xmin, xmax, N)
y = a*x**2 + b*x + c

plot(x, y)

xlabel('x')
ylabel('y')
title(fr'${a}x^2 + {b}x + {c}$') # skriv funksjonsuttrykket i tittelen
grid()

show()