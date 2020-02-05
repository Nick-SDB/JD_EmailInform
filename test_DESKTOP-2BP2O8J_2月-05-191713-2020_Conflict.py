import requests
import time
import random
import json
import re

i = 'https://c0.3.cn/stock?skuId=54343606579&area=15_1233_1238_42401&venderId=659202&buyNum=1&choseSuitSkuIds=&cat=9192,12190,12608&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery9193844'
# s://c0.3.i = 'httpcn/stock?skuId=100004559325&area=15_1233_1238_42401&venderId=1000000904&buyNum=1&choseSuitSkuIds=&cat=9987,653,655&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery2770362'

session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Connection": "keep-alive"
}
skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
response = session.get(i)
response_text = response.text
response_text_json = response_text[re.search('{', response_text).span()[0]: len(response_text) - 1]
response_json = json.loads(response_text_json)
print(response_json)