import numpy as np

# 1. Create an integer array with 100 ones.
print(np.ones(100, dtype='int'))

# 2. Create a (4, 3) float array filled with zeros.
print(np.zeros((4, 3)))

# 3. Create a (5, 2) array filled with 6.28.
print(np.full((5,2), 6.28))

# 4. Create an array filled with a linear sequence, started at 0, ending at 30, stepping by 3.
print(np.arange(0, 33, 3))

# 5. Create an array of 9 evenly spaced values between 0 and 64 inclusive.
print(np.linspace(0, 64, 9))

# 6. Create a (5, 2) array of uniformaly distributed random values between 0 and 1.
print(np.random.random((5,2)))

# 7. Create an array of 10 random integers in the interval [0, 5].
print(np.random.randint(0, 6, 10))

# 8. Create a (4, 4) identity matrix.
print(np.eye(4))