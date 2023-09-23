import numpy as np

# 1. Create a list containing the values 1, 3, and 5.
list_1 = [1, 3, 5]
print(list_1)

# 2. Create a list containing the values from 0 to 9 using the range function and assign it to L.
L = list(range(10))
print(L)

# 3. Print the first element from L.
print(L[0])

# 4. Create an array containing the values [5, 4, 3, 2, 1] and store is in A.
A = np.array([5, 4, 3, 2, 1])
print(A)

# 5. Print the datatype of array A.
print(A.dtype)

# 6. What is the expected datatype of this array? Why? Enter the expected datatype between quotation marks
A2 = np.array([3.14, 4, 2, 3])
print(A2.dtype == 'float64')

# 7. For practice reasons, create a multidimesional array from a multidimesional list.
multidimesional_array = np.array([[1, 2], [3, 4], [5, 6]])
print(multidimesional_array)