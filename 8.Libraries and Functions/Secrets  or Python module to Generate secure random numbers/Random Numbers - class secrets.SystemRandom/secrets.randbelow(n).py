import secrets

passwd = secrets.randbelow(20)
print(passwd)


'''
secrets.randbelow(n): This function returns a random integer in the range [0, n).

'''
