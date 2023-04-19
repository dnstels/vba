# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:50:05 2023

@author: 63007
"""
from xml.etree import ElementTree as ET
#import pandas as pd
import re
from compare_tools import *

regex = re.compile(r"\{.*\}")

et_old = ET.parse('explanatorynote-01-00.xsd')
et_new = ET.parse('explanatorynote-01-03.xsd')


outDataSet_old=xmlTreeToDataFrame(et_old.getroot(), regex.sub('', et_old.getroot().tag), regex ,names=list())
outDataSet_new=xmlTreeToDataFrame(et_new.getroot(), regex.sub('', et_new.getroot().tag), regex ,names=list())

outDataSet_old['Attr']=frozeset(outDataSet_old['Attr'])
outDataSet_new['Attr']=frozeset(outDataSet_new['Attr'])

compareDataSet = outDataSet_old.merge(outDataSet_new, on='Path', how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

compareDataSet['Attr_x'] = unFrozeset(compareDataSet['Attr_x'])
#compareDataSet['Attr_y'] = unFrozeset(compareDataSet['Attr_y'])

var4=deleteRows(compareDataSet, 'Path', 'documentation')
var4=deleteRows(var4, 'Path', 'annotation')

var4=var4.sort_values(by=['Path'], ascending=True)

#attr_x=compareDataSet.loc[['name' in i for i in unFrozeset(compareDataSet['Attr_x'])]]
nameAttr_x=compareDataSet.loc[['name' in i for i in compareDataSet['Attr_x']]]
