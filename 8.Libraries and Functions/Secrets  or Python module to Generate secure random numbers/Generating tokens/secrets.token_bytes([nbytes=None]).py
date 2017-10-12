import secrets

token1 = secrets.token_bytes()
token2 = secrets.token_bytes(10)

print(token1)
print(token2)


''''
secrets.token_bytes([nbytes=None]) : 
This function is responsible for generating a random byte string containing 
nbytes number of bytes. If no value is provided, a reasonable default is used.

How many bytes should tokens use? 
At least 32 bytes for tokens should be used to be secure against a brute-force attack.

'''
