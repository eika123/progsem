N = 10
g = -9.81   # m/s**2      (gravitasjonskonstant)
v0 = 10     # m/s         (utgangshastighet)
h0 = 1      # m           (utgangsposisjon
            #             høyde over bakken)

# høyden over bakken beregnes for tider i
# intervallet [t0, T]
T = 2.04
t0 = 0

print("     %s                   %s" %\
                        ('time', 'height'))
print('----------------------------------')
for n in range(N + 1):
    dt = T/N
    t = t0 + n*dt
    # Beregn høyde over bakken med formel
    s = h0 + v0*t + 0.5*g*t**2
    print("%10.4f         %15.8f" % (t, s))
