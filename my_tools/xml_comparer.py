import sys
import pandas as pd
import re

from lxml import etree
import console_process_bar1 as bar

# Отключение предупреждения
pd.options.mode.chained_assignment = None  # default='warn'

# doc = etree.parse("test_exp.xml")
doc = etree.parse("Data.xml")
doc2 = etree.parse("Data2.xml")


def doc_to_DataFrame(doc):
    root = doc.getroot()
    regex = re.compile(r"\[\d+\]")
    tree = etree.ElementTree(root)
    path = tree.getpath(root)
    outDataSet = pd.DataFrame(
        {'Path': path, 'Path*': regex.sub('', path), 'Text': root.text, 'Child_count': len(root),
         'Attr': [dict(root.attrib)]})
    arr = list(root.xpath(".//*"))
    # total = len(arr)
    for i, e in enumerate(arr):
        # bar.printProgressBar(i, total, prefix=f'Progress ({i}/{total}) :', suffix='Complete', length=50)
        attr = [dict(e.attrib)]
        path = tree.getpath(e)
        row = pd.DataFrame(
            {'Path': path, 'Path*': regex.sub('', path), 'Text': e.text, 'Child_count': len(e), 'Attr': attr})
        outDataSet = pd.concat([outDataSet, row], axis=0, ignore_index=True)
    return outDataSet


outDataSet = doc_to_DataFrame(doc)
outDataSet1 = doc_to_DataFrame(doc2)
outDataSet['Attr'] = outDataSet.Attr.transform(lambda k: frozenset(k.items()))
outDataSet1['Attr'] = outDataSet1.Attr.transform(lambda k: frozenset(k.items()))

# print(outDataSet)
var1 = outDataSet.groupby('Path*')["Path*"].count().sort_values(ascending=False)

# print('=' * 50)
# print(pd.DataFrame({'Path*': var1.index, 'count': var1.values}).head(10))
#
print(outDataSet.head(10))

# Производим сравнение
#var3 = outDataSet.merge(outDataSet1, on=['Path*','Text','Attr'] ,how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

var3 = outDataSet.merge(outDataSet1, how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

for i in var3['Attr'].index:
    print(i, var3['Attr'][i])
    var3['Attr'][i] = {s[0]: s[1] for s in var3['Attr'][i]}

for i in var3['Attr'].index:
    print()
    for key in var3['Attr'][i]:
        print(key, var3['Attr'][i][key])
