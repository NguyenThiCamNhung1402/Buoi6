# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:22:18 2024

@author: Nguyễn Thị Cẩm Nhung 23712471 
"""

chuoi=("Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM")
s=chuoi.replace("P. ","").replace("Q. ","").replace("Tp. ","").split(", ")
for ketqua in s:
    print(ketqua)
    