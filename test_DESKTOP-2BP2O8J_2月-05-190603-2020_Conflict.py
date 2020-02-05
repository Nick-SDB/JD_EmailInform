import requests
import time
import random
import json
import re

# 已下架 StockState = 33
# i = 'https://c0.3.cn/stock?skuId=65426898142&area=15_1233_1238_42401&venderId=10078105&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery2661232'
# 无货 StockState = 34
# i = 'https://c0.3.cn/stock?skuId=17449572308&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery7465039'
# 有货 
# i = 'https://c0.3.cn/stock?skuId=100010266524&area=15_1233_1238_42401&venderId=1000000706&buyNum=1&choseSuitSkuIds=&cat=670,677,678&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery1343895'
i = 'https://c0.3.cn/stock?skuId=29160736185&area=15_1233_1238_42401&venderId=659202&buyNum=1&choseSuitSkuIds=&cat=9192,12190,12608&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery598969'

flag = 0
session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Connection": "keep-alive"
}
skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
print('Sending get request')
response = session.get(i)
# 从jquery中提取json
response_text = response.text
response_text_json = response_text[re.search('{', response_text).span()[0]: len(response_text) - 1]
response_json = json.loads(response_text_json)
print(response_json['stock']['IsPurchase'])
# response_text = json.loads(response.text)
# print(content)

