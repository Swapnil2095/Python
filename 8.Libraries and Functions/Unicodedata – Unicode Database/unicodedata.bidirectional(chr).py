import unicodedata

print (unicodedata.bidirectional(u'\u0660'))


'''
This function returns the bidirectional class assigned to the given character as string. 
For example, it returns ‘A’ for arabic and ‘N’ for number. 
An empty string is returned by this function if no such value is defined.

'''
