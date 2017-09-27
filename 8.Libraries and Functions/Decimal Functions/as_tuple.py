# Python code to demonstrate the working of 
# as_tuple() and fma()

# importing "decimal" module to use decimal functions
import decimal

# using as_tuple() to return decimal number as tuple
a = decimal.Decimal(-4.5).as_tuple()

# using fma() to compute fused multiply and addition
b = decimal.Decimal(5).fma(2,3)

# printing the tuple
print ("The tuple form of decimal number is : ",end="")
print (a)

# printing the fused multiple and addition
print ("The fused multiply and addition of decimal number is : ",end="")
print (b)


'''

5. as_tuple() :- Returns the decimal number as tuple containing 3 arguments, sign(0 for +, 1 for -), 
digits and exponent value.

6. fma(a,b) :- This “fma” stands for fused multiply and add. 
It computes (num*a)+b from the numbers in argument. No rounding of (num*a) takes place in 
this function.


'''