import numpy as np

# For the following six tasks, refer to the arrays created below. Run this code to get started.

np.random.seed(1)  # seed for reproducibility

x1 = np.random.randint(10, size=9)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 3))  # Two-dimensional array

print(x1)
print(x2)

# 1. Print the first element of x1.
print(x1[0])

# 2. Print the fifth element of x1.
print(x1[4])

# 3. Print the second to last element of x1 using negative indicies.
print(x1[-2])

# 4. Print the element at position (0,2) of x2.
print(x2[0, 2])

# 5. Print the second element of the last row of x2 using positive and negative indicies.
print(x2[2, -2])

# 6. Assign a value of 25 to the first element of the last row of x2.
x2[2, 0] = 25
print(x2)