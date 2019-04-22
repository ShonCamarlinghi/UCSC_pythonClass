
# coding: utf-8

# In this notebook we will discuss Python data structures:
# 
# 1. List
# 
# 2. Dictionary
# 
# 3. tuples
# 
# 4. sets
# 
# 5. slicing lists and tuples
# 
# 6. List comprehension
# 
# 7. Dictionary comprehension 
# 
# https://docs.python.org/2/tutorial/datastructures.html

# # List
# 
# A list is a collection of items separated by commas. 
# 
# Syntax for list is n = [item1, item2, item3].  The items can be any 
# Python object. The index of the list starts from zero.

# In[2]:

fruits = ['apple', 'grapes', 'peach']

print fruits


# In[4]:

# Syntax of the for statement
# for each_item in something:
#     execute statement(s) that are under this block
for f in fruits:
    print( 'we are printing one element at a time: ', f )


# Function and methods that can be applied to lists
# 
# len(A):           returns the number of items in A
#     
# A.insert(i,x1):   inserts x1 at index i
#     
# A.pop(i1):        removes item at index value i1 from A
#     
# A.remove(x3):     removes x3 from A
#     
# A.append(x4):     adds x4 to the end of A
#     
# A.extend(L):      appends items from L to the end of A
#     
# A.count(x):       returns the frequency of occurence of x in A
#     
# A.sort():         sorts the items in the list in ascending order, 
#                   A.sort(reverse=Ture) will sort the list in descending 
#                   order
# 
# A.index(x5):      returns the index corresponding to item x5
#     
# A.reverse():      reverses the items in A in place
# 

# In[ ]:

# len(listA) will return the number of elements in the list 'listA'
print len(fruits)


# In[ ]:

# here we want to loop through the elements in fruits and get the index value 
# and the element at that index
for i in range(len(fruits)):
    print i,fruits[i]


# In[5]:

mylist = [1,2,"CA",[3,4]]  
# mylist is a collection of numbers, string and a list
print mylist


# In[ ]:

# Accessing elements from a list
# mylist[n] will return element at nth index in mylist
print mylist[0] # this returns the first element in mylist


# Elements in a list can be accessed from left to right with indicies starting from 
# 0 (0 indicates the first position in the list) and going up
# 
# elements in a list can be accessed from right to left with indicies starting from 
# -1 (-1 indiciates the last position in the list) and going down

# In[ ]:

# this returns the last but one element in mylist
print mylist[-2] 


# In[ ]:

print mylist[-1][-2] 


# In[ ]:

# mylist[a:b] will return elements with index starting from a up to b-1. 
# This process is called Slicing
print mylist[0:2]


# In[ ]:

print mylist[-1][1] # this is used to get elements from a list of list


# In[ ]:

# append() will add a value to the end of the list
# current_list.append(x1) will add x1 to the end of current_list
mylist.append(3.14) 
print mylist


# In[9]:

# pop() removes an element at the given index
print mylist.pop(2)
print mylist


# In[ ]:

# Insert adds an element at the given index
mylist.insert(2,"MN")
print mylist


# In[ ]:

print mylist[1]


# sort() sorts elements in place, that means sorted elements are stored 
# back in the orginal list.

# In[ ]:

mylist = ['couple','3','3a',1,5,2,2.4,'c','0'] # note '3' is a string
a = mylist.sort()
print a 
print mylist 


# A simple ascending sort can be done using sorted(listname)
# sorted() is not in place.

# In[ ]:

mylist = ['couple','3','3a',1,5,2,2.4,'c','0'] # note '3' is a string
a = sorted(mylist) 
print a 
print mylist 


# sort() function will sort the list in ascending order. 
# If reverse = True is specified then it will sort the list in 
# descending order

# In[ ]:

mylist.sort(reverse=True)
print mylist


# For list of lists, sort command sorts the lists with respect to the first 
# element in the lists.

# In[ ]:

a = [[10,3],[5,2]]
a.sort()
print a


# In[ ]:

b = [['q', 'a'], ['dog','cat']]
b.sort()
print b


# count will return the frequency of occurance of a particular value 
# in the list.

# In[ ]:

mylist = [2,3,2,5,6,6,6]
mylist.count(3) 
m = ['apple', 'cat', 'cat', 'sat']
m.count('cat')


# In[ ]:

# EXTEND METHOD
mylist = [1,2,3]
newl = [4,5,6]
#mylist.append(newl)
mylist.extend(newl)
print mylist


# len(list1) will return the number of items in list1.

# In[ ]:

mylist = [1,2,3]
bylist = mylist
mylist.extend([4,5,6])
print mylist
print bylist
#print "mylist after extend: ", mylist
#print "length of mylist: ", len(mylist)
#print "bylist: ", bylist


