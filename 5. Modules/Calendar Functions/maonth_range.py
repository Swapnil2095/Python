# Python code to demonstrate the working of
# monthrange() and prcal()

# importing calendar module for calendar operations
import calendar

# using monthrange() to print start week day and
# number of month
print("The start week number and no. of days of month : ", end="")
print(calendar.monthrange(2008, 2))

# using prcal() to print calendar of 1997
print("The calendar of 1997 is : ")
calendar.prcal(1997, 2, 1, 6)
