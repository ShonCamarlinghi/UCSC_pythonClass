
# coding: utf-8

# In this notebook we will discuss:
# 1. Functions
# 2. Arguments and outputs
# 3. default argument
# 4. keyword based arguments

# In[29]:

'''
Syntax for function
def name_of_the_function(list of arguments):
    statements that need to be executed
    return value

'''

def increment(a):
    b = a+1
    print 'the increment2 value is : %d' %b
    return b

print increment(20) # calling the function and passing a required argument.


# In[30]:

# Scope of variables that are is local to the function. 

'''
The variable b does not exist outside the function.  
So we will get NameError exception.
'''

def increment(a):
    b = a+1
    print 'the increment2 value is : %d' %b
    return b

print increment(20) # calling the function and passing a required argument. 
#print b


# In[31]:

# A function can take multiple inputs
def increment(a,incr):
    c = a+incr
    print 'The value of a is: %d' %a
    return c

print increment(3,10) # calling the function and passing two required arguments. 
# 10 will be assigned to a and 
# 3 will be assigned to incr. So these are called positional arguments.


# In[32]:

def increment(a,incr):
    c = a+incr
    return (c,a,incr)
    # returning multiple values as a tuple
print increment(10,3)


# In[33]:

# Specifying default values
def increment(a,incr=1):
    a = a+incr
    return a

print increment(3) # for this the incr will default to 1
print increment(3,4) 
# here the incr is assigned a value of 4 which overrides the default value


# In[34]:

def increment(a=4,incr1=1):
    print 'the value of a is :%d' %a
    a = a+incr1
    return a

print increment(a=6,incr1=2) # 2 keyword arguments


# In[35]:

print increment(incr1=2,a=3)
# Unlike positional arguments, order is not important for keyword arguments.


# In[36]:

print increment(10,incr1=5) # if you assign a value for a keyword argument 
# then other arguments to its right should also be assigned values.


# In[37]:

print increment(a=10,5) # This will generate a Syntax error


# In[38]:

print increment(5,incr1=2) 
# if you assign a value for a keyword argument 
# then other keyword arguments to its right should also be assigned values.


# In[39]:

print type(increment)
print increment


# Pass-by-value and pass-by-reference
# 
# http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

# In[40]:

def myfunc(a):# a is an int
    a = a*2
    print "a = ", a
    return a
b = 2
myfunc(b)
print "b = ", b


# In[41]:

def myfunc(a):# a is a TUPLE that is completely replaced
    a = (4, 5, 6,)
    print "a = ", a
    return a
b = (1,2,3)
myfunc(b)
print "b = ", b


# In[42]:

def myfunc(a):# a is a list that is completely replaced
    a = [4,5,6]
    print "a = ", a
    return a
b = [1,2,3]
myfunc(b)
print "b = ", b


# In[43]:

def myfunc(a):# a is a LIST that is modified inline
    a.append(4)
    print "a = ", a
    return a
b = [1,2,3]
myfunc(b)
print "b = ", b


# In[44]:

def myfunc(a):# a is a LIST that is modified inline
    a = a[:] 
    # Creating a deepcopy will solve the problem of pass by reference
    a.append(4)
    print "a = ", a
    return a
b = [1,2,3]
myfunc(b)
print "b = ", b


# In[ ]:

'''
Summary of pass-by-value and pass-by-reference
'''


# <img src="http://i.stack.imgur.com/hKDcu.png = 70*70">

# In[ ]:

'''
In-class activity

Create a function called squared which takes a list called mylist and 
returns another list where the elements are square of mylist. Also write 
another function that takes mylist and returns a dictionary where the key 
is the input and the value is the square of the input. 
'''
mylist = [2, -7, 10]


# In[45]:

# args and kwargs helps to supply variable number of arguments to a 
# function. Inside the function, args is of type tuple.
def take1(*args):
    print args, type(args)
    for i in args:
        print i
        
take1(-10)
take1(1,2,3)


# In[46]:

# kwargs is a dictionary, with the dictionary key being the variable 
# name and dictionary value is the value of that variable
def utake(**kwargs):
    print kwargs, type(kwargs)
    
utake(a = 'abe')
utake(a = 'abe', b ='cab')


# In[47]:

def ptab(**kwargs):
    # since kwargs is a dictionary, we can iterate using items() function. 
    for key, value in kwargs.items():
        print key, value

ptab(a = 7, b = -5, c = 3, d = -10)


# In[ ]:

'''
In-class activity: define a function that takes a word and prints 
characters from the word. Call the function and pass a word.
'''


# In[ ]:

'''
In-class activity: define a function that converts Fahrenheit into 
Celsius. The formula is C = (F - 32)*(5.0/9). Use sys in the code and 
pass the value when running the program from the command line 
(if Windows) or terminal (if MAC).
'''


# In[ ]:



