'''
Created on Jan 24, 2015

@author: SJS
'''
import sys

listevt = dict()
if()
listevt.append( ("2015", "toto"))
listevt.append( ("2016", "toto2"))
listevt.append( ("2017", "toto3"))
listevt.append( ("2018", "toto4"))

print(listevt.index("2015"))

listevt.append( ("2015", "totoD"))
print(listevt.index("2015"))
listevt.pop(listevt.index("2015"))
print(listevt.index("2015"))
