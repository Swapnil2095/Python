import secrets
import string

#exqmple 1

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(10))

print(password)


'''
#example 2
alphabet = string.ascii_letters + string.digits
while True:
	password = ''.join(secrets.choice(alphabet) for i in range(10))
	if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) &gt;= 3):
		print(password)
		break

'''

'''

The secrets module is used for generating random numbers for managing 
important data such as passwords, account authentication, security tokens, and 
related secrets, that are cryptographically strong. This module is responsible 
for providing access to the most secure source of randomness. 
This module is present in Python 3.6 and above.


secrets.choice(sequence): This function returns a randomly-chosen element 
from a non-empty sequence to manage a basic level of security.

Example 1 : Generate a ten-character alphanumeric password.

Example 2 : Generate a ten-character alphanumeric password with at least one lowercase character, 
at least one uppercase character, and at least three digits.


'''
