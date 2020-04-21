import requests
from requests.models import Response, Request

urls = ["https://www.baidu.com/s?wd=magedu", "https://www.baidu.com/s?wd=magedu"]
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
session = requests.Session()
with session as s:
    # for url in urls:
    with s.get("https://www.baidu.com/s?wd=magedu", headers={'User=agent': ua}) as re:
        # with requests.request('GET',url,headers={'User-agent':ua}) as re :
        print(0, re.request.headers)
        print(1, re.cookies)
        with open('t2.html', 'w+', encoding='utf-8') as f:
            f.write(re.text)
        print('--------------------------------')
    with s.get("https://www.baidu.com/s?wd=xuwei", headers={'User=agent': ua}) as re:
        # with requests.request('GET',url,headers={'User-agent':ua}) as re :
        print(0, re.request.headers)
        print(1, re.cookies)
        with open('t3.html', 'w+', encoding='utf-8') as f:
            f.write(re.text)
        print('--------------------------------')

# response:Response = requests.request('GET',url,headers={'User-agent':ua})
#
# with response as re:
#     print(type(re))
#     print(1,re.url)
#     print(2,re.status_code)
#     print(3,re.headers)
#     print(4,re.request.headers)
#     print(5,re.encoding)
#     print(6,re.content)
#     with open('t2.html','w+',encoding='utf-8') as f:
#         f.write(re.text)
