sigma = 5.6704E-8   # Stefan-Boltzmanns konstant
o = sigma           # omskrivning
T = 250 + 293.15    # temperatur (K)

eps = 0.68          # emmisivitet
area = 1.9          # m^2

phi = eps*o*T**4

effekt = phi*area


print("Effekt: ", effekt/1000, " kiloWatt")
