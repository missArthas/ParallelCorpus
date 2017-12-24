#coding=utf-8
from bs4 import BeautifulSoup

basepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/'
soup1 = BeautifulSoup(open(basepath + 'sc/index.html'),'lxml')
print(soup1.title)
for string in soup1.body.stripped_strings:
    print(repr(string))

soup2 = BeautifulSoup(open(basepath + 'en/index.html'),'lxml')
print(soup2.title)
for string in soup2.body.stripped_strings:
    print(repr(string))