# Python code to demonstrate the working of
# prmonth() and setfirstweekday()

# importing calendar module for calendar operations
import calendar

# using prmonth() to print calendar of 1997
print("The 4th month of 1997 is : ")
calendar.prmonth(1997, 4, 2, 1)


# using setfirstweekday() to set first week day number
calendar.setfirstweekday(4)

print("\r")

# using firstweekday() to check the changed day
print("The new week day number is : ", end="")
print(calendar.firstweekday())
