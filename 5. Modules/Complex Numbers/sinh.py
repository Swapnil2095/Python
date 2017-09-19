# Python code to demonstrate the working of 
# sinh(), cosh(), tanh()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = 1.0

y = 1.0

# converting x and y into complex number z
z = complex(x,y);

# printing hyperbolic sine of the complex number
print ("The hyperbolic sine value of complex number is : ",end="")
print (cmath.sinh(z))

# printing hyperbolic cosine of the complex number
print ("The hyperbolic cosine value of complex number is : ",end="")
print (cmath.cosh(z))

# printing hyperbolic tangent of the complex number
print ("The hyperbolic tangent value of complex number is : ",end="")
print (cmath.tanh(z))
