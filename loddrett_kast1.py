
h0 = 1.5    ## m/s          (starthøyde)
g = -9.81   # m/s**2        (gravitasjonskonstant)
t = 2       # s             (tidspunkt)
v0 = 15     # m/s           (utgangshastighet)


# Beregn høyde over bakken etter t sekunder
s = h0 + v0*t + 0.5*g*t**2

print(s)

"""kjøreeksempel fra spyder
runfile('C:/Users/..../loddrett_kast1.py', wdir='C:/Users..../GitHub/progsem')
11.879999999999999
"""