import secrets

passwd = secrets.randbits(7)
print(passwd)

'''
secrets.randbits(k): This function returns an int with k random bits.

'''