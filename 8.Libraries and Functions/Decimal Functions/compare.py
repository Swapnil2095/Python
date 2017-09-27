# Python code to demonstrate the working of 
# compare() and compare_total_mag()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(-9.56)

# comparing decimal numbers using compare()
print ("The result of comparison using compare() is : ",end="")
print (a.compare(b))

# comparing decimal numbers using compare_total_mag()
print ("The result of comparison using compare_total_mag() is : ",end="")
print (a.compare_total_mag(b))


'''
7. compare() :- This function is used to compare decimal numbers. 
Returns 1 if 1st Decimal argument is greater than 2nd, 
        -1 if 1st Decimal argument is smaller than 2nd and 
        0 if both are equal.

8. compare_total_mag() :- Compares the total magnitute of decimal numbers. 
Returns 1 if 1st Decimal argument is greater than 2nd(ignoring sign), 
        -1 if 1st Decimal argument is smaller than 2nd(ignoring sign) and 
        0 if both are equal(ignoring sign).

'''

