# Accessing items using enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
	print (x)


# demonstrating use of start in enumerate
for x in enumerate(cars, start=1):
	print (x[0], x[1])


# Printing return value of enumerate() 
print (enumerate(cars))


# Accessing items and indexes enumerate()
for x in enumerate(cars):
	print (x[0], x[1])
