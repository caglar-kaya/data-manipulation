import numpy as np

# For the following seven tasks, refer to the arrays created below. Run this code to get started.

np.random.seed(1)  # seed for reproducibility

x1 = np.random.randint(10, size=9)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 3))  # Two-dimensional array

print(x1)
print(x2)

# 1. Create a slice containing the last 5 elements of x1.
print(x1[-5:])

# 2. Create a slice containing every third element starting at the second element of x1.
print(x1[1::3])

# 3. Create a slice where x1 has been reversed.
print(x1[::-1])

# 4. Create a slice containing the first two rows and first column of x2.
print(x2[:2, :1])

# 5. Create a slice where the rows have been reversed for x2.
print(x2[::-1, :])

# 6. Print the first column of x2.
print(x2[:, 0])

# 7. Print the first row of x2.
print(x2[0, :])
