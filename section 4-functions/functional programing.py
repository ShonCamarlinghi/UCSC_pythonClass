
# coding: utf-8

# In this notebook we will discuss:
#     
# filter()
# 
# map()
# 
# reduce()
# 
# lambda function

# filter() takes two inputs one is a function and other one is 
# iterable. filter returns a list of values that satisfies the condition, 
# in this case it returns all the values between 2 and 9 that 
# are NOT divisible by 2. 

# In[ ]:

# Get all odd numbers between 2 and 10
a = range(2, 10)
print a

def f(x): 
    return x % 2 != 0

b = filter(f, a) 
print b


# The lambda function, also known as anonymous function is used 
# when the function is a throw away function or is not used more than once. 
# 
# Syntax for lambda function:
# 
# lambda inputs : output
# 
# Let us consider an example
# 
# lambda x: x%2 !=0 
# 
# can be interpreted as follows:
# x to the left of the : is the argument to 
# the function. The expression x%2!=0 to the right of : is the 
# operation being performed inside the function and also the value 
# being returned by the function.

# In[ ]:

# Get all odd numbers between 2 and 10 using LAMBDA FUNCTIONS
a = range(2,10)
b = filter(lambda x : x%2!=0, a) 
print b


# map() takes a function and iterable(s). In this case one input is 
# the function and other input is the values. Map returns a list which is the output of the function. In this case it returns the squares of the values from 1 to 4. Map takes a set of values and returns another set of values based on the function.

# In[ ]:

def squared(x): 
    return x*x

print map(squared, range(1, 5)) 


# In[ ]:

'''
lambda function that is similar to the squared function 
'''
print map(lambda x:x*x, range(1, 5))


# In[ ]:

'''
You can also give a name to the lambda function. 
'''

lambdasq = lambda x:x*x
print map(lambdasq, range(1, 5))


# In[ ]:

a = [1,2,3]
b = [4,5,6]
def add(a1, b1): 
    return a1+b1
# here map takes two lists and adds them
print map(add,a,b)


# reduce() is used to shrink an iterable to a single value.

# In[ ]:

# Find the sum of all elements in a list
a = [1,2,5]
print reduce(lambda x,y: x+y, a)


# In[ ]:

a = [1,2,5]
print reduce(lambda x,y: x*y , a)

