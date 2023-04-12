# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:36:43 2023

@author: 63007
"""

# =============================================================================
# import xml.dom.minidom
#
# dom = xml.dom.minidom.parse("Data.xml")
# dom.normalize()
#
# root_element=dom.documentElement
# print(root_element.nodeName)
#
# print(root_element.childNodes[0].nodeName)
# =============================================================================

# =============================================================================
# for child in dom.getElementsByTagName(root_element.nodeName):
#     print(child[0].firstChild.nodeValue)
#
# =============================================================================

from xml.etree import ElementTree as ET
import sys
import pandas as pd

# =============================================================================
# et = ET.parse ( "test_exp.xml" )
# print(sys.getsizeof(et))
# 
# root = et.getroot()
# print(sys.getsizeof(root))
# =============================================================================

test_str="""
<Document ProgramVersion="12.3.0.39351" Generator="GrandSmeta" DocumentType="{2B0470FD-477C-4359-9F34-EEBE36B7D340}" GrandSmetaSign="RHAAAAM7OziAiw+Dn7/Du7CDv8O7l6vLo8O7i4O3o5SLxaZI7QTRCNjNCRjUxOTIwOUNCNEFEOERBNzAwQTgwRkZGQTc=">
  <Properties LocNum="06-07-03-01" RegNum="10000038" Object="Установка канализационной насосной станции бытовых сточных вод" Constr="Магистральный газопровод Голубой поток - Россия - Турция (морской вариант). 3 этап. База Березанского ЛПУМГ в г. Тихорецке" Stage="Этап 3." Comment="Задание 3/0528/422 от 08.12.2022,18/0528/80 от 09.12.2022" Description="Строительные работы. Установка канализационной насосной станции бытовых сточных вод. Конструкции железобетонные"/>
  <GsDocSignatures>q1w2e3
  asdfasdfasdf
    <Item Caption="Основание" ID="100" Value="0528.001.П.3/0.0001-КР2.5(БЛЭС 608.2019.013-КЖ).ВР"/>
    <Item Caption="Журнал" ID="124">DAta</Item>
    <Item Caption="Шифр затрат" ID="121" Value="101"/>
    <Item Caption="Смета составлена в ценах по состоянию на:" ID="102" Value="01.01.2022"/>
    <Item Caption="Составил" ID="300" Value="Котова М.Г."/>
    <Item Caption="Проверил" ID="310" Value="Дорощенко Т.Н."/>
  </GsDocSignatures>
  <RegionalK Options="Percent Base"/>
</Document>
"""

root=ET.fromstring(test_str)
print(sys.getsizeof(root))


#print(root.tag)

def getChilds(root,ch,lvl):
    prefix=ch*(lvl+0)
    out_tags=[]
    for child in root:
        out_tags.append({child.tag:child.attrib})
        #print(prefix, child.tag, len(child), child.text if child.text != None else '')
        #print(' '*(lvl+0),child.attrib)
# =============================================================================
#         if(len(child)<1):
#             print(prefix, child.tag, len(child), child.text)
#             print(' '*(lvl+0),child.attrib)
#         else:
#             #print('------------>', child.tag, type(child[0]))
#             print(prefix,child.tag, len(child))#, child.text, child[0])
#             print(' '*(lvl+0), child.attrib)
# =============================================================================
        if lvl <2:
            #out_tags.append(getChilds(child,ch,lvl+1))
            pass
    return {root.tag: out_tags}


def getChilds_pd(tree):
    out_tags=[]
    for child in tree:
        out_tags.append((tree.tag,child.tag))
        if len(child)>0:
            out_tags.append(getChilds_pd(child))
    return out_tags

#print(getChilds(root,'~',1))
print(getChilds_pd(root))