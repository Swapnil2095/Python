# Python code to demonstrate the working of 
# remainder_near() and scaleb()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(23.765)

# Initializing decimal number
b = decimal.Decimal(12)

# Initializing decimal number
c = decimal.Decimal(8)

# using remainder_near to compute value
print ("The computed value using remainder_near() is : ",end="")
print (b.remainder_near(c))

# using scaleb() to shift exponont
print ("The value after shifting exponent : ",end="")
print (a.scaleb(2))


'''
13. remainder_near() :- Returns the value “1st – (n*2nd)” where n is the integer value nearest to the result of 1st/2nd. If 2 integers have exactly similar proximity, even one is choosen.

14. scaleb() :- This function shifts the exponent of 1st number by the value of second argument.

'''