#/usr/bin/env python
#coding:utf-8
#author:CanBing

import re

result = []
f = open("result.txt","r")
r = open("res.txt","a")

for i in f.readlines():
	result.append(i.strip())

print '--'*20
sets = {}.fromkeys(result).keys()
#sets2 = list(set(result))
for i in sets:
	r.write(i)
	r.write('\n')
#print '--'*20
#print sets2