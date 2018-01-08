#coding=utf-8
from bs4 import BeautifulSoup
import os
from com.missArthas.bs4.Html2Text import Html2Text

homepath = '/Users/nali/github/ParallelCorpus/websites/'
webpath = homepath + 'www.edb.gov.hk/'
savepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/save/'
enpath = webpath + 'en/' + 'index.html'
cnpath = webpath + 'sc/' + 'index.html'