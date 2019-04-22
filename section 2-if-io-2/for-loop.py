
# coding: utf-8

# In this notebook we will discuss the following:
#     
# 1) if-else
# 
# 2) while
# 
# 3) for-loop
# 
# 4) range and xrange

# In[ ]:

'''
Syntax of if-else
if condition 1:
   execute statement(s) that are under this block
elif condition 2:
    execute statement(s) that are under this block
else:
    execute statement(s) that are under this block
'''

x = int(raw_input("Please enter your choice (0 or 1): "))
if x < 0:
    print 'Negative number not allowed'
elif x == 0:
    print "Zero"
elif x == 1:
    print 'One'
else:
    print 'Number more than 1 is not allowed'


# In Python, we can compute bool of any data type. What?
# bool of non-trivial values of any data type will return True whereas bool of trivial values of any data type will return False.
# 
# bool(0) is False
# 
# bool(-1) is True
# 
# bool('') is False
# 
# bool(' ') is True
# 
# bool(0.0) is False
# 
# bool(0.1) is True
# 
# This will be useful especially when you want to check if something is empty or not using the if-else condition. 

# 
# To learn more about Truthiness in Python check the following links
# 
# https://www.udacity.com/wiki/cs258/truthiness-in-python
# 
# https://docs.python.org/release/2.5.2/lib/truth.html
# 
# https://www.youtube.com/watch?v=9OK32jb_TdI

# In[ ]:

a = 0
if a:
    print 'a is non zero integer'
else:
    print 'a is zero'


# In[ ]:

a = 0.0
if a:
    print "a is non zero float"
else:
    print "a is 0.0"


# In[ ]:

a = ''

if a:
    print "a is a non-empty string"
    
else:
    print "a is an empty string"


# In[ ]:

'the    life  is    good   '.strip(' ')


# In[2]:

';the    life  is    good   '.strip('; ')


# Syntax for list 
# 
# n = [item1, item2, item3].
# 
# Simple way to create a list of integers
# is by using range(n) that will create a list [0, 1, 2, ..., n-1]

# In[ ]:

print range(5)


# range(n1, n2) will return a list from n1 to n2-1

# In[ ]:

print range(2, 9)


# range(n1, n2, incr) will return a list from n1 to n2-1 in steps of incr

# In[1]:

print range(2, 9, 3)
print range(-3, 3, 2)


# xrange creates an object with an iterator that returns the value on 
# demand. The demand is in the loop

# In[ ]:

print xrange(5)

for i in xrange(5):
    print i


# Loop control statements in Python:
# 
# 1) break - this statement terminates the loop and transfers the execution to the 
# statement after the loop.
# 
# 2) continue - suspends execution of remaining statements in the loop and goes 
# back to the next loop iteration.
# 
# 3) pass - does nothing, is used for syntax purpose, the control goes to the next line.

# In[ ]:

for n in range(22, 30):
    if n % 3 == 0:
        print n, 'is the first multiple of 3'
        break
    else:
        print n, 'is not a multiple of 3'


# In[2]:

for n in range(22, 30):
    if n % 4 == 0:
        print n, 'is a multiple of 4'
        continue
    print n, 'is not a multiple of 4'


# In[ ]:

for item in [1,2,3]:
    pass 
print item


# In[ ]:

some_list = [1, 3, 6, -2, 5, 8]
print some_list


# In[ ]:

for items in some_list:
    if items < 0:
        # we are iterating through some_list until we hit the first negative number
        print items
        break


# In[ ]:

'''
In-class activity: Ask the user to input a year and if the input is '2016' 
then print 'You are right.'
'''


# In[ ]:

'''
In-class activity: Create a list that starts with -10 and goes all the way 
up to 10. Then find:
1) all the multiples of 4
2) stop when you found the first multiple of 4
''' 


# In[ ]:

'''
while-loop

syntax

while (condition):
    statements
    
Note: The while loop will get executedonly when the condition is True.
'''


# In[ ]:

n = 5
while (n > 0):
    print n
    n -= 1


# In[ ]:

# Example of an infinite while-loop with a break statement inside the 
# if condition

n = 0
while True:
    if n == 4:
        print n
        break
    n += 1


# In[ ]:

n = 5
while False:
    if n == 4:
        print n
        break 
    n -= 1
    
# Why is this not working?


# In[ ]:

'''
In-class activity:
Write a code that will keep taking names from the user until the user 
decides to quit by entering q or Q. Also perform a check to see whether the 
user entered anything. If the user didn't enter anything, ask them to enter 
a name. 
'''


# In[ ]:



