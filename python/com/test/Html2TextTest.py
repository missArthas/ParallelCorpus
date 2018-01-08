#coding=utf-8
from bs4 import BeautifulSoup
import os
from com.missArthas.bs4.Html2Text import Html2Text

homepath = '/Users/nali/github/ParallelCorpus/websites/'
webpath = homepath + 'www.edb.gov.hk/'
savepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/save/'
enpath = webpath + 'en/' + 'index.html'
cnpath = webpath + 'sc/' + 'index.html'


ensoup = BeautifulSoup(open(enpath), 'lxml')
cnsoup = BeautifulSoup(open(cnpath), 'lxml')

html2Text = Html2Text()
strs = html2Text.html2Text(ensoup, cnsoup)
print(strs[1])

fileNum = '2.txt'

enfile = open(savepath + 'en/' + fileNum, 'w+')
cnfile = open(savepath + 'cn/' + fileNum, 'w+')

enfile.write(strs[0])
enfile.close()
cnfile.write(strs[1])
cnfile.close()