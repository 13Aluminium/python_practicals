import numpy as np

# create two 2D numpy arrays with random numbers
arr1 = np.random.rand(2, 3)
arr2 = np.random.rand(2, 4)

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# concatenate the two arrays
concatenated = np.concatenate((arr1, arr2), axis=1)

print("Concatenated array:\n", concatenated)

# reshape the concatenated array
reshaped = concatenated.reshape(concatenated.shape[1], concatenated.shape[0])

print("Reshaped array:\n", reshaped)
print("21DCE052")