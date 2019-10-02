import numpy as np
ln = np.log

"""
Dette programmet løser en
differensiallikning for eksponentsiell/
logistisk vekst
            y' = k(y)*y
"""

p = [5]     # populasjon ved start
k_ = 0.2   # vekstparameter
T = 70      # simulasjonstid
B = 150

dt = 1E-3   # tidssteg
t = [0]     # start ved t=0
n = 0       # tellevariabel


def k1(y):
    return (B - y)/y

def k2(y, a=0.25):
    return a*(B - y)/B

while t[n] < T:

    k = k2(p[n], k_)
    dP = k*p[n]*dt

    p += [p[n] + dP]
    t += [t[n] + dt]

    n += 1

import pylab as pl

pl.plot(t, p)
pl.xlabel('tid [år]')
pl.ylabel('Antall individer')
pl.title('populasjonsutvikling')
pl.show()
