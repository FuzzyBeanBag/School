#!/usr/bin/python

#=====================================================
# Variables
#=====================================================
myString = "This is a string!" # This is a string variable
myInteger = 5 # This is an integer value
myFloat = 5.5 #This is a floating-point value
myList = [ 1, 2, 3, 4, 5] #This is a list of integers
myDict = { 'name' : 'Python User', 'value' : 75 } #This is a dictionary with keys representing # Name and Value

#====================================================
# Multiple Line Comments
#====================================================

"""
This is a Python comment. We can make them multiple lines
And not have to deal with spacing This makes it easier to 
make readable comment headers
"""

#===================================================
# String Manipulation
#===================================================
print "\n\n"
print 'myString = "This is a string! " '+"#" + ' This is a string variable'
print 'myInteger = 5 ' '#'  ' This is an integer value'
print 'myFloat = 5.5 '+ "#" + ' This is a floating-point value'
print 'myList = [ 1, 2, 3, 4, 5] ' + "#" + ' This is a list of integers'
print 'myDict = { \'name\' :, \'Python User\', \'value\' : 75 } ' + '# This is a dictionary with keys representing ' + '# Name and Value'
print "\n"
print '\"\"\"'
print 'This is a Python comment. We can make them multiple lines'
print 'And not have to deal with spacing'
print 'This makes it easier to make readable comment headers'
print '\"\"\"'
print "\n"
print "And our code still works!\n\n\n"
myString2 = "This is a cool String"
print 'myString2 = "This is a Cool String\"\n'
print 'print "The first 4 characters are " + myString2[:4]' + "\n"
print "The first 4 characters are " + myString2[:4] + "\n"
print '"When os becomes 0s, the string is " + myString2.replace("o","0")' + "\n"
print "When os becomes 0s, the string is " + myString2.replace("o","0") + "\n"
print 'myList = myString2.split(" ")' + "\n"
myList = myString2.split(" ")
print 'print myList' + "\n"
print myList
print "\n\n"




