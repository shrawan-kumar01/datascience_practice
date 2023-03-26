'''
DTATA PROCESSING WITH NUMPY ARRAY 
IT REMPVE THE LOOP METHOD BY ARRAY OPERATION 
it is 32 or 3 magnitude faster than norma python 

'''
#  the practice replacing the explicite loop with array expression is called array vactorization

"""
problem description :
calculate :----------> squrt(x^2+y^2) across a regular grid of values

hint:~  np.meshgrid :-------->> fxn takes two 1-d array and produce two 2-d matrices coressponding to all points of (x,y) in two arrays 
"""

#  import module numpy

#  take 1000 random points
import  matplotlib.pylab as plt
import numpy as np
if __name__ == "__main__":
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)

    # print(xs)
    # print()
    # print(ys)

    z = np.sqrt(xs ** 2 + ys ** 2)
    # print(z)

    #  importing the py plote as plty


    plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
    plt.colorbar()
    plt.title("image plotting of $\sqrt{x^2 + y^2}$ for a grid value ")
