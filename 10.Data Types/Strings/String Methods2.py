# Python code to demonstrate working of 
# len() and count()
str = "geeksforgeeks is for geeks"

# Printing length of string using len()
print (" The length of string is : ", len(str));

# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""geeks"" is : ",end="")
print (str.count("geeks",0,15))


# Python code to demonstrate working of 
# center(), ljust() and rjust()
str = "geeksforgeeks"

# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))

# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))

# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))



# Python code to demonstrate working of 
# isalpha(), isalnum(), isspace()
str = "geeksforgeeks"
str1 = "123"

# Checking if str has all alphabets 
if (str.isalpha()):
	print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
	print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
	print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")



# Python code to demonstrate working of 
# join()
str = "_"
str1 = ( "geeks", "for", "geeks" )

# using join() to join sequence str1 with str
print ("The string after joining is : ", end="")
print ( str.join(str1))

