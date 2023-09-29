import numpy as np

# 1. Create a boolean mask of x for values less than or equal to 2.
x = np.arange(-3, 5)
print(x)

mask = x <= 2
print(mask)

# 2. Create a boolean mask of x for values equal to -1.
mask2 = x == -1
print(mask2)

# 3. Create a boolean mask of x for all positive values.
mask3 = x > 0
print(mask3)

# 4. Create a boolean mask of x for all even values.
mask4 = x % 2 == 0
print(mask4)

# 5. Create a boolean mask 'greater' of x2 for values greater than 4. Create an array of x2 for values greater than four using a masking operation.
np.random.seed(1)  # seed for reproducibility
x2 = np.random.randint(10, size=(3, 4))

greater = x2 > 4

print(x2[greater])

# 6. Create a boolean mask 'odd' of x2 for all odd values. Create an array of x2 for those odd values using a masking operation.
odd = x2 % 2 != 0

print(x2[odd])

# 7. Create an array of x2 containing all values that are greater than 4 and are not odd using boolean operators and a masking operation.
mask5 = (x2 > 4) & (x2 % 2 == 0)

print(x2[mask5])