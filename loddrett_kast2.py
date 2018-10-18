N = 10
g = -9.81   # m/s**2      (gravitasjonskonstant)
v0 = 10     # m/s         (utgangshastighet)
T = 2.04
t0 = 0

print("%s            %s" % ('time', 'height'))
print('--------------------------')
for n in range(N + 1):
    dt = T/N
    t = t0 + n*dt 
    # Beregn høyde over bakken/utgangsposisjon med formel
    s = v0*t + 0.5*g*t**2
    print("%.4f         %.8f" % (t, s))