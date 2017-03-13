# -*-coding=utf-8-*-
import logging.config
import time
from gevent.pool import Pool
from gevent import monkey
from DB.MYSQLHelper import MySqlHelper
from HD.headers import THREADNUM
from PS.parser import Stockparser
from SP.spider import Xueqiuspider
from URL.urls import stockids

monkey.patch_all()
__author__ = 'LiuJingYuan'
logging.config.fileConfig('logging.conf')

class xueqiu():
    def __init__(self):
        if not hasattr(self, 'Stockparser') or not hasattr(self, 'MySqlHelper'):
            self.Stockparseri = Stockparser()
            self.MySqlHelperi = MySqlHelper()
            self.keys = []

    def run(self,stockid):
        self.Xueqiuspideri = Xueqiuspider(stockid)
        print stockid
        logging.info('stock stockid:%s' % stockid)
        stockdata = self.Xueqiuspideri.stockdata()
        # print stockdata
        logging.info('stock data:%s' % stockdata)
        stockjson = self.Stockparseri.Stockparser(stockdata)[3]
        if self.keys==[]:
            self.keys = self.Stockparseri.keys
        logging.info('self.keys:%s' % self.keys)
        try:
            if stockid.lower() not in self.MySqlHelperi.showdb():
                self.MySqlHelperi.create_db_tb(self.MySqlHelperi.dbname, stockid, self.keys)
        except Exception as e:
            self.MySqlHelperi.create_db_tb(self.MySqlHelperi.dbname, stockid, self.keys)
        try:
            self.MySqlHelperi.batch_insert(stockid,self.keys,stockjson)
            logging.info('%s,%s,%s !',stockid,self.keys,stockjson)
        except Exception as e:
            print e
        logging.info('insert into done !')

def main():
    while True:
        xueqius = xueqiu()
        crawl_pool = Pool(THREADNUM)
        works = crawl_pool.map(xueqius.run, stockids)
        print u'已抓取%s支股票实时数据！' % len(works)
        time.sleep(60)
    self.MySqlHelperi.close()

if __name__ == '__main__':
    main()