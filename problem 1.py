# -*- coding: utf-8 -*-
"""@author: bhuvi
"""

d=[]
g=set()
a=int(input())
for i in range(0,a):
    r=input()
    d.append(r)
    g.add(r)
    

print(len(g))


for i in d:
    c=d.count(i)
    if c>1:
        print(c,end=" ")
        d.remove(i)
        continue
    else:
        print(c,end=" ")
