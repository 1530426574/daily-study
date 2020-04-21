from urllib.request import Request, urlopen
from http.client import HTTPResponse
import random

url = "http://ww.bing.com"

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
request = Request(url)
request.add_header('User-Agent', ua)
print(type(request))

response: HTTPResponse = urlopen(request, timeout=20)
print(type(response))
with response as re:
    print(1, re.status, re.getcode())
    print(2, re.geturl())
    print(3, re.read())
print(4, request.get_header('User-agent'))
print(5, 'user-agent'.capitalize())
