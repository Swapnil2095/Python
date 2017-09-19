# Python code to demonstrate the working of
# fromtimestamp(), min() and max()

# importing built in module datetime
import datetime
from datetime import date

# using fromtimestamp() to calculate date
print ("The calculated date from seconds is : ",end="")
print (date.fromtimestamp(3452435))

# using min() to print minimum representable date
print ("Minimum representable date is : ",end="")
print (date.min)

# using max() to print minimum representable date
print ("Maximum representable date is : ",end="")
print (date.max)
