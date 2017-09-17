def hello(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print ("%s == %s" % (key, value))


hello(name="GeeksforGeeks")
