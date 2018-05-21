#coding=utf-8
from bs4 import BeautifulSoup
import os


class Html2Text(object):

    def html2Text(self, ensoup, cnsoup):
        """
        :type ensoup: BeautifulSoup
        :type cnsoup: BeautifulSoup
        :rtype: List[str]
        """
        # ensoup = BeautifulSoup(open(enpath), 'lxml')
        # cnsoup = BeautifulSoup(open(cnpath), 'lxml')

        enstr = ""
        cnstr = ""
        if ensoup.title != None:
            enstr = enstr + ensoup.title.getText() + '\n'
        for string in ensoup.body.stripped_strings:
            enstr += (string + '\n')

        if cnsoup.title != None:
            cnstr += cnsoup.title.getText() + '\n'
        for string in cnsoup.body.stripped_strings:
            cnstr += (string + '\n')

        return [enstr, cnstr]


