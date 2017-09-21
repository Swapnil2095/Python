# Python example to check if a class is
# subclass of another


class Base(object):
	pass  # Empty Class


class Derived(Base):
	pass  # Empty Class


# Driver Code
print(issubclass(Derived, Base))  # True
print(issubclass(Base, Derived))  # False

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))  # False

# But d is an instance of Base
print(isinstance(d, Base))  # True
