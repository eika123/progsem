from pylab import *
import sys

#programmet plotter grafen til en funksjon a*x**2 + b*x + c

# les inn nødvendige parametere for å representere funksjonen
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# les inn nødvendige parametere for xmin og xmax for plottet.
# verdimengden behøver vi ikke bekymre oss om for plotting
xmin = float(sys.argv[4])
xmax = float(sys.argv[5])


N = round(abs(xmax - xmin)*100) # hundre punkter i et intervall med bredde 1

x = linspace(xmin, xmax, N)
y = a*x**2 + b*x + c

plot(x, y)

xlabel('x')
ylabel('y')
title(fr'${a}x^2 + {b}x + {c}$') # skriv funksjonsuttrykket i tittelen
grid()

show()

