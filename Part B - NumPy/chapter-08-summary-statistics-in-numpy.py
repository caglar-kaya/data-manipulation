import numpy as np

# 1. Print the min and max values of big_data.
np.random.seed(1)  # seed for reproducibility
big_data = np.random.rand(1000000)

print("Max value:", np.max(big_data))
print("Min value:", np.min(big_data))

# 2. Print the sum of the elements of big_data.
print("Sum:", np.sum(big_data))

# 3. Print the minimum value of each column of x.
np.random.seed(1)  # seed for reproducibility
x = np.random.random((3, 4))

print(x.min(axis = 0))

# 4. Print the maximum value of each row of x.
print(x.max(axis = 1))