from cgi import print_arguments
from gettext import npgettext
import numpy as np 
x = np.array([[1,2,3],[5,6,7]])
y = np.array([[6,23],[-1,7],[8,9]])
# xy_dot = x.np.dot(y)        #AttributeError: 'numpy.ndarray' object has no attribute 'np'
xy_dot = np.dot(x,y)
print(xy_dot)

'''
a matrix product between 2d array and sutiably size 1d array reasult in 1d arrray 
'''

x_ones = np.dot(x,np.ones(3))
print(x_ones)


from numpy.linalg import inv , qr

x_rndn = np.random.randn(5,5)
print(x_rndn)
print()
mat = x_rndn.T.dot(x_rndn)
print(inv(mat))
# print(mat.dot.inv(mat))         #AttributeError: 'builtin_function_or_method' object has no attribute 'inv'
# print(mat)


y_mat = mat.dot(inv(mat))
print(y_mat)


q,r = qr(mat)
print(r)
print()
print(q)











