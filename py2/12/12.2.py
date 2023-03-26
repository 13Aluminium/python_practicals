import pandas as pd
import numpy as np

# create a list of random numbers
num_list = [np.random.randint(1, 10) for i in range(10)]

# create a Pandas series from the list
num_series = pd.Series(num_list)

# find the mean
mean = num_series.mean()

# find the median
median = num_series.median()

# find the mode
mode = num_series.mode().values

# find the range
range_val = num_series.max() - num_series.min()

# find the standard deviation
std_dev = num_series.std()

# print the statistical measures
print("Original Series:\n", num_series)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", range_val)
print("Standard Deviation:", std_dev)

print("21DCE052")