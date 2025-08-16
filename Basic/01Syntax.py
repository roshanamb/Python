import sys
import keyword

print(sys.version)
print("Hello Roshan, Welcome to Python learning")
print("Whenever you are done in the python command line, you can simply type the following to quit the python command line interface: exit()");

x,y,z = str(3), int(3), float(3)   # Assign values to multiple variables in one line:   or x, y = "python"
 # x will be '3'
 # y will be 3
 # z will be 3.0

print(str(type(x)) , " - " , x, str(type(y)) + " - " + str(y), str(type(z)) + " - " + str(z));
# print(str(type(y)) + " - " + str(y));
# print(str(type(z)) + " - " + str(z));

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z);

print(keyword.kwlist) # List all 34 Keywords of Python

