# Python code to demonstrate range() 
# on basis of memory

import sys

# initializing a with range()
a = range(1,10000)



# testing the size of a
# range() takes more memory
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))

