# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:54:20 2022

@author: Harshit kandpal. 
@day - 2
"""

"""

"""

#basic code of conditional statements

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == "python" and password == "python22":
    print("login succesfully")
elif username == "python" and password != "python22":
    print("wrong password")
elif username != "python" and password == "python22": 
    print("wrong username")
else:
    print("wrong username and password")
    
    
    

"""
# billing program

    >3000 then bill will be : amount + 18%gst +1%st
    >2000 and <=3000 then bill : amount + 2%gst
    >1000 and <=2000 then bill : amount + 18%gst +3%st
    >500 and <=1000 then bill : amount + 4%gst
    >0 and <=500 then bill : amount + 18%gst +4.5%st
    
"""
 
amount = int(input("Enter the bill amount : "))
gst = (.18*amount)

if amount>3000:
   st = (0.01*amount) 
elif amount>2000 and amount<=3000:
   st = (0.02*amount)
elif amount>1000 and amount<=2000:
   st = (0.03*amount) 
elif amount>500 and amount<=1000:
   st = (0.04*amount) 
elif amount>0 and amount<=500:
   st = (0.045*amount)
   
print("amount : ",amount)
print("gst : ",gst)    
print("service tax : ",st) 
bill= amount + gst + st
print("your bill is : ",bill)



#nested if else

a = int(input("Enter the number"))

if a%2 == 0:
    if a>8:
        print("Greater")
    else:
        print("Lesser")
else:
    print("False")

"""
LOOP
  1: for
  2: while
"""


L = [1,3,34,5,65,2,2,23,54,45,23,2]

for i in L:
    print("hi")
    
    
for i in range(1,11,1):      #1 to 10
    print(i)
for i in range(1,11):        #1 to 10 cause base step is always 1 if not specified
    print(i)
    
    
"""
print
    
    3 odd
    6 even
    9 odd
    12 even
    15 odd
    18 even
    21 odd
    24 even
    27 odd
    30 even
"""
    
for i in range(3,31,3):
    if i%2 == 0:
        print(i, "even")
    else:
        print(i,"odd")
        
"""
print
    
    3 
    odd
    6 
    even
    9 
    odd
    12
    even
    15 
    odd
    18 
    even
    21 
    odd
    24 
    even
    27 
    odd
    30 
    even
    
"""

for i in range(3,31,3):
    print(i)
    if i%2 == 0:        
        print( "even")
    else:
        print("odd")
        
#PATTERNS
        
"""

*
**
***
****
*****

"""

n = int(input("enter"))
for i in range (0,n):
    for j in range (0,i+1):
        print('*' ,end = "")
    print()
    
    
"""

*****
****
***
**
*

"""

n = int(input("enter"))
for i in range (n,0,-1):
    for j in range (0,i):
        print('*' ,end = "")
    print()
