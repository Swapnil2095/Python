# Python code to demonstrate the working of
# sin(), cos(), tan()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = 1.0

y = 1.0

# converting x and y into complex number z
z = complex(x, y)

# printing sine of the complex number
print("The sine value of complex number is : ", end="")
print(cmath.sin(z))

# printing cosine of the complex number
print("The cosine value of complex number is : ", end="")
print(cmath.cos(z))

# printing tangent of the complex number
print("The tangent value of complex number is : ", end="")
print(cmath.tan(z))
