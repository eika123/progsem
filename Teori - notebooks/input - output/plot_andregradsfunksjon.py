
from pylab import *
import argparse


parser = argparse.ArgumentParser() # lag et objekt parser som kan lese input fra kommandolinjen

# definer forventede argumenter fra kommandolinjen med key-value pairs
parser.add_argument('--a', type=float)
parser.add_argument('--b', type=float)
parser.add_argument('--c', type=float)

parser.add_argument('--xmin', type=float)
parser.add_argument('--xmax', type=float)

# antall grid-punkter i et intervall med lengde 1
parser.add_argument('--grid_density', type=int, default=100)

# les argumentene fra kommandolinjen
args = parser.parse_args()
a, b, c, xmin, xmax, grid_density = args.a, args.b, args.c, args.xmin, args.xmax, args.grid_density

N = round(abs(xmax - xmin)*grid_density) # antall punkter i gridet

x = linspace(xmin, xmax, N)
y = a*x**2 + b*x + c

plot(x, y)

xlabel('x', fontsize=16); xticks(fontsize=14)
ylabel('y', fontsize=16); yticks(fontsize=14)

title(fr'${a}x^2 + {b}x + {c}$', fontsize=20) # skriv funksjonsuttrykket i tittelen
grid()


# gcf: get current figure 
fig = gcf()
fig.set_size_inches(10, 7)


show()
