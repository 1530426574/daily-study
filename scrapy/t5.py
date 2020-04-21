from urllib.request import Request, urlopen
from http.client import HTTPResponse
import random
from urllib import parse

original_url = "http://httpbin.org/post"
data = parse.urlencode({'name': "louis", 'age': '27'})

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

request = Request(original_url, headers={'User-agent': ua})

response: HTTPResponse = urlopen(request, timeout=20, data=data.encode('utf-8'))
with response as re:
    print(re.status)
    with open('t2.html', 'w+', encoding='utf-8') as f:
        f.write(re.read().decode())
print(request.data)
