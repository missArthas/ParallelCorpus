#调用有道词典的web接口进行翻译
#coding: utf-8
import requests
import json

def translate(word=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key={
    'type':"AUTO",
    'i':word,
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_CLICKBUTTON",
    "typoResult":"true"
    }
    #key这个字典为发送给有道词典服务器的内容，里面的i就是我们需要翻译的内容。此处直接调用word变量。
    response = requests.post(url,data=key)
    return response.text

def get_result(li=None):
    result = json.loads(li)
    print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
    print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])

def main():
    print ("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print ("外文-->中文")
    print ("中文-->英文")
    word = input('请输入你想要翻译的词或句：')
    list_trans = translate(word)
    get=get_result(list_trans)

if __name__ == '__main__':
    main()