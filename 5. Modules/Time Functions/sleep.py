# Python code to demonstrate the working of
# sleep()

# importing "time" module for time operations
import time

# using ctime() to show present time
print ("Start Execution : ",end="")
print (time.ctime())

# using sleep() to hault execution
time.sleep(4)

# using ctime() to show present time
print ("Stop Execution : ",end="")
print (time.ctime())
