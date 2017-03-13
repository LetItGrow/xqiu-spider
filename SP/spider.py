# -*-coding=utf-8-*-
import logging

from lxml import etree
import requests

from CK.cookies import FetchCookies
from HD.headers import HEADER
__author__ = 'LiuJingYuan'

logger = logging.getLogger("SP")
logging.info('use SP')

class Xueqiuspider():
    def __init__(self,stockid):
        if not hasattr(self, 'FetchCookies'):
            self.FetchCookies = FetchCookies()
            self.cookies = self.FetchCookies.dictcookies()
        self.stockURL = 'https://xueqiu.com/S/{0}'.format(stockid)
        self.baseURL = 'https://xueqiu.com/stock/forchart/stocklist.json?symbol={0}&period=1d&one_min=1&_='.format(
            stockid)

    def getstockurl(self):
        try:
            stock = requests.get(self.stockURL , headers=HEADER)
            logging.info('stock text %s'%stock.text)
        except Exception as e:
            stock = requests.get(self.stockURL, headers=HEADER,cookies=self.cookies)
            logging.info('stock text %s' % stock.text)
        try:
            root = etree.HTML(stock.text)
            urlid = root.xpath("//script[2]")[0].text.split("=")[-2].split("\n")[0].strip()
            logging.info('stock  urlid %s' % urlid)
            # print self.baseURL + urlid
            return self.baseURL + urlid
        except Exception as e:
            logging.error('Exception1: %s' % e)
            return None

    def stockdata(self):
        try:
            # print self.getstockurl(),self.CK
            stocklist = requests.get(self.getstockurl(), headers=HEADER, cookies=self.cookies)
            logging.info('Stock  Data %s' % stocklist.text)
            return stocklist.text
        except Exception as e:
            logging.error('Exception2: %s' % e)
            return None

if __name__ == '__main__':
    pass