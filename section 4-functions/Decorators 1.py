
# coding: utf-8

# In Python, functions are first class objects. That means that functions can be around and used as arguments. A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. Decorators provide a simple syntax for calling higher-order functions.
# 
# References:
# 
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# 
# http://thecodeship.com/patterns/guide-to-python-function-decorators/

# In[1]:

# the function outer is the decorator
def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func() 
        return ret + 1
    return inner # we are returning inner function

def re_one():
    return 1

# First method to use a decorator
outer(re_one)() 
# outer is the decorator for re_one. Any calls to re_one won't get the 
# original re_one, instead will get the decorated version.


# In[2]:

# Second method to use a decorator
@outer
def re_two():
    return 1

re_two()


# In[ ]:

def checkage(func):
    def wrapper(a):
        if func(a) < 18:
            print "Not allowed"
        else:
            print "Allowed"
    return wrapper

def processdata(a):
    return a

checkage(processdata)(23)


# In[ ]:

def checkage(func):
    def wrapper(a):
        if func(a) < 18:
            print "Not allowed"
        else:
            print "Allowed"
    return wrapper

@checkage
def processdata(a):
    return a

processdata(12)


# In[3]:

import time
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def fun(n):
    a = [i*i for i in range(n)]
     
fun(1000000)


# In[ ]:



