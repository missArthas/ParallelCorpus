#coding=utf-8
from bs4 import BeautifulSoup
import os

homepath = '/Users/nali/github/ParallelCorpus/websites/'
webpath = homepath + 'www.edb.gov.hk/'
savepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/save/'
enpath = 'en/'
cnpath = 'sc/'

fileNum = '1.txt'

os.path.exists(webpath + enpath + 'index.html')


enfile = open(savepath + 'en/' + fileNum, 'w+')
cnfile = open(savepath + 'cn/' + fileNum, 'w+')


soup1 = BeautifulSoup(open(webpath + enpath + 'index.html'),'lxml')
print(soup1.title)
for string in soup1.body.stripped_strings:
    (string + '\n')
    print(repr(string))
enfile.close()

soup2 = BeautifulSoup(open(webpath + cnpath + 'index.html'),'lxml')
print(soup2.title)
for string in soup2.body.stripped_strings:
    cnfile.write(string + '\n')
    print(repr(string))
cnfile.close()
