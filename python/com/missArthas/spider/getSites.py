from com.tools.BaiduSearch import BaiduSearch

object = BaiduSearch()

urls, titles = object.search('site:.hk inurl: ( "/zh-cn/" )', 1)
for i in range(len( urls)) :
    print(urls[i])
    print(titles[i])
    