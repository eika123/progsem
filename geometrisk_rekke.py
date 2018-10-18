N = 50

k = 0.5
a = 1     # a0
s = a

for i in range(N):
    a = a*k
    s = s + a

print(s)