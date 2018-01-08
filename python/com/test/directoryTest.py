# -*- coding: utf-8 -*-
# coding=utf-8
import os

import chardet
from bs4 import BeautifulSoup
from com.missArthas.bs4.Html2Text import Html2Text

enFlagList = ['/en/', '/eng/', '/english/', '/en-us/']
cnFlagList = ['/zh/', '/zh-cn/', '/ch/', '/chi/', '/sc/', '/schi/', '/han/', '/utf-8']

def SlashPathSearch(directory, web, enFlag, cnFlag):
    encodingList = ["utf-8", "gb2312", "gbk"]

    fileNum = 10
    assert os.path.isdir(directory),'make sure directory argument should be a directory'
    savepath = '/Users/nali/github/ParallelCorpus/texts/' + web
    result = []
    count = 0
    total = 0
    html2Text = Html2Text()
    for root,dirs,files in os.walk(directory, topdown=True):
        for fl in files:
            cnpath = root + "/" + fl
            enpath =""
            if cnpath.find(cnFlag) != -1:
                enpath = cnpath.replace(cnFlag, enFlag)
            total += 1
            if os.path.exists(enpath) and os.path.isfile(enpath):
                encodingFlag = False
                print(enpath)
                print(cnpath)
                print("\n")

                with open(enpath, "rb") as f:
                    data = f.read()
                    print(chardet.detect(data)['encoding'].lower())
                    print("\n")
                    if chardet.detect(data)['encoding'].lower() in encodingList:
                        print("encoding is ok!\n")
                        encodingFlag = True
                    else:
                        print("encoding is error!\n")
                        encodingFlag = False
                if encodingFlag == True:
                    count += 1
                    ensoup = BeautifulSoup(open(enpath), 'lxml')
                    cnsoup = BeautifulSoup(open(cnpath), 'lxml')
                    strs = html2Text.html2Text(ensoup, cnsoup)

                    fileNum = web + '.' + str(count) + '.txt'
                    print(fileNum)

                    if not os.path.exists(savepath + enFlag):
                        os.mkdir(savepath + enFlag)
                    if not os.path.exists(savepath + cnFlag):
                        os.mkdir(savepath + cnFlag)

                    enfile = open(savepath + enFlag + fileNum, 'w+')
                    cnfile = open(savepath + cnFlag + fileNum, 'w+')

                    enfile.write(strs[0])
                    enfile.close()
                    cnfile.write(strs[1])
                    cnfile.close()

            os.path.join(root, fl)

            #result.append(os.path.join(root,fl) + '\n')
    print("总数目", total)
    print("互译对", count)

    return result

# filepath = '/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk/'
# pathDir = os.listdir(filepath)
# IterateFiles(filepath, 'www.edb.gov.hk', '/eng/', '/tc/')


basepath = '/Users/nali/github/ParallelCorpus/websites/'
path = os.listdir(basepath)

for dir in path:
    if os.path.isdir(basepath + dir): #判断是否为文件夹，如果是输出所有文件就改成： os.path.isfile(p)
        filepath = basepath + dir
        print(filepath)

        pathDir = os.listdir(filepath)
        for enFlag in enFlagList:
            for cnFlag in cnFlagList:
                SlashPathSearch(filepath, dir, enFlag, cnFlag)



