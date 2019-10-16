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


N = ceil(abs(xmax - xmin)*100) # hundre punkter i et intervall med bredde 1

# Lag et intervall (array) med flyttall fra xmin til xmax med N punkter
x = linspace(xmin, xmax, N)

# beregn en y-verdi for hvert av flyttallene i arrayet x
y = a*x**2 + b*x + c

plot(x, y)

#pynt på grafen
xlabel('x', fontsize='24')
xticks(fontsize='16', rotation=40)
ylabel('y', fontsize='24')
yticks(fontsize='16')
title(fr'${a}x^2 + {b}x + {c}$', fontsize='32') # skriv funksjonsuttrykket i tittelen
grid()

# gcf: get current figure 
fig = gcf()
fig.set_size_inches(10, 7)


show()

