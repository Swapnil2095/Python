# A Simple Python templaye example
from string import Template

# Create a template that has placeholder for value of x
t = Template('x is $x')

# Substitute value of x in above template
print(t.substitute({'x': 1}))
