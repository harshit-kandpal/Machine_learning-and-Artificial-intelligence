# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:37:47 2022

@author: Harshit kandpal
"""


"""
functions :- two types
            1: predefined functions
            2: user defined functions
            
            has
             1:functions with argument
             2:functions without argument
            
"""

def wel():
    print("imsec")
    
    
def add(a,b):
    print(a+b)
    
#add(4)    
    
wel()
wel()
add(4,5)



def SI(P,R,T):
    st = P*R*T
    print("SIMPLE INTREST IS : ",st/100)
    
SI(100,2,2)




def SI():
    pri = int(input("Enter Principle "))
    rate = int(input("Enter rate "))
    time = int(input("Enter time "))
    si = (pri*rate*time)/100
    
    print("SIMPLE INTREST IS : ",si)
        
SI()


def addition(a,b):
    return (a+b)

addition(4,5)+10



import math 
 
def root( a, b, c): 
    return(
           (-b + math.sqrt(abs( b * b - 4 * a * c )))/(2 * a),
           (-b -math.sqrt(abs( b * b - 4 * a * c )) )/(2 * a)) 
 
l = root(3,-5,2)
print(l)
print(type(l))




c= 8
a= 7

def add(a,b):
    print(a+b)
    print(a)
    global c
    c = c+6
    print(c)

add(5,6)
print(c)
