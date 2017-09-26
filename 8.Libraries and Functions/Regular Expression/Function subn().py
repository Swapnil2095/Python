import re
print(re.subn('ub', '~*', 'Subject has Uber booked already'))
t = re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)
print(len(t))

print("Each Tuple->")
# This will give same output as sub() would have
print(t[0])
print(t[1])

