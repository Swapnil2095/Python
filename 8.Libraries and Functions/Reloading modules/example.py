import importlib
importlib.reload(module)

'''
reload() reloads a previously imported module. 
This is useful if you have edited the module source file using an external editor 
and want to try out the new version without leaving the Python interpreter. 
The return value is the module object.

Note: The argument should be a module which has been successfully imported.

'''
