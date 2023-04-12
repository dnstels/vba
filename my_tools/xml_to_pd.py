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

et = ET.parse('Data.xml')

et = ET.fromstring(xml_test_str2)

if type(et) is ET.ElementTree:
    root = et.getroot()
else:
    root=et

path = [root.tag]
outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Attr': [root.attrib]})
print(type(root.attrib))

def xmlTreeToDataFrame(tree, path):
    global outDataSet
    for child in tree:
        pathA = path.copy()
        pathA.append(child.tag)
        attr=[child.attrib]
        outDataSet = pd.concat([outDataSet, pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Attr':attr})], axis=0, ignore_index=True)
        if len(child)>0:
            xmlTreeToDataFrame(child, pathA)

xmlTreeToDataFrame(root, path)
#print(outDataSet)

var1=outDataSet.groupby('Path')["Path"].count()
print(var1)
