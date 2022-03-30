import array
import keyword

import numpy as np
import numpy.typing as npt


# Python Keywords
print(keyword.kwlist)

# Conditionals
A: int = 3
B: int = 2

if A > B:
    print("A is greater than B")
elif A < B:
    print("A is less than B")
else:
    print("A is equals to B")

# List
my_list: list[int] = [x for x in range(5)]
print(my_list)

# Array
my_array = array.array("i", my_list)
print(my_list)

# Loops
i = 0
while i < 10:
    print("I: ", i, sep=" ")
    i += 1

for items in my_list:
    print("Item: ", items, sep= " ")

# Numpy
np_array_1: npt.NDArray[np.int_] = np.arange(10)    #type: ignore
np_array_2: npt.NDArray[np.int_] = np.arange(10)    #type: ignore
print(np_array_1)
print(np_array_2)
print("Sum: ", np_array_1 + np_array_2)
