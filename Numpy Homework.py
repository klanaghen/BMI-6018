#Problem 1: Import Numpy and print version
import numpy as np
print("1: numpy version", np.__version__)

#Problem 2: Create 1D array from numbers 0 to 9
from numpy import array as ar
arr1 = ar([0,1,2,3,4,5,6,7,8,9])
print("2:", arr1)

#Problem 3: Import a dataset with numbers and texts keeping the text intact in python numpy
import numpy as np

iris_data = np.genfromtxt(
    "/Users/kimlanaghen/Downloads/iris.data.txt",
    delimiter=",",
    dtype=None,        # allows mixed types (numbers + text)
    encoding="utf-8"   # ensures text is read correctly
)

print(iris_data)

#Problem 4: Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset

petal_width = iris_data['f3'] #Set petal width

# Find first occurrence of value > 1.0
first_index = np.argmax(petal_width > 1.0)

print("4: The first occurrence of a petal width > 1.0 is at position:", first_index)
print("Value:", petal_width[first_index])

#Problem 5:
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print("Original array:\n", a)

#boolean mask
a[a > 30] = 30
a[a < 10] = 10
print("Modified array:\n", a)


