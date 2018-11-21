avogadro_konstant = 6.28E23   # avogadros tall

M_oksygen = 16
M_karbon = 12
M = M_karbon + 2*M_oksygen    # molar masse (g/mol)

m = 15000                     # masse (g)

n = m/M                       # antall mol

antall_molekyler = n*avogadro_konstant

print("antall mol: ", n)
print("antall molekyler: ", antall_molekyler)
