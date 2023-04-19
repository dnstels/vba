# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:37:35 2023

@author: 63007
"""
import pandas as pd
#import re


def xmlTreeToDataFrame(tree, path, regex, names, index=0, total=0):
    if index>0:
        outDataSet = pd.DataFrame()
    else:
        outDataSet = pd.DataFrame({'Path':f'/{path}','Text':tree.text, 'Attr': [tree.attrib]})
    for child in tree:
        index=index+1
        attr=[child.attrib]
        suff=''
        namesA = names.copy()
        isName=False
        if 'name' in attr[0]:
            isName=True
            name=attr[0]['name']
            namesA.append(name)
            suff=f'({name})'
        pathB=regex.sub('',child.tag)
        pathA=f'{path}/{pathB}{suff}'

        row=pd.DataFrame({'Path':f'/{pathA}', 'Names':[tuple(namesA)], 'IsName':isName, 'Text':child.text, 'Attr':attr})
        outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True, sort=False)
        if len(child)>0:
            outDataSet=pd.concat([outDataSet,xmlTreeToDataFrame(child, pathA, regex, namesA, index, total)], ignore_index=True, sort=False)
    return outDataSet

def frozeset(column):
    return column.transform(lambda k: frozenset(k.items()))

def unFrozeset(froze):
    unfroze=[]
    for s in froze:
        if type(s) is float or len(s)<1:
            unfroze.append(dict())
            continue
        d={}
        for x in s:
            d[x[0]]=x[1]
        unfroze.append(d)
    return unfroze

def deleteRows_z(dataSet, nameColumn, subString):
    dataSet=deleteRows(dataSet, f'{nameColumn}_x', subString)
    return deleteRows(dataSet, f'{nameColumn}_y', subString)

def deleteRows(dataSet, nameColumn, subString):
    return dataSet.loc[~dataSet[f'{nameColumn}'].str.contains(subString,na=False)]
