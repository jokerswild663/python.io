import orderText
import sys
import pandas as pd

#printing package info
print(sys.version)
pd.show_versions(as_json=False)

#test run of orderText Module
unique_list=orderText.removeDuplicates(['first.xml','first.xml','second.xml','second.xml','third.xml'])
print(unique_list)
orderText.readText('sample.txt')
