#coding=utf-8

import os
import chardet
from bs4 import BeautifulSoup
import glob
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

    def slashPathSearch(self, readPath, savePath, enFlag, cnFlag, count):
        """
        :param readPath: /Users/nali/github/ParallelCorpus/websites/www.edb.edu.hk
        :param savePath: /Users/nali/github/ParallelCorpus/texts/www.edb.edu.hk
        :param enFlag:  en
        :param cnFlag: zh
        :return:
        """
        savepath =  savePath
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        directory = readPath

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
                if cnpath.find("/"+cnFlag+"/") != -1:
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
                        if chardet.detect(data)['encoding'] != None:
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

                        fileNum = str(count)
                        print(fileNum)

                        encnDir = savepath + "/"+ enFlag+";"+cnFlag+"/"
                        if not os.path.exists(encnDir):
                            os.mkdir(encnDir)

                        enfile = open(encnDir + fileNum+";"+enFlag+".txt", 'w+')
                        cnfile = open(encnDir + fileNum+";"+cnFlag+".txt", 'w+')

                        enfile.write(enpath + "\n")
                        enfile.write(strs[0])
                        enfile.close()

                        cnfile.write(cnpath + "\n")
                        cnfile.write(strs[1])
                        cnfile.close()

                os.path.join(root, fl)

                # result.append(os.path.join(root,fl) + '\n')
        print("总数目", total)
        print("互译对", count)

        return result

    def slashSearchAll(self, readPath, savePath):
        """
        :param readPath: /Users/nali/github/ParallelCorpus/websites/
        :param savePath: /Users/nali/github/ParallelCorpus/texts/
        :return:
        """
        searchPath = readPath
        webs= os.listdir(searchPath)

        for dir in webs:
            if os.path.isdir(searchPath + dir):  # 判断是否为文件夹，如果是输出所有文件就改成： os.path.isfile(p)
                filepath = searchPath + dir
                print(filepath)

                pathDir = os.listdir(filepath)
                for enFlag in self.enFlagList:
                    for cnFlag in self.cnFlagList:
                        self.slashPathSearch(searchPath + dir, savePath + dir, enFlag, cnFlag, 0)

    def languagePathSearch(self, readPath, savePath, enFlag, cnFlag):
        """
        :param readPath: /Users/nali/github/ParallelCorpus/websites/www.edb.edu.hk
        :param savePath: /Users/nali/github/ParallelCorpus/texts/www.edb.edu.hk
        :param enFlag:  lang=en
        :param cnFlag:  lang=cn
        :return:
        """
        savepath =  savePath
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        directory = readPath

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
                        if chardet.detect(data)['encoding'] != None:
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

                        fileNum = str(count)
                        print(fileNum)

                        # # if not os.path.exists(savepath + "/" + enFlag + "/"):
                        # #     os.mkdir(savepath + "/" + enFlag)
                        # # if not os.path.exists(savepath + "/" + cnFlag + "/"):
                        # #     os.mkdir(savepath + "/" + cnFlag)
                        #
                        # enfile = open(savepath + "/" + enFlag + "/" + fileNum, 'w+')
                        # cnfile = open(savepath + "/" + cnFlag + "/" + fileNum, 'w+')

                        encnDir = savepath + "/" + enFlag + ";" + cnFlag + "/"
                        if not os.path.exists(encnDir):
                            os.mkdir(encnDir)

                        enfile = open(encnDir + fileNum + ";" + enFlag + ".txt", 'w+')
                        cnfile = open(encnDir + fileNum + ";" + cnFlag + ".txt", 'w+')

                        enfile.write(enpath + "\n")
                        enfile.write(strs[0])
                        enfile.close()

                        cnfile.write(cnpath + "\n")
                        cnfile.write(strs[1])
                        cnfile.close()

                os.path.join(root, fl)

                # result.append(os.path.join(root,fl) + '\n')
        print("总数目", total)
        print("互译对", count)

        return result

    def languageSearchAll(self, readPath, savePath):
        """
        :param readPath: /Users/nali/github/ParallelCorpus/websites/
        :param savePath: /Users/nali/github/ParallelCorpus/texts/
        :return:
        """
        #searchPath = self.basepath + '/websites/'
        paramList = ["language", "lang"]
        searchPath = readPath
        webs= os.listdir(searchPath)

        for dir in webs:
            if os.path.isdir(searchPath + dir):  # 判断是否为文件夹，如果是输出所有文件就改成： os.path.isfile(p)
                filepath = searchPath + dir
                print(filepath)

                pathDir = os.listdir(filepath)
                for enFlag in self.enFlagList:
                    for cnFlag in self.cnFlagList:
                        for language in paramList:
                            self.languagePathSearch(searchPath + dir, savePath + dir, language + "=" + enFlag, language + "=" + cnFlag)


# pairFinder = PairFinder('/Users/nali/github/ParallelCorpus')
# print(pairFinder.basepath)
# # pairFinder.slashPathSearch('/Users/nali/github/ParallelCorpus/websites/www.edb.gov.hk',
# #                            '/Users/nali/github/ParallelCorpus/texts/www.edb.gov.hk',
# #                            '/en/', '/sc/')
# # pairFinder.languageSearchAll('/Users/nali/github/ParallelCorpus/websites/', '/Users/nali/github/ParallelCorpus/texts/')
#
# # pairFinder.slashSearchAll('/Users/nali/github/ParallelCorpus/websites/', '/Users/nali/github/ParallelCorpus/texts/')
# pairFinder.slashPathSearch('/Users/nali/github/ParallelCorpus/websites/www.lcsd.gov.hk/',
#                            '/Users/nali/github/ParallelCorpus/texts/www.lcsd.gov.hk/','en', 'sc', 0)










# enpath = '/Users/nali/github/ParallelCorpus/websites/www.interface.com.cn/index.php?option=com_imagebank&view=downloads&id=1636&Itemid=109&lang=en&task=downloadzip'
# encodingList = ["utf-8", "gb2312", "gbk"]
# with open(enpath, "rb") as f:
#     data = f.read()
#     print(chardet.detect(data))
#     print("\n")
#     if chardet.detect(data)['encoding'].lower() in encodingList:
#         print("encoding is ok!\n")
#         encodingFlag = True
#     else:
#         print("encoding is error!\n")
#         encodingFlag = False

