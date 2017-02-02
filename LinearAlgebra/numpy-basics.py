"""
Ref:http://cs231n.github.io/python-numpy-tutorial/#numpy-math
"""

import numpy as np

a = np.arange(15).reshape(3, 5)
print a

print a.shape
print a.ndim
print type(a)

#np.range method
np.arange(10,30,5)
np.arange(0,2,0.3)

#linsapce and arange
#improvised arange for floating point numbers
y= np.linspace( 0, 2, 4 )   # 9 numbers from 0 to 2
#x = np.linspace( 0, 2*pi, 100 ) 

print y
print np.sin(y)

####################################################################################

#Numpy also provides many functions to create arrays:
#Different ways to creatwe arrays

#array of zeros
a = np.zeros((2,2))
print a
#array of ones
a = np.ones((2,2))
print a
#Constant array
a= np.full((2,2),3)
print a
#identity matrix
a= np.eye(2)
print a
#Array filled with random values
a = np.random.random((2,2))
print a
#Create empty array with shap like <x>
y = np.empty_like(a)
print y

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

####################################################################################
# Array Indexing
# Numpy offers several ways to index into arrays.
# Slicing: Similar to Python lists, numpy arrays can be sliced. 
# Since arrays may be multidimensional, you must specify a slice for 
# each dimension of the array:
#First 2 rows, columns 1 and 2

b =a[:2, 1:3]
print b

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print a[0, 1]   # Prints "2"
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print a[0, 1]   # Prints "77"

####################################################################################
#Mixing integer indexing with slice indexing
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a

print row_r1, row_r1.shape  # Prints "[5 6 7 8] (4,)"
print row_r2, row_r2.shape  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]

print col_r1, col_r1.shape 
print col_r2, col_r2.shape 

####################################################################################
#Integer array indexing
a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and 
print a[[0, 1, 2], [0, 1, 0]]  # Prints "[1 4 5]" #(0,0) , (1,1) ,(2,0)

# The above example of integer array indexing is equivalent to this:
print np.array( [ a[0,0], a[1,1], a[2,0] ] )

# When using integer array indexing, you can reuse the same
# element from the source array:
print a[[0, 0], [1, 0] ] # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print np.array([a[0,1], a[0,1]])

####################################################################################
#selecting or mutating one element from each row of a matrix:

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

# Create an array of indices
b = np.array([0, 2, 0, 1])

print a
print a[np.arange(4), b] # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10
print a


####################################################################################
#Boolean array indexing
a = np.array([[1,-2], [-13, 4], [0, 6]])

bool_idx = (a > 0)

print bool_idx

print a[bool_idx]
# We can do all of the above in a single concise statement:
print a[a > 0]     # Prints "[3 4 5 6]"

#Elements without affecting the shape of the array/matrix 
print a*bool_idx

