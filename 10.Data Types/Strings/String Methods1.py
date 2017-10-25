# Python code to demonstrate working of 
# find() and rfind()
str = "geeksforgeeks is for geeks"
str2 = "geeks"

# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) )

# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )


# Python code to demonstrate working of 
# startswith() and endswith()
str = "geeksforgeeks"
str1 = "geeks"

# using startswith() to find if str starts with str1
if str.startswith(str1):
		print ("str begins with str1")
else : print ("str does not begin with str1")

# using endswith() to find if str ends with str1
if str.startswith(str1):
	print ("str ends with str1")
else : print ("str does not end with str1")


# Python code to demonstrate working of 
# isupper() and islower()
str = "GeeksforGeeks"
str1 = "geeks"

# checking if all characters in str are upper cased
if str.isupper() :
	print ("All characters in str are upper cased")
else : print ("All characters in str are not upper cased")

# checking if all characters in str1 are lower cased
if str1.islower() :
	print ("All characters in str1 are lower cased")
else : print ("All characters in str1 are not lower cased")


# Python code to demonstrate working of 
# upper(), lower(), swapcase() and title()
str = "GeeksForGeeks is fOr GeeKs"

# Coverting string into its lower case
str1 = str.lower();
print (" The lower case converted string is : " + str1)

# Coverting string into its upper case
str2 = str.upper();
print (" The upper case converted string is : " + str2)

# Coverting string into its swapped case
str3 = str.swapcase();
print (" The swap case converted string is : " + str3)

# Coverting string into its title case
str4 = str.title();
print (" The title case converted string is : " + str4)
