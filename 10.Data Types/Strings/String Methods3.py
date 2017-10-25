# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )

# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )

# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )


# Python code to demonstrate working of 
# min() and max()
str = "geeksforgeeks"

# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str));

# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str));


# Python code to demonstrate working of 
# maketrans() and translate()
#from string import maketrans # for maketrans() #for 2.6 to 3

str = "geeksforgeeks"

str1 = "gfo"
str2 = "abc"

# using maktrans() to map elements of str2 with str1
mapped = str.maketrans( str1, str2 );

# using translate() to translate using the mapping
print ("The string after translation using mapped elements is : ")
print (str.translate(mapped))


# Python code to demonstrate working of 
# replace()

str = "nerdsfornerds is for nerds"

str1 = "nerds"
str2 = "geeks"

# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 



