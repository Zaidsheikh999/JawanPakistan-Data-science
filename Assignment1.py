#task 1

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#task 2

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#task 3

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#task 4

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#task 5

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#task 6


a = input('Enter first number: ')
b = input('Enter second number: ')
 
sum = (a) + (b)
 
print('The sum of {0} and {1} is {2}'.format(a, b, sum))