print(2.9987)
print(3 * 4 + 5)
# Use parantheses to specify the order
print(3 * (4 + 5))
# finding MOD
print(10 % 3)
# can store a number in variables

my_num =-6
print(my_num)
# can convert this number into astring (can be useful when we want to store a number alongside string )
print(str(my_num) + " is my favourite number" )
# printing absolute value of a number
print (abs(my_num))

# CONVERSION
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#ASSIGNING MULTIPLE VALUES

A, B, C = "Tulips" , "lilies" , "Jasmine"
print(A)
print(B)
print(C)

#UNPACKING A COLLECTION INTO VARIABLES

Flowers = ["roses" , "jasmine" , "Daises"]
Aney, Tanzila, Aiza = Flowers
print(Aney)
print(Tanzila)
print(Aiza)

# GIVING POWER TO ANUMBER 
print(pow(3, 2))

# round a number
print (round(3.25))

# to access math functions

from math import *
numb_er = -5
print(floor(3.2))  # grabs the lowest number


