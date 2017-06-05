# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:44:14 2017

@author: zhous
"""

import numpy as np              #导入numpy库
from scipy import interpolate   #导入scipy库
import matplotlib.pyplot as plt   #导入matplotlib库
x=np.linspace(0,10,11)
#[0,10]取11个数
#x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]  
y=np.sin(x)  
x2=np.linspace(0,10,110)
#[0,10]取 110个数 作为插值的x值

fig=plt.figure()
fig2 = plt.gcf()
fig2.set_size_inches(18.5, 10.5)
#画布的大小，并保存

kind=['nearest','zero','slinear','quadratic','cubic']
    #插值方式  
    #'nearest','zero'为0阶样条插值 ，'
    #slinear' 线性插值 相当于1阶样条插值 
    #'quadratic'为2阶样条插值
    #'cubic'3阶样条插值 
color=['r','b','c','g','m','k'] #线条颜色

for i in range(5):
    axi=fig.add_subplot(3,2,i+1)
    gi=interpolate.interp1d(x,y,kind=kind[i]) #调用函数
    yi=gi(x2)
    plt.plot(x,y,color[i]) 
    plt.plot(x2,yi,color[i+1],label=kind[i]) 
    plt.legend(loc="lower right") 
fig2.savefig('I:/tu/1.jpg', dpi=200)
    
fig=plt.figure()
fig3= plt.gcf()
fig3.set_size_inches(18.5, 10.5)

for j in["nearest","zero","slinear","quadratic","cubic"]:
    g=interpolate.interp1d(x,y,kind=j) 
    y0=g(x2)
    plt.plot(x2,y0,label=str(j))
fig3.savefig('I:/tu/2.jpg', dpi=120)
plt.legend(loc="lower right") 
plt.show() 
