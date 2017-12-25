#coding=utf-8
from bs4 import BeautifulSoup
import os
from com.missArthas.bs4.Html2Text import Html2Text

homepath = '/Users/nali/github/ParallelCorpus/websites/'
webpath = homepath + 'www.edb.gov.hk/'
savepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/save/'
enpath = webpath + 'en/' + 'index.html'
cnpath = webpath + 'sc/' + 'index.html'



html2Text = Html2Text()
strs = html2Text.html2Text(enpath, cnpath)
print(strs[1])