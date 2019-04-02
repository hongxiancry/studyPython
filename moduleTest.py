
#/Users/chairuiya/Documents/learn/studyPython
#_*_ utf-8 _*_
'MODULE TEST SCRIPT'
__author__='chairuiya'

import moduleScript1
import copy
import sys
import os

name = input("input your name!")
inputName = moduleScript1.greeting(name)
print(inputName)
print([n for n in dir(copy) if not n.startswith('_')])
print(copy.__all__)
help(copy.copy)
print(range.__doc__)
print(copy.__file__)

print(' '.join(reversed(sys.argv[1:])))

print([n for n in dir(os) if not n.startswith('_')])

print(os.__all__)

from heapq import *
import random
heap = []
data = []
for n in range(10):
	data.append(n)
print(data)
random.shuffle(data)
print(data)
for n in data:
	heappush(heap,n)
print(heap)
heappop(heap)
print(heap)

