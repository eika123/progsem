# list-comprehension to generate t-values
from math import sqrt
h0, v0, g = 1, 10, -10

# Calculate time T when ball reaches ground
a, b, c = 0.5*g, v0, h0
time_stop = (-b - sqrt(b**2 - 4*a*c))/(2*a)

# generate time values [0, .... T]
time_values = [i/15*time_stop for i in range(15 + 1)]
h_values = []


print("--------------------------------")
print("loddrett kast: høyde over bakken")
print("--------------------------------")
print("  h = h0 + v0*t + 0.5*g*t**2    ")
print("--------------------------------")
print(f" h0 = {h0},   v0 = {v0},   g = {g} ")
print("--------------------------------")
print(" tid                   høyde   ")
print("--------------------------------")
for t in time_values:
    h = h0 + v0*t + 0.5*g*t**2
    h_values += [h]
    print(f"{t:5.2f},          {h:14.5f}")
print("--------------------------------")



import pylab as pl

pl.plot(time_values, h_values)
pl.xlabel("tid [s]")
pl.ylabel("høyde over bakken [m]")
pl.title("loddrett kast")


pl.show()
