# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:20:58 2023

@author: User
"""

# =============================================================================
# import xml.dom.minidom as mindom
# from xml.dom.minidom import Node
# 
# # Загрузка xml-файла
# dom_min=mindom.parse('Data.xml')
# 
# root=dom_min
# # Получаем тег корневого элемента
# root_tag = root.documentElement.tagName
# =============================================================================


from xml.etree import ElementTree as ET
import sys
import pandas as pd

import console_process_bar1 as bar

xml_test_str2=u'''
<CAT>
  <NAME>Izzy</NAME>
  <BREED>Siamese</BREED>
  <AGE>6</AGE>
  <ALTERED>yes</ALTERED>
  <DECLAWED>no</DECLAWED>
  <LICENSE>Izz138bod</LICENSE>
  <OWNER>Colin Wilcox</OWNER>
</CAT>
'''

et = ET.parse('test_exp.xml')

#et = ET.fromstring(xml_test_str2)

if type(et) is ET.ElementTree:
    root = et.getroot()
else:
    root=et

#print(type(root.attrib))
from lxml import etree
doc = etree.parse("test_exp.xml")
root = doc.getroot()

# =============================================================================
# nodes = root.xpath(".//*")
# Total=len(nodes)
# for node in nodes:
#     print(node.tag)
# =============================================================================

def xmlTreeToDataFrame(tree, path, index=0, total=0):
    global outDataSet
    if index==0 :
        bar.printProgressBar(index, total,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    for child in tree:
        index=index+1
        pathA = path.copy()
        pathA.append(child.tag)
        bar.printProgressBar(index, total,  prefix = 'Progress ('+str(index)+') :', suffix = 'Complete', length = 50)
        attr=[child.attrib]
        row=pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Child_count':len(child), 'Attr':attr})
        #print(row)
        outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True)
        if len(child)>0 and index<100:
            len(child)
            xmlTreeToDataFrame(child, pathA, index, total)
            pass


path = [root.tag]
outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Child_count':len(root), 'Attr': [root.attrib]})
# =============================================================================
#
# xmlTreeToDataFrame(root, path,0, len(root.xpath(".//*")))
# print(outDataSet)
#
# var1=outDataSet.groupby('Path')["Path"].count()
# print(var1)
#
# =============================================================================
#print(root.xpath('/'+root.tag))

tree = etree.ElementTree(root)
arr=list(root.xpath(".//*"))#[:10000]
total=len(root.xpath(".//*"))
total=len(arr)
#for i,e in enumerate(root.iter()[:1000]):
for i,e in enumerate(arr):
    #print(i,tree.getpath(e), e.tag)
    bar.printProgressBar(i, total,  prefix = f'Progress ({i}/{total}) :', suffix = 'Complete', length = 50)
    attr=[e.attrib]
    row=pd.DataFrame({'Path':tree.getpath(e), 'Text':e.text, 'Child_count':len(e), 'Attr':attr})
    outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True)

print(outDataSet)
var1=outDataSet.groupby('Path')["Path"].count()
print(var1)




