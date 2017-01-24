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
