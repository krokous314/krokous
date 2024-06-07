# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:47:20 2022

@author: Lenovo
"""



def polynom3(x,coeff):
    val=0
    for i in range(len(coeff)):
        val+=coeff[i]*(x**i)
        
    return val
print(polynom3(10,[1,2,3]))

def polynom(x,a=10,b=5):
    y=a*x+b*x^2
    return y
print("y je", polynom(x=10))#lepší

def polynom2(x,a=10,b=5):
    y=a*x+b*x^2
    print(y)
polynom(x=15)
print(5**3)