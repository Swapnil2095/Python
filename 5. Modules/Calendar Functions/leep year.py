# Python code to demonstrate the working of
# isleap() and leapdays()

# importing calendar module for calendar operations
import calendar

# using isleap() to check if year is leap or not
if (calendar.isleap(2008)):
	print("The year is leap")
else:
	print("The year is not leap")

#using leapdays() to print leap days between years
print("The leap days between 1950 and 2000 are : ", end="")
print(calendar.leapdays(1950, 2000))
