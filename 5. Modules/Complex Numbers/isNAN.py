# Python code to demonstrate the working of
# isnan(), isinf(), isfinite()

# importing "cmath" for complex number operations
import cmath
import math

# Initializing real numbers
x = 1.0
y = 1.0
a = math.inf
b = math.nan

# converting x and y into complex number
z = complex(x, y)

# converting x and a into complex number
w = complex(x, a)

# converting x and b into complex number
v = complex(x, b)

# checking if both numbers are finite
if cmath.isfinite(z):
	print("Complex number is finite")
else:
	print("Complex number is infinite")

# checking if either number is/are infinite
if cmath.isinf(w):
	print("Complex number is infinite")
else:
	print("Complex number is finite")

# checking if either number is/are infinite
if cmath.isnan(v):
	print("Complex number is NaN")
else:
	print("Complex number is not NaN")
