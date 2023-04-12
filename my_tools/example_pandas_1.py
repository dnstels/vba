# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:26:24 2023

@author: 63007
"""
import pandas as pd
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([6, 15, 24])

var1=pd.DataFrame(dict(a=a.tolist(), b=b)).T
var2=pd.DataFrame({'c':['a','b','c']})
print(var1, var2.T, sep='\n')

var3=var1.append(var2.T)

print(var3)


var4=pd.DataFrame({'Tags':[('t1','t2'),('t3','t2')],'Atrebutes':[('t1','t2','t3','t2'),()]})

print(var4)
