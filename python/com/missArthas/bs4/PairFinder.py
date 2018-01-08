#coding=utf-8

import os
import chardet
from bs4 import BeautifulSoup
from com.missArthas.bs4.Html2Text import Html2Text

class PairFinder(object):
    '''
    URL模式的底表
    字符集底表
    '''
    enFlagList = ['en', 'eng', 'english', 'en-us']
    cnFlagList = ['zh', 'zh-cn', 'ch', 'chi', 'sc', 'schi', 'han', 'utf-8']

    enSlashList = ['/en/', '/eng/', '/english/', '/en-us/']
    cnSlashList = ['/zh/', '/zh-cn/', '/ch/', '/chi/', '/sc/', '/schi/', '/han/', '/utf-8/']

    encodingList = ["utf-8", "gb2312", "gbk"]

    basepath = '/Users/nali/github/ParallelCorpus'

    def __init__(self, path):
        self.basepath = path

    def slashPathSearch(self, directory, web, enFlag, cnFlag):
        savepath =  self.basepath + '/text/' + web

        result = []
        count = 0
        total = 0

        assert os.path.isdir(directory), 'make sure directory argument should be a directory'

        html2Text = Html2Text()

        #递归循环对目录下所有文件
        for root, dirs, files in os.walk(directory, topdown=True):
            for fl in files:
                cnpath = root + "/" + fl
                enpath = ""
                if cnpath.find(cnFlag) != -1:
                    enpath = cnpath.replace(cnFlag, enFlag)
                total += 1
                if os.path.exists(enpath) and os.path.isfile(enpath):
                    encodingFlag = False
                    print(enpath)
                    print(cnpath)
                    print("\n")

                    #确保文件的编码是["utf-8", "gb2312", "gbk"]
                    with open(enpath, "rb") as f:
                        data = f.read()
                        print(chardet.detect(data)['encoding'].lower())
                        print("\n")
                        if chardet.detect(data)['encoding'].lower() in self.encodingList:
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

                # result.append(os.path.join(root,fl) + '\n')
        print("总数目", total)
        print("互译对", count)

        return result

    def slashSearchAll(self, directory):
        #searchPath = self.basepath + '/websites/'
        searchPath = self.basepath + directory
        path = os.listdir(searchPath)

        for dir in path:
            if os.path.isdir(searchPath + dir):  # 判断是否为文件夹，如果是输出所有文件就改成： os.path.isfile(p)
                filepath = searchPath + dir
                print(filepath)

                pathDir = os.listdir(filepath)
                for enFlag in self.enFlagList:
                    for cnFlag in self.cnFlagList:
                        self.slashPathSearch(filepath, dir, enFlag, cnFlag)


    def languagePathSearch(self, directory, web, enFlag, cnFlag):
        savepath = self.basepath + web

        result = []
        count = 0
        total = 0

        assert os.path.isdir(directory), 'make sure directory argument should be a directory'

        html2Text = Html2Text()

        # 递归循环对目录下所有文件
        for root, dirs, files in os.walk(directory, topdown=True):
            for fl in files:
                cnpath = root + "/" + fl
                enpath = ""
                if cnpath.find(cnFlag) != -1:
                    enpath = cnpath.replace(cnFlag, enFlag)
                total += 1
                if os.path.exists(enpath) and os.path.isfile(enpath):
                    encodingFlag = False
                    print(enpath)
                    print(cnpath)
                    print("\n")

                    # 确保文件的编码是["utf-8", "gb2312", "gbk"]
                    with open(enpath, "rb") as f:
                        data = f.read()
                        print(chardet.detect(data)['encoding'].lower())
                        print("\n")
                        if chardet.detect(data)['encoding'].lower() in self.encodingList:
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

                # result.append(os.path.join(root,fl) + '\n')
        print("总数目", total)
        print("互译对", count)

        return result

    def languageSearchAll(self, directory):
        ''


pairFinder = PairFinder('/Users/nali/github/ParallelCorpus')
print(pairFinder.basepath)
