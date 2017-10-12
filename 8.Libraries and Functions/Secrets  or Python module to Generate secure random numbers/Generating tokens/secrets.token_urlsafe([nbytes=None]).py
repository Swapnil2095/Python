import secrets

url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
print(url)


'''

secrets.token_urlsafe([nbytes=None]) : 
This function is responsible for generating a random URL-safe text string 
containing nbytes random bytes. This is suitable for password recovery applications.

Example : Generate a hard-to-guess temporary URL containing a security token.

'''
