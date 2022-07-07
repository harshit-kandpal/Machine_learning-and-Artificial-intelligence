"""
Python 

 features 
 -->high level language
 -->user friendly
 -->
 -->


commands
 ctrl +   --> zoom in
 ctrl -   --> zoom out
 ctrl 1   --> comment
 f5       --> run code
 f9       --> run code specific line
 
Data types
 1. numeric
 2. text 
 3. boolean
 4. sequence
 5. mapping: dictionaries
 6. set{}
"""

a=5
b=6
c="hello"
d=7.5
print(a+b)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#list & tuple

"""
         | ordered   |        changable     |     duplicate items|
         |           |                      |                    |
list[]   |  yes      |         yes          |         yes        |
tuple()  |  yes      |         no           |         yes        |
set{}    |  no       |         yes          |         no         |
"""

#list
#  0 1 2 3 4   5    6     7
l=[2,3,4,6,78,"hi",5.7,"hello"]

#tuple
#    0 1 2 3 4 5 6 7  8 9 10 11 12  13
t = (3,4,5,6,6,7,8,88,7,6, 5, 4, 3, 22)


#ordered and duplicate checking
print(l)
print(t)

# changable list

print(l[5])
l[5] = "harshit"
print(l[5])
l.append("kandpal")
print(l)

#chnagable tuple
print(t[7])
# t[7]=57        Error: 'tuple' object does not support item assignment
# t.append(57)   Error: 'tuple' object has no attribute 'append'


# change element via typecasting to lists

t1=(20,30,50)  # change 









#set
"""
  set
  --> non indexing
  --> non ordered
  --> no duplicate elements
  --> set can't be empty
  

"""



