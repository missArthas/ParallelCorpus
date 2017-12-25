#coding=utf-8
from bs4 import BeautifulSoup
import os


class Html2Text(object):

    def html2Text(self, enpath, cnpath):
        """
        :type enpath: str
        :type cnpath: str
        :rtype: List[str]
        """

        ensoup = BeautifulSoup(open(enpath), 'lxml')
        cnsoup = BeautifulSoup(open(cnpath), 'lxml')

        enstr = ""
        cnstr = ""

        enstr = enstr + ensoup.title.getText() + '\n'
        for string in ensoup.body.stripped_strings:
            enstr += (string + '\n')

        cnstr += cnsoup.title.getText() + '\n'
        for string in cnsoup.body.stripped_strings:
            cnstr += (string + '\n')

        return [enstr, cnstr]

