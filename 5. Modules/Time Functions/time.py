# Python code to demonstrate the working of
# time() and gmtime()

# importing "time" module for time operations
import time

# using time() to display time since epoch
print ("Seconds elapsed since the epoch are : ",end="")
print (time.time())


# using gmtime() to return the time attribute structure
print ("Time calculated acc. to given seconds is : ")
print (time.gmtime())
