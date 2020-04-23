from urllib.request import urlopen
from http.client import HTTPResponse
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

response: HTTPResponse = urlopen("https://www.baidu.com/?a=345")
print(response.closed)
with response as re:
    print(1, type(re))
    print(2, re.status, re.reason)
    print(3, re.geturl())
    print(4, re.info())
    # print(5,re.read())
    with open('t2.html', "w+", encoding="utf-8") as f:
        f.write(re.read().decode())
    print(6, re.msg)
print(response.closed)