from com.missArthas.BaiduSearch import BaiduSearch

object=BaiduSearch()
urls,titles=object.search('site:www.beeden.com inurl: ( "/zh-cn/" )',1)
for i in range(len(urls)):
    print(urls[i])
    print(titles[i])
    print("")