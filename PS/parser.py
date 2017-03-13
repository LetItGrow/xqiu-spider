# -*-coding=utf-8-*-
import json
import logging
from SP.spider import Xueqiuspider
__author__ = 'LiuJingYuan'
logger = logging.getLogger("PS")
logging.info('use PS')

class Stockparser():

    def __init__(self):
        pass

    def Stockparser(self,stocktext):
        logging.info('stock text : %s'%stocktext)
        self.xueqiudict = json.loads(stocktext)
        logging.info('stock dict : %s' % self.xueqiudict)
        status = self.xueqiudict["success"]
        logging.info('stock status : %s' % status)
        stockid = self.xueqiudict["stock"]
        logging.info('stock id : %s' % stockid)
        self.keys = dict(self.xueqiudict[dict(self.xueqiudict).keys()[0]][0]).keys()
        return self.keys,status,stockid,[(stock['volume'], stock['current'], stock['avg_price'], stock['time']) for stock in
                               self.xueqiudict["chartlist"]]

if __name__ == '__main__':
    pass