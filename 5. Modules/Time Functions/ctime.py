# Python code to demonstrate the working of
# asctime() and ctime()

# importing "time" module for time operations
import time

# initializing time using gmtime()
ti = time.gmtime()

# using asctime() to display time acc. to time mentioned
print ("Time calculated using asctime() is : ",end="")
print (time.asctime(ti))


# using ctime() to diplay time string using seconds 
print ("Time calculated using ctime() is : ", end="")
print (time.ctime())
