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
