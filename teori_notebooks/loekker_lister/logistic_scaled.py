import sys
from pylab import *

# legg argumenter fra kommandolinje i liste,
# gjør om til floats og pakk ut
dt, T, U_0, R = [float(arg) for arg in sys.argv[1:5]]

# ekvivalent kode:
dt = float(sys.argv[1])
T = float(sys.argv[2])
U_0 = float(sys.argv[3])
R = float(sys.argv[4])


N = int(ceil(T/dt))
t = linspace(0, T, N + 1)

y = U_0/R         # definer y0
y_verdier = [y]
for i in range(1, N + 1):
    y_neste = y + dt*y*(1 - y)
    y = y_neste
    y_verdier.append(y)

y_verdier = array(y_verdier)

plot(t, y_verdier)
fig = gcf()
fig.set_size_inches(8,5)
xlabel(r'$\tau$', fontsize=20)
ylabel(r'$v$', fontsize=20)
xticks(fontsize=16)
yticks(fontsize=16)
title('Logistisk vekst', fontsize=26)
grid()
show()

