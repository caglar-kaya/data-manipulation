import numpy as np

# 1. Add 2 to every element in x, subtract 2 from every element in x, multiply every element in x with 3.
x = np.arange(9)

print("Add 2:", x + 2)
print("Subtract 2:", x - 2)
print("Multiply 3:", x * 3)

# 2. Negate every element in x, cube every element in x, calcualte the remainder if you divide every element by 4 in x.
print("Negation:", -x)
print("Cubed:", x ** 3)
print("Mod 4:", x % 4)

# 3. Print the absolute value for every element in x2.
x2 = np.arange(-4, 5)

print(np.abs(x2))

# 4. Print the results sine, cosine, and tangent on the elements of theta.
theta = np.linspace(0, np.pi, 3)

print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

# 5. Print the results arcsine, arccosine, and arctangent on the elements of x3.
x3 = [-1, 0, 1]

print("arcsin(x3) = ", np.arcsin(x3))
print("arccos(x3) = ", np.arccos(x3))
print("arctan(x3) = ", np.arctan(x3))

# 6. Print the results of e^x4, 2^x4, and 5^x4.
x4 = [1, 2, 3]

print("e^x4 =", np.exp(x4))
print("2^x4 =", np.exp2(x4))
print("5^x4 =", np.power(5, x4))

# 7. Print the results of ln, log 2, and log 10 on x5.
x5 = [1, 2, 4, 10]

print("ln(x5) =", np.log(x5))
print("log2(x5) =", np.log2(x5))
print("log10(x5) =", np.log10(x5))

# 8. Print the results of exp(z) - 1 and expm1(z) to see that expm1 is more precise.
z = [0, 0.0000000001, 0.000000001, 0.00000001]

print("(e^z)-1 =", np.exp(z) - 1)
print("(e^z)-1 =", np.expm1(z))