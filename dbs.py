import MySQLdb
from pymongo import MongoClient

CBET_VGUESS_ORDER_LIST = "cbet:vguess:orders:{node}:{expect}:{stageid}"
#===========online=================

#MYSQL_HOST = '106.75.139.183'
#MYSQL_USER = 'crazy_bet_ro'
#MYSQL_PASSWORD = '2kJp[]3Ljd'
#MYSQL_DB = 'crazy_bet2'
#MYSQL_PORT = 53306




#============offline===============

MYSQL_HOST = '10.0.1.27'
MYSQL_USER = 'crazy_bet'
MYSQL_PASSWORD = 'crazy_bet'
MYSQL_DB = 'crazy_bet'
MYSQL_PORT = 3306




class DB(object):
    def __enter__(self):
        self.conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB)
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        return self

    def __exit__(self, a, *args, **kwargs):
        if self.conn: self.conn.close()
