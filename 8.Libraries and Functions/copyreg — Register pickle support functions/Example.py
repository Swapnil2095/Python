# Python 3 program to illustrate
# use of copyreg module
import copyreg
import copy
import pickle


class C(object):
	def __init__(self, a):
		self.a = a


def pickle_c(c):
	print("pickling a C instance...")
	return C, (c.a, )


copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
print(d)

p = pickle.dumps(c)
print(p)


'''

The copyreg module defines functions which are used by pickling specific objects
 while pickling or copying. This module provides configuration information 
 about object constructors(may be factory functions or class instances) 
 which are not classes.

copyreg.constructor(object)
This function is used for declaring object as a valid constructor. 
An object is not considered as a valid constructor if it is not callable. 
This function raises TypeError if the object is not callable.

copyreg.pickle(type, function, constructor=None)
This is used to declare function as a “reduction” function for objects of type type.
 function should return either a string or a tuple containing two or three elements.
The constructor parameter is optional. It is a callable object which can be used
 to reconstruct the object when called with the tuple of arguments returned by
  function at pickling time. TypeError is raised if object is a class or 
  constructor is not callable.



'''