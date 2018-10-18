a = 1  # try changing this - first element in progression
d = 1   # difference between terms in sum

s = 0
N = 100

for i in range(N):
    s = s + a
    a = a + d

print(s)

