from urllib import parse

u = parse.urlencode({'wd': '中国'})
url = "https://www.baidu.com/s?{}".format(u)
print(1, url)
print(2, '中国'.encode('utf-8'))
print(3, parse.unquote(u))
print(4, parse.unquote(url))
