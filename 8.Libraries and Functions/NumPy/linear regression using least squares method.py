import numpy as np
import matplotlib.pyplot as plt

# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0]

# plotting the line
line = w[0] * x + w[1]  # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()


'''
A linear regression line is of the form w1x + w2 = y and it is the line that 
minimizes the sum of the squares of the distance from each data point to the line. 
So, given n pairs of data (xi, yi), the parameters that we are looking for are w1 and w2 
which minimize the error:

'''
