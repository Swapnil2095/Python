# Python code to demonstrate the working of
# asinh(), acosh(), atanh()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = 1.0

y = 1.0

# converting x and y into complex number z
z = complex(x, y)

# printing inverse hyperbolic sine of the complex number
print("The inverse hyperbolic sine value of complex number is : ", end="")
print(cmath.asinh(z))

# printing inverse hyperbolic cosine of the complex number
print("The inverse hyperbolic cosine value of complex number is : ", end="")
print(cmath.acosh(z))

# printing inverse hyperbolic tangent of the complex number
print("The inverse hyperbolic tangent value of complex number is : ", end="")
print(cmath.atanh(z))
