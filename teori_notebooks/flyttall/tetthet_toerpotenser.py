from pylab import *
N = 10
x = arange(0, N, 1)
def f(n):
    return 1/(2**n)

y = f(x)
scatter(x, y)
xlabel(r'$n$ - eksponent', fontsize=16)
xticks(x, fontsize=14)
ylabel(r'$2^{-n}$', fontsize=16)
yticks([2**(-i) for i in range(5)] + [0], fontsize=14)
grid()
title(r'Tetthet av $\frac{1}{2^n}$ på tallinja', fontsize=20)
fig = gcf()
fig.set_size_inches(9, 9)
savefig('power_two_density.png')
