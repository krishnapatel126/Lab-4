import math

x_degrees = float(input("Enter x in degrees: "))

x_radians = x_degrees * (math.pi / 180)

sin_x = 0
term = x_radians

tolerance = 1e-10
i = 1

while abs(term) > tolerance:
    sin_x += term
    i += 2
    term = (-1)**((i-1)//2) * (x_radians**i) / math.factorial(i)

print("sin(x) =", sin_x)
