# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:37:48 2024

@author: Nguyễn Thị Cẩm Nhung 23712471 
"""
c=("i'm a cat")
c1=c.title()
print(c1)
print(c.upper())
print( c[0].upper() + c[1:])
moi = list(c)
moi[2]= moi[2].upper()
moi[7]= moi[7].upper()
moi[8]= moi[8].upper()
moi="".join(moi)
print(moi)

