# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:41:26 2023

@author: 63007
"""

from xml.etree import ElementTree as ET
import sys
import pandas as pd

import re

regex = re.compile(r"\{.*\}")

et = ET.parse('explanatorynote-01-00.xsd')
et_new = ET.parse('explanatorynote-01-03.xsd')

#print(et)
root = et.getroot()
path = [regex.sub('', root.tag)]
outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Child_count':len(root), 'Attr': [root.attrib]})

root_new = et_new.getroot()
path_new = [regex.sub('', root_new.tag)]
outDataSet_new = pd.DataFrame({'Path':[tuple(path_new)],'Text':root_new.text, 'Child_count':len(root_new), 'Attr': [root_new.attrib]})

def xmlTreeToDataFrame(tree, path, index=0, total=0):
    global outDataSet
    global regex
    #if index==0 :
        #bar.printProgressBar(index, total,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    for child in tree:
        index=index+1
        pathA = path.copy()
        pathA.append(regex.sub('',child.tag))
        #bar.printProgressBar(index, total,  prefix = 'Progress ('+str(index)+') :', suffix = 'Complete', length = 50)
        attr=[child.attrib]
        row=pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Child_count':len(child), 'Attr':attr})
        #print(row)
        outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True)
        if len(child)>0:
            xmlTreeToDataFrame(child, pathA, index, total)

def xmlTreeToDataFrame_new(tree, path, index=0, total=0):
    global outDataSet_new
    global regex
    #if index==0 :
        #bar.printProgressBar(index, total,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    for child in tree:
        index=index+1
        pathA = path.copy()
        pathA.append(regex.sub('',child.tag))
        #bar.printProgressBar(index, total,  prefix = 'Progress ('+str(index)+') :', suffix = 'Complete', length = 50)
        attr=[child.attrib]
        row=pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Child_count':len(child), 'Attr':attr})
        #print(row)
        outDataSet_new = pd.concat([outDataSet_new, row], axis=0, ignore_index=True)
        if len(child)>0:
            xmlTreeToDataFrame_new(child, pathA, index, total)

#xmlTreeToDataFrame(root, path,0, len(root.xpath(".//*")))
xmlTreeToDataFrame(root, path,0)
xmlTreeToDataFrame_new(root_new, path_new,0)
#print(outDataSet.head(10))
#outDataSet['Path'] = outDataSet.Path.transform(lambda k: frozenset(k.items()))
#outDataSet_new['Path'] = outDataSet_new.Path.transform(lambda k: frozenset(k.items()))
outDataSet['Attr'] = outDataSet.Attr.transform(lambda k: frozenset(k.items()))
outDataSet_new['Attr'] = outDataSet_new.Attr.transform(lambda k: frozenset(k.items()))

#print(outDataSet.head(10))

var3 = outDataSet.merge(outDataSet_new, on=['Path','Text','Attr'], how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

print(var3)
