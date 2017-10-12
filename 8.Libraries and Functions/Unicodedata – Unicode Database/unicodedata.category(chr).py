import unicodedata

print (unicodedata.category(u'A'))
print (unicodedata.category(u'b'))


'''
This function returns the general category assigned to the given character as string. 
For example, it returns ‘L’ for letter and ‘u’ for uppercase.
'''
