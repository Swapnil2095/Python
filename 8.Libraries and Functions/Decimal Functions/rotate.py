# Python code to demonstrate the working of 
# rotate() and shift()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(2343509394029424234334563465)

# using rotate() to rotate the first argument
# rotates to right by 2 positions
print ("The rotated value is : ",end="")
print (a.rotate(-2))

# using shift() to shift the first argument
# rotates to left by 2 positions
print ("The shifted value is : ",end="")
print (a.shift(2))


'''

11. rotate() :- This function rotates the first argument by the amount mentioned in the second argument. If the sign of second argument is positive, rotation is towards left, else the rotation is towards right. The sign of first argument is unchanged.

12. shift() :- This function shifts the first argument by the amount mentioned in the second argument. If the sign of second argument is positive, shifting is towards left, else the shifting is towards right. The sign of first argument is unchanged. Digit shifted are replaced by 0.

'''