# Python code to demonstrate the working of
# log10(), sqrt()
# importing "cmath" for complex number operations
import cmath
import math

# Initializing real numbers
x = 1.0
y = 1.0

# converting x and y into complex number
z = complex(x, y)

# printing log10 of complex number
print("The log10 of complex number is : ", end="")
print(cmath.log10(z))

# printing square root form of complex number
print("The square root of complex number is : ", end="")
print(cmath.sqrt(z))