# In[ ]:

mylist = [1,2,3]
mylist_copy = mylist
print mylist
print mylist_copy
mylist_copy.append([4,5,6])
print mylist, len(mylist)
print mylist_copy, len(mylist_copy)


# Note 1: mylist.append([4,5,6]) will add this list to the end of mylist. 
# Whereas mylist.extend([4,5,6]) will add values 4, 5 and 6 to mylist.
# 
# Note 2: mylist_copy1 is a copy of mylist. Any changes to mylist_copy1 
# will also affect mylist because the copy we made is a shallow copy.

# Deep Copy
# 
# A deep copy of a list can be done by using slicing [:].

# In[ ]:

mylist = [5,9,3]
mylist_copy2 = mylist[:]
mylist_copy2.append([11,2,3])
mylist.sort()
#mylist_copy2.sort()
print mylist
print mylist_copy2
#print "mylist after append", mylist_copy2
#print mylist, len(mylist)


# Note: mylist_copy2 is a deep copy of mylist so any changes to mylist_copy2 
# will not affect mylist and vice versa.

# #### LIST COMPREHENSION

# In[ ]:

# traditional method
squares = []
for x in range(10):
    squares.append(x**2)
print squares


# In[ ]:

# smart method using list comprehension
squares = [x**2 for x in range(10)]
print squares


# In[1]:

# an elaborate example of list comprehension which combines two lists and returns a list of tuples
combined = [(x, y) for x in [1, 2, 3, 4] for y in [3, 1, 4] if x%2 and x>y]
print combined


# ## Tuple
# 
# Tuple is a collection of immutable Python elements. That means we cannot 
# delete, add or modify elements in a tuple. The syntax for a tuple is 
# a = (item1, item2, item3,).  

# In[ ]:

T1 = 1,2,'String'
# Here Python will automatically assumes T1 is a tuple
print T1


# In[ ]:

emptyTuple = ()
print emptyTuple


# In[ ]:

T2 = (1,)
# without the comma, T2 will be of type integer and not tuple
print T2, type(T2)


# In[ ]:

T2 = T2+1 # Not allowed, as tuple cannot be modified
print T2, type(T2)


# In[ ]:

T3 = T1,T2 # T3 is a tuple of tuples
print T3
print T3[0]
print T3[0][1] 
# 0 index indicates the first tuple and 1 index indicates the 
# second element in the first tuple


# In[ ]:

T3[0][0]=2 # New values cannot be assigned


# In[ ]:

t  = (1,2,3)
print t,type(t)
l = list(t)
print l,type(l)
t2 = tuple(l)
print t2, type(t2)


# In[ ]:

B = (1,) # B is a tuple with one element
B = (1,2,) # a new tuple named B is created which has two elements
B = () # a new tuple named B is created with no elements
print B


# In[ ]:

A = (2,4,5,8,10,11)
B = ('CA', 'MN', 'TX')
C = A + B # + operation concatenates the tuples
print C


# In[ ]:

# Basic tuple operations
print len(A) 
print max(B)
print min(B)


# In[ ]:

# Basic tuple operations
H = ('Hello',)
print H*4 # * means repetition


# In[ ]:

'''
Inclass activity: Consider the tuple t1 = (2,4,8). 
1. Try to modify the first element of the tuple to 5. 
2. Convert the tuple into a list and append the number 5 to the list
3. Use extend to add [1,4,5] to the list
4. Pop the third item from the list and then print the list.
5. Convert it back into a tuple. 
'''


# ## Dictionary 
# 
# Dictionary is a collection of key-value pairs. 
# 
# Unlike sequences, which are indexed by a range of numbers, dictionaries are 
# indexed by keys, which can be any immutable type; strings and numbers can 
# always be keys. Tuples can be used as keys if they contain only strings, 
# numbers, or tuples.
# 
# https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences

# 
# Syntax for dictionary
# 
# ```
# D1 = {key1:value1, key2:value2}
# ```
# 

# In[ ]:

# A simple dicitonary
d1 = {26:'z', 24:'x'}
print d1


# In[ ]:

ziploc = {} # ziploc is an empty dictionary
print ziploc


# In[ ]:

print ziploc['95117']
ziploc['95117'] = 'Santa Clara'
print ziploc['95117']
ziploc['95054'] = 'Santa Clara'
print ziploc


# In[ ]:

'''
In this example for the key 95117, the value is San Jose, 
for the key 94086, the value is Sunnyvale etc.
'''

ziploc = {'95117': 'San Jose','94086':'Sunnyvale','95014': 'Cupertino'}
print ziploc
print ziploc.keys()
print tuple(ziploc.keys())
print ziploc.values()


# In[ ]:

