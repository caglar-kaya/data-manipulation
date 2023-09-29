import numpy as np

# For the following tasks 1, 2, and 3, refer to the array created below. Run this code to get started.

np.random.seed(0)  # seed for reproducibility

x = np.random.randint(10, size=(3, 3))  # Two-dimensional array
print(x)

# 1. Print the ndim, shape, and size attributes of x. The print code has already been created for you.
print("x ndim: ", x.ndim)
print("x shape:", x.shape)
print("x size: ", x.size)

# 2. Print the dtype of x.
print("dtype:", x.dtype)

# 3. Print the itemsize and nbytes of x.
print("itemsize:", x.itemsize, "bytes")
print("nbytes:", x.nbytes, "bytes")