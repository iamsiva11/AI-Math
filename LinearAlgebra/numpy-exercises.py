"""
from: 
https://github.com/rougier/numpy-100
"""
import numpy as py

"""
Basic Exercises
"""

#Version and config
print np.__version__
np.show_config()

#Create a null vector of size 10
Z = np.zeros(12)
print Z

#How to find the memory size of any array 
print Z.size # no of elemeents 
print Z.itemsize #bytes 
print Z.Size * Z.items

#Create a null vector of size 10 but the fifth value which is 1
Z =np.zeros(10)
Z[4]=1
print Z

#Create a vector with values ranging from 10 to 49 
Z = np.arange(10,49)
print Z

#Reverse a vector (first element becomes last)
Z = np.arange(10)
rev_Z= Z[::-1]
print rev_Z

#Create a 3x3 matrix with values ranging from 0 to 8 
Z = np.arange(9).reshape(3,3)
print Z

#Create a 3x3 identity matrix
Z=np.eye(3)
print Z

#Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
print Z

#Create a 10x10 array with random values and find the minimum and maximum values
Z= np.random.random((10,10))
Zmin , Zmax = Z.min(),Z.max()
print Zmin,Zmax

#Create a random vector of size 30 and find the mean value 
Z = np.random.random(10)
print Z.mean()











