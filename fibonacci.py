N = 10

a_pp = 1  #a0
a_p = 1   #a1

print(a_pp)
print(a_p)

for i in range(2, N):
    a = a_p + a_pp
    print(a)
    a_pp = a_p
    a_p = a
    
