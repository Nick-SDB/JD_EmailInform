#coding=utf-8

import requests
import time
import random
import json
import re
from configurarion import *

# 商品的url
url = [
    'https://c0.3.cn/stock?skuId=65426813241&area=15_1233_1238_42401&venderId=665737&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery76896',
    'https://c0.3.cn/stock?skuId=65426813242&area=15_1233_1238_42401&venderId=665737&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery9365077',
    'https://c0.3.cn/stock?skuId=65420955733&area=15_1233_1238_42401&venderId=10227223&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery8595650',
    'https://c0.3.cn/stock?skuId=17449572304&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery3214622',
    'https://c0.3.cn/stock?skuId=17449572305&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery575572',
    'https://c0.3.cn/stock?skuId=17449572306&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery8501347',
    'https://c0.3.cn/stock?skuId=17449572309&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery1177955',
    'https://c0.3.cn/stock?skuId=17449572307&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery3720592',
    'https://c0.3.cn/stock?skuId=17449572311&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery2499469',
    'https://c0.3.cn/stock?skuId=17449572310&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery8436184',
    'https://c0.3.cn/stock?skuId=17449572308&area=15_1233_1238_42401&venderId=724119&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery7465039',
    'https://c0.3.cn/stock?skuId=62408717969&area=15_1233_1238_42401&venderId=10112044&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery7382467',
    'https://c0.3.cn/stock?skuId=62408717970&area=15_1233_1238_42401&venderId=10112044&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery9065091',
    'https://c0.3.cn/stock?skuId=56657322838&area=15_1233_1238_42401&venderId=10238087&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery867081',
    'https://c0.3.cn/stock?skuId=56655493806&area=15_1233_1238_42401&venderId=10238087&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery5499223',
    'https://c0.3.cn/stock?skuId=56655493809&area=15_1233_1238_42401&venderId=10238087&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery7237874',
    'https://c0.3.cn/stock?skuId=56657322841&area=15_1233_1238_42401&venderId=10238087&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580742651197543050433&ch=1&callback=jQuery9615283',
    'https://c0.3.cn/stock?skuId=65424912829&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery7713247',
    'https://c0.3.cn/stock?skuId=1614629784&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery4334984',
    'https://c0.3.cn/stock?skuId=1614629785&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery9178520',
    'https://c0.3.cn/stock?skuId=1614629787&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery530148',
    'https://c0.3.cn/stock?skuId=1614629788&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery4057810',
    'https://c0.3.cn/stock?skuId=65424912828&area=15_1233_1238_42401&venderId=117784&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery8708925',
    'https://c0.3.cn/stock?skuId=51137726168&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery6130199',
    'https://c0.3.cn/stock?skuId=51137726170&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery6710010',
    'https://c0.3.cn/stock?skuId=51137726172&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery2819112',
    'https://c0.3.cn/stock?skuId=51137726173&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery5453313',
    'https://c0.3.cn/stock?skuId=51137726179&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery8477107',
    'https://c0.3.cn/stock?skuId=51137726169&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery9703025',
    'https://c0.3.cn/stock?skuId=51137726171&area=15_1233_1238_42401&venderId=645952&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580787804339563515333&ch=1&callback=jQuery772545',
    
]


def sendMail(url, shop, price):
    import smtplib
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header

    # 用于构建邮件头

    # 发信方的信息:发信邮箱，QQ 邮箱授权码
    # from_addr = 'sender email address'
    # password = 'your SMTP address'

    # 收信方邮箱
    # to_addr = 'receiver email address'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    mail_msg = '[￥' + price + ' ] ' + shop + '\n' + url
    msg = MIMEText(mail_msg, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('有口罩啦 ' + time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


flag = 0
while (1):
    try:
        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        print('=============================================================')
        print('Attemp no.' + str(flag) + ' at ' + time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime()))
        flag += 1
        index = 0
        for i in url:
            index += 1
            # 商品url
            skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
            response = session.get(i)
            response_text = response.text
            response_text_json = response_text[re.search('{', response_text).span()[0]: len(response_text) - 1]
            response_json = json.loads(response_text_json)
            
            # if response_json['stock']['D']['deliver']:
            #     shop = response_json['stock']['D']['deliver']
            # else:
            #     shop = response_json['stock']['self_D']['deliver']
            if 'D' in response_json['stock']:
                shop = response_json['stock']['D']['deliver']
            elif 'self_D' in response_json['stock']:
                shop = response_json['stock']['self_D']['deliver']

            price = response_json['stock']['jdPrice']['p']
            # log= str(response_json['stock']['StockState']) + '\n' + response_json['stock']['StockStateName']
            # print (log)
            if response_json['stock']['StockState'] == 33 and response_json['stock']['StockStateName'] == '现货':
                print('[' + str(index) + '] In stock : '     + skuidUrl)
                sendMail(skuidUrl, shop, price)
            elif response_json['stock']['StockState'] == 34:
                print('[' + str(index) + '] Out of stock : ' + skuidUrl) 
            else:
                print('[' + str(index) + '] Off shelf : '    + skuidUrl) 
        sleeptime = 5 + random.uniform(-2,2)
        print('Sleep ' + str(sleeptime) + ' seconds.')
        time.sleep(sleeptime)
    except Exception as e:
        print('ERROR ', str(e))