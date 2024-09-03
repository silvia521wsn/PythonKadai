"""
プログラム名:Kadai14-2.py
作成日:2024年09月03日
作成者:CD69-3組 K024C2100 WANG SHINING
"""
import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([10,20,30,40]) 
label = ['CD69-1','CD69-2','CD69-3','CD69-4']
plt.pie(x,labels=label)
plt.show()