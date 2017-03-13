# -*-coding=utf-8-*-
from PS import parser
import MySQLdb
import logging
__author__ = 'LiuJingYuan'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
logger = logging.getLogger("DB")
logging.info('DB')
class MySqlHelper():
    def __init__(self):
        self.Stockparser = parser.Stockparser()
        self.database = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', connect_timeout=5,
                     compress=True, charset='utf8')
        self.cursor = self.database.cursor()
        self.dbname = 'xueqiu'
        self.dbtbstatus = False

    # todo：创建表结构
    def create_db_tb(self, dbname, tbname, keys):
        dbname = str(dbname)
        tbname = str(tbname)
        keys = list(keys)
        self.cursor.execute('create database if not exists {0}'.format(dbname))
        self.database.select_db(dbname)
        self.cursor.execute('DROP TABLE IF EXISTS {0}'.format(tbname))
        sql = 'create table {0}(id int AUTO_INCREMENT,{1}, PRIMARY KEY(id));'.format(tbname, ' varchar(50),'.join(
            keys) + ' varchar(50),spider_time timestamp default CURRENT_TIMESTAMP')
        self.cursor.execute(sql)
        self.database.select_db(dbname)
        self.dbtbstatus = True
        return self.dbtbstatus

    # todo：更新
    def update(self, tableName, condition, value):
        self.cursor.execute('UPDATE %s %s' % (tableName, condition), value)
        self.database.commit()

    # todo: 批量插入
    def batch_insert(self, tbname, keys, values):
        sql = "INSERT INTO {0} ({1})VALUES({2});".format(tbname, ','.join(keys), 's,'.join('%' * len(keys)) + 's')
        self.cursor.executemany(sql,values)
        self.database.commit()

    # 关闭对象、数据库
    def close(self):
        self.cursor.close()
        self.database.close()

    def showdb(self):
        self.cursor.execute('use %s'%self.dbname)
        self.cursor.execute('show tables;')
        result = self.cursor.fetchall()
        return [tb[0] for tb in result]

if __name__ == "__main__":
    pass