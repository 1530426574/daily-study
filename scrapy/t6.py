from urllib.request import Request, urlopen
from http.client import HTTPResponse
import random
from urllib import parse

original_url = "https://search.douban.com/movie/subject_search"
data = parse.urlencode({'search_text': '隐形人', 'cat': '1002'})
with urlopen('{}?{}'.format(original_url, data)) as re:
    print(re.status)
    with open('t2.html', 'w+', encoding='utf-8') as f:
        f.write(re.read().decode())

# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
# request = Request(original_url,headers={'User-agent':ua})
# data= parse.urlencode({'search_text':'大赢家','cat':'1002'})
# print(data)
# response:HTTPResponse = urlopen(request,timeout=20,data=data.encode('utf-8'))
# with response as re:
#     print(re.status)
#     with open('t2.html','w+',encoding='utf-8') as f:
#         f.write(re.read().decode())
