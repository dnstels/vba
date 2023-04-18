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
#path = [regex.sub('', root.tag)]
path = regex.sub('', root.tag)
#outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Child_count':len(root), 'Attr': [root.attrib]})
#outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Attr': [root.attrib]})

root_new = et_new.getroot()
path_new = regex.sub('', root_new.tag)
#outDataSet_new = pd.DataFrame({'Path':[tuple(path_new)],'Text':root_new.text, 'Child_count':len(root_new), 'Attr': [root_new.attrib]})
#outDataSet_new = pd.DataFrame({'Path':[tuple(path_new)],'Text':root_new.text, 'Attr': [root_new.attrib]})

def xmlTreeToDataFrame(tree, path, names, index=0, total=0):
    #outDataSet = pd.DataFrame({'Path':[tuple(path)],'Text':root.text, 'Attr': [root.attrib]})
    if index>0:
        outDataSet = pd.DataFrame()
    else:
        outDataSet = pd.DataFrame({'Path':f'/{path}','Text':root.text, 'Attr': [root.attrib]})
    global regex
    #if index==0 :
        #bar.printProgressBar(index, total,  prefix = 'Progress:', suffix = 'Complete', length = 50)
    for child in tree:
        index=index+1
        #pathA = path.copy()
        #pathA.append(regex.sub('',child.tag))
        attr=[child.attrib]
        suff=''
        namesA = names.copy()
        isName=False
        if 'name' in attr[0]:
            isName=True
            name=attr[0]['name']
            namesA.append(name)
            suff=f'({name})'
        #attrName=attr['name']
        #suff=f'{attr["name"]}'
        pathB=regex.sub('',child.tag)
        pathA=f'{path}/{pathB}{suff}'

        #bar.printProgressBar(index, total,  prefix = 'Progress ('+str(index)+') :', suffix = 'Complete', length = 50)
        #row=pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Child_count':len(child), 'Attr':attr})
        #row=pd.DataFrame({'Path':[tuple(pathA)], 'Text':child.text, 'Attr':attr})
        row=pd.DataFrame({'Path':f'/{pathA}', 'Names':[tuple(namesA)], 'IsName':isName, 'Text':child.text, 'Attr':attr})
        #print(row)
        outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True, sort=False)
        if len(child)>0:
            outDataSet=pd.concat([outDataSet,xmlTreeToDataFrame(child, pathA, namesA, index, total)], ignore_index=True, sort=False)
    return outDataSet


#xmlTreeToDataFrame(root, path,0, len(root.xpath(".//*")))
outDataSet=xmlTreeToDataFrame(root, path,names=list())
outDataSet_new=xmlTreeToDataFrame(root_new, path_new,names=list())
#print(outDataSet.head(10))

outDataSet['Attr'] = outDataSet.Attr.transform(lambda k: frozenset(k.items()))
outDataSet_new['Attr'] = outDataSet_new.Attr.transform(lambda k: frozenset(k.items()))

#print(outDataSet.head(10))

compareDataSet = outDataSet.merge(outDataSet_new, on=['Path'], how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

#print(var3)

def deleteRows_z(dataSet, nameColumn, subString):
    dataSet=deleteRows(dataSet, f'{nameColumn}_x', subString)
    return deleteRows(dataSet, f'{nameColumn}_y', subString)

def deleteRows(dataSet, nameColumn, subString):
    return dataSet.loc[~dataSet[f'{nameColumn}'].str.contains(subString,na=False)]

var4=deleteRows(compareDataSet, 'Path', 'documentation')
var4=deleteRows(var4, 'Path', 'annotation')

var4=var4.sort_values(by=['Path'], ascending=True)



