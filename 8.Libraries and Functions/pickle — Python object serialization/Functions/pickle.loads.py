# Python program to illustrate
# pickle.loads()
import pickle
import pprint

data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print ('BEFORE:',pprint.pprint(data1))

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print ('AFTER:',pprint.pprint(data2))

print ('SAME?:', (data1 is data2))
print ('EQUAL?:', (data1 == data2))


'''

pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
This function is used to read a pickled object representation from a bytes object 
and return the reconstituted object hierarchy specified.

'''
