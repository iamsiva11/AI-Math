"""
Linear algebra 101
"""
import numpy as np
import numpy.linalg as linalg

#Matrix inverseand A * A^-1
a = np.array([[3., 4., 0.],
			 [-4., 5, 0.],
			 [0., 0., 9.]])
b=linalg.inv(a)
#Matrix product of A ndnd A^-1(A Inverse)
print np.dot(b,a)		

#Solving linear system ofequations
d = [1,3,4]
x = linalg.solve(a,d)
print x
