import secrets

token1 = secrets.token_hex(16)
token2 = secrets.token_hex(9)

print(token1)
print(token2)


'''

secrets.token_hex([nbytes=None]) : 
This function is responsible for generating a random text string in 
hexadecimal containing nbytes random bytes. If no value is provided, 
a reasonable default is used.

'''