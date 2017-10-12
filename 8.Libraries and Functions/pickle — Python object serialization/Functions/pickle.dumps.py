# Python program to illustrate
#Picle.dumps()
import pickle

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
data_string = pickle.dumps(data)
print ('PICKLE:', data_string)


'''
pickle.dumps(obj, protocol = None, *, fix_imports = True)
This function returns the pickled representation of the object as a bytes object.

'''
