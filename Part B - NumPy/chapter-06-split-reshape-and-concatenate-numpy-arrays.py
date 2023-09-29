import numpy as np

# 1. Create a range from 1 to 16 and reshape it into a (2, 8) array.
print(np.arange(1, 17).reshape(2, 8))

# 2. Reshape x1 into a 1 dimensional column using slice notation and np.newaxis.
np.random.seed(1)  # seed for reproducibility
x1 = np.random.randint(10, size=9)  # One-dimensional array

print(x1[:, np.newaxis])

# 3. Concatenate arrays x and y.
x = np.array([2, 4, 6])
y = np.array([8, 10, 12])

print(np.concatenate([x, y]))

# 4. Concatenate arrays x, y, and z.
z = [99, 99, 99]

print(np.concatenate([x, y, z]))

# 5. Concatenate array with itself along the second axis.
array = np.array([[5, 4, 1],
                 [4, 5, 6]])

print(np.concatenate([array, array], axis=1))

# 6. Concatenate x and array using the vstack function.
print(np.vstack([x, array]))

# 7. Split x2 on element 4 and element 7.
x2 = [1, 2, 3, 99, 99, 3, 2, 1]

print(np.split(x2, [3, 6]))

# 8. Split array2 on row 3.
array2 = np.arange(25).reshape((5, 5))

print(np.vsplit(array2, [2]))

# 9. Split array2 on column 4.
print(np.hsplit(array2, [3]))