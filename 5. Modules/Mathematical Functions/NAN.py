# Python code to demonstrate the working of
# inf, nan, isinf(), isnan()

# importing "math" for mathematical operations
import math

# checking if number is nan
if (math.isnan(math.nan)):
	print("The number is nan")
else:
	print("The number is not nan")

# checking if number is positive infinity
if (math.isinf(math.inf)):
	print("The number is positive infinity")
else:
	print("The number is not positive infinity")
