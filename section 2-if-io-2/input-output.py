
# coding: utf-8

# In this notebook we will discuss the following:
#     
# 1) Input and output functions
# 
# 2) Single and multi-line comments
# 
# 3) Multi line statement
# 
# 4) stdout using print
# 
# 5) formatted printing
# 
# 6) stdin using raw_input
# 
# 7) Reading from and writing to text file
# 
# 8) Changing and obtaining file handler's position in text file

# In[ ]:

a = 4
print a # a simple print statement 


# In[ ]:

print'the value of a is: ',a 


# In[ ]:

print 'the value of a is %d' %a 


# In[ ]:

# Single line comment in Python should start with # 

'''
Multiple line comments should either start and end with three single 
quotes or start and end with three double quotes.
'''
# or

"""
Multiple line comments should either start and end with three single 
quotes or start and end with three double quotes.
"""


# In[ ]:

'''
Multi-line statements can be indicated by '\' at the end of each line except 
for the last line

total = item_one + \
        item_two + \
        item_three

'''
a = 4 + \
    5 + \
    10 


print 'the value is: %d' %a # this is an example of a formatted print
print a
print a + 1


# In[ ]:

# stringA.upper() converts stringA to uppercase
a = 'apple'
print a.upper()


# In[ ]:

# stringA.lower() converts stringA to lowercase
a = 'Hyderabad'
print a.lower()

b = 'BANANA'
print b.lower()


# In[ ]:

# formatted printing
print '{0} and {1}'.format('san jose','santa clara')


# In[ ]:

print '{0} and {1}'.format('san jose') # fails as we need to provide two values


# In[ ]:

print '{0}'.format('san jose','santa clara') 
# the first value in the list will be printed


# In[ ]:

print '{nearcity} and {farcity}'.format(farcity='Sacramento',nearcity='San jose')


# In[ ]:

import math 
print 'PI = %0.5f' %(math.pi) # The () is optional for one input


# In[ ]:

a = 5
b = 3.25
c = '5.6'
print 'a = %03d b = %0.2f c = %s' %(a,b,c)


# In[ ]:

'''
raw_input() gets input from the command line.
In this example, we are getting the input from the user and assigning it 
to variable s.
'''
s = raw_input('Enter a name : ')
print s


# In[ ]:

a = 'r'
b = str(2)
print a+b


# In[ ]:

'''
In-class activity: Can you insert a space between r and 2? If yes, then 
implement it. 
'''


# In[ ]:

'''
In-class activity: Can you ask the user to enter an integer greater than 50. 
Then print the value and also its type.
'''


# In[ ]:

'''
Note - Go to for-loop iPython notebook. 
'''


# In[ ]:

# f is a filehandler
f = open('python_list.txt')
# readlines reads one line at a time from the file
# Syntax filehandle.readlines()
for line in f.readlines():
    print line.strip() 
# strip removes newline, carriage return, space etc at the beginning and 
# at the end of the line
f.close()


# In[ ]:

# f is a filehandler
f = open('python_list.txt')
# readlines reads one line at a time from the file
# Syntax filehandle.readlines()
for line in f.readlines():
    cleanedline = line.strip() 
    if cleanedline:
        print cleanedline
f.close()


# In[ ]:

fo = open('python_list.txt', 'r')
print fo.readlines()
# fo.readlines is a list of string where each item in the list is a string.

# Why does the for-loop not produce any output ???
for items in fo.readlines():
    print 'inside for-loop',items
fo.close()


# In[ ]:

# tell() returns the current position within the file. 
fo = open('python_list.txt', 'r')
for items in fo.readlines():
    print items
print fo.tell()

#fo.close()


# seek() changes the current file position
# syntax - 
# ```
# filehandler.seek(offset, position)
# ```
# 
# The number of bytes to be moved is given in offset argument.
# In the position argument the bytes are to be moved is given.
# position = 0, means the reference position is the beginning of the file
# position = 1, means the reference position is the current position 
# position = 2, means the reference position is the end of the file

# In[ ]:

fo.seek(3,1)
print fo.tell()
print fo.read(5)

fo.seek(1,0)
print fo.tell()
print fo.read(5)

fo.seek(1,2)
print fo.tell()
print fo.read(3)


# In[ ]:

fo.seek(0,0)
print fo.tell()
for i in fo.readlines():
    print i


# In[ ]:

# Writing a file
fo = open('python_list1.txt', 'w+') 
# here the text file is opened in write and read mode. 
fo.writelines('1,2,3\n')
fo.writelines('a,b,c\n')
print fo
fo.close()

fo = open('python_list1.txt', 'r')
for items in fo.readlines():
    print items.strip()
fo.close()


# In[ ]:

# appending to a file
fo = open('python_list1.txt','a') 
# here the text file is opened in append mode
fo.writelines('little puppy\n')
fo.writelines('cute cub \n')
print fo
fo.close()

fo = open('python_list1.txt','a+')
for items in fo.readlines():
    print items.strip()
fo.close()


# The with keyword is called the context manager.
# It will close the file whether or not there is an exception.

# In[ ]:

with open('python_list1.txt', 'r') as fo:
    for items in fo.readlines():
        print items.strip()
# close does not have to be called exclusively 


# In[ ]:

'''
In-class activity: Create a txt file and write names of 4 states and close 
the file. Then open the file and print each line. 
'''


# In[ ]:

'''
Instead of Python 2.7 raw_input(), in Python 3, you should use input().
'''

