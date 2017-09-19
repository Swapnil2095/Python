# Python code to demonstrate the working of
# asin(), acos(), atan()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = 1.0

y = 1.0

# converting x and y into complex number z
z = complex(x, y)

# printing arc sine of the complex number
print("The arc sine value of complex number is : ", end="")
print(cmath.asin(z))

# printing arc cosine of the complex number
print("The arc cosine value of complex number is : ", end="")
print(cmath.acos(z))

# printing arc tangent of the complex number
print("The arc tangent value of complex number is : ", end="")
print(cmath.atan(z))