for keys in ziploc: 
    print keys,ziploc[keys]


# In[ ]:

for keys,value in ziploc.iteritems(): # Use .items() for version 3.0+
    print keys,value


# In[ ]:

print ziploc['55421'] 
# This is not allowed, as the dictionary does not have key 55421


# In[ ]:

exists = False
for k,v in ziploc.iteritems():
    if k == '95117':
        exists = True
        break
print exists


# In[ ]:

print '55421' in ziploc


# In[ ]:

print ziploc.items() # dictname.items() returns a list of (key,value) tuple pairs


# In[ ]:

ziploc.clear() # removes all the elements of the dictionary
print ziploc


# In[ ]:

# Dictionary comprehension 
squared = {x: x**2 for x in range(5)}
print squared


# In[ ]:

d = dict(a=1, b=2, e=1, d=2, c=1, g=2, f=3)
print d


# In[ ]:

for items in d.iteritems():
    print items


# In[ ]:

'''
In-class activity: Create a dictionary with five key-value pairs, 
state as the key and it's capital city as the value. 
'''


# In[ ]:

'''
In-class activity: Create a dictionary with five key-value pairs, state 
as the key and it's capital city and the capital city's current 
temperature as the value using tuples or lists. 
'''


# # Set
# 
# A set is an unordered collection of unique items.

# In[ ]:

vegetables = ['tomatoes','eggplant','cauliflower','eggplant'] # A list
vegetables_set = set(vegetables)
# set command returns only unique items
print vegetables,vegetables_set


# In[ ]:

a = list(vegetables_set)
# vegetables_set[0] # Not allowed as set cannot be indexed. 
# You can iterate through them.
print a[0]


# In[ ]:

for items in vegetables:
    print items 


# In[ ]:

for items in vegetables_set:
    print items 


# In[ ]:

print 'Cauliflower' in vegetables_set 
# the above statement checks whether Cucumber is in vegetables_set


# In[ ]:

finallistofveg = list(vegetables_set)
print finallistofveg


# In[ ]:

a = [1,1,4,5,7]
print type(a), a
b = set(a)
c = list(b)
print c

print list(set(a))


# From https://docs.python.org/2/library/sets.html, you can obtain a list 
# of all operators that can be applied to sets
# 
# len(s):                           cardinality of set s
# 
# x in s:                           tests x for membership in s
# 
# x not in s:                       tests x for non-membership in s
# 
# s.issubset(t): <=     t:          test whether every element in s is in t
# 
# s.issuperset(t): s >= t:          test whether every element in t is in s
# 
# s.union(t): s | t :               new set with elements from both s and t
# 
# s.intersection(t): s & t:         new set with elements common to s and t
# 
# s.difference(t): s - t :          new set with elements in s but not in t
# 
# s.symmetric_difference(t): s ^ t: new set with elements in either 
#                                   s or t but not both
#                                   
# s.copy():                         new set with a shallow copy of s
# 
# s.update(t):                      will add elements from t to s
# 
# s.add(x1):                        will add x1 to s
# 
# s.remove(x2):                     will remove x2 from s
# 
# s.discard(x3):                    will discard x3 from s
# 
# s.pop():                          will arbitrarily remove an element from s
# 
# s.clear():                        will clear all elements in s

# In[ ]:

list1 = [1,2,3,45,76]
list2 = [5,12,45]
set1 = set(list1)
set2 = set(list2)
print set1, set2


# In[ ]:

print set1.union(set2)
print set1.intersection(set2)
print set1.difference(set2)
print 1 in set1 # Check if an element exists in a set using in keyword
print set1.issubset(set2) 


# In[ ]:

# update()
# current_set.update(another_set) function will update current_set with 
# elements in another_set
set1.update(set2)
print set1


# In[ ]:

# add()
# current_set.add(x1) will add x1 to current_set
set1.add(-11)
print set1


# In[ ]:

# remove()
# current_set.remove(x2) will remove x2 from current_set
set1.remove(2) 
print set1


# In[ ]:

# discard()
# current_set.discard(x3) will remove x3 from current_set
'''
A key difference between remove() and discard() is that if the element is 
not there then remove will raise an exception called 'KeyError' while discard() 
will silently fail
'''

set1.discard(3) 
print set1


# In[ ]:

# pop()
# current_set.pop() will arbitrarily removes an element from current_set
set1.pop() 
print set1


# In[ ]:

# clear()
# current_set.clear() will remove all the elements from current_set
set1.clear()
print(set1)


# In[ ]:

'''
In-class activity:
mylist = [2,3,2,5,6,6,6], create a dictionary with element in mylist as 
a key and its frequency of occurence as its value. Use set to accomplish 
this.
'''


# In[ ]:



