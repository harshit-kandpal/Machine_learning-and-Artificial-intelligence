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

t1=(20,30,50)  # change 50 to 500 and append 600

temp_t = list(t1)
temp_t[2] = 500
temp_t.append(600)

t1 = tuple(temp_t)

print(t1)



#set
"""
  set
  --> non indexing
  --> non ordered
  --> no duplicate elements
  --> set can't be empty
  

"""
s = {5,5,6,7,8,9,0}
print(s)  #output: {0, 5, 6, 7, 8, 9}

s.add(77)
s.remove(5)
print(s)   #output: {0, 6, 7, 8, 9, 77}

#remove duplicate elements from tuple
t2=(2,2,2,3,34,4,45,5,56,6,6,4,4,4)

temp_t=set(t2)
t2=tuple(temp_t)

print(t2)  #output: (2, 3, 34, 4, 5, 6, 45, 56)


#dictionaries = {key,value}
"""
     values --> Can be repeated 
     key    --> Cannot be repeated
     
"""


d = {"india":"delhi",
     "delhi":"new-delhi",
     "punjab":"chandigarh",
     "kashmir":"srinagar",
     "kashmir":"jammu",
     "australia":"cannaberra"}


print(d)


#nested dictionarires

d1 = {1:{"name":"aman","contact":1245678,"lang":["c++","java"]},
      2:{"name":"baman","contact":998765,"lang":["java","python"]},
      3:{"name":"chaman","contact":567890,"lang":["da","ml"]},
      4:{"name":"dhaman","contact":987633,"lang":["java","r"]}}

print(d1)

#dictionaries operations 






#is operator and id(address)


a=5
b=5



print(a==b)
print(a is b)

x = [1,2,3]
y = [1,2,3]

print(id(a))
print(id(b))

print(x==y)
print(x is y)

print(id(x))
print(id(y))

t1 = (1,2,3)
t2 = (1,2,3)

print(t1==t2)
print(t1 is t2)

print(id(t1))
print(id(t2))
