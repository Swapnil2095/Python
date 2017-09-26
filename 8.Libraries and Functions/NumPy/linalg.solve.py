import numpy as np


'''
Let us assume that we want to solve this linear equation set:

x + 2*y = 8
3*x + 4*y = 18

'''
# coefficients
a = np.array([[1, 2], [3, 4]])
# constants
b = np.array([8, 18])

print("Solution of linear equations:", np.linalg.solve(a, b))
