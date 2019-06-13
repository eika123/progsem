# <codecell>
number_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

for number in number_list:
    print(number, ",   ", number*10)

print("----------------------------------------")

# <codecell>
x_list = [0.0, 0.1, 0.2, 0.3, 0.4]
y_list = [0.0, 0.4, 0.8, 1.2, 1.6]

# naive approach?
for i in range(len(x_list)):
    print(x_list[i], y_list[i])

print("----------------------------------------")

for i in range(10, 100 + 1, 5):
    print(i)

# zip makes iterator that returns
for x, y in zip(x_list,y_list):
    print(x, y)

print("----------------------------------------")
print("\n \n \n")


# list comprehensions

# liste [0, 1, 2, 3, 4]
i_list = [i for i in range(5)]
print(i_list)

# liste [1, 2, 3, 4, 5]
i_list = [i + 1 for i in range(5)]
print(i_list)
print("\n \n \n")

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



from pylab import plot as plt

plt(time_values, h_values)

pylab.show()
