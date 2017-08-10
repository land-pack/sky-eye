from config import *
from pymongo import MongoClient
import MySQLdb

print '--->',DB_HOST, DB_PORT, DB_PASSWD, DB_USERNAME, DB_NAME
class DB(object):

    def __init__(self, switch='online', c='xx'):
        self.c = c
        if switch == 'online':
            self.host = DB_HOST
            self.port = DB_PORT 
            self.passwd = DB_PASSWD
            self.username = DB_USERNAME
            self.db = DB_NAME
            self.mongo_uri = DB_MONGO_URI
        else:
            self.host = DB_HOST_OFFLINE
            self.port = DB_PORT_OFFLINE
            self.passwd = DB_PASSWD_OFFLINE
            self.username = DB_USERNAME_OFFLINE
            self.db = DB_NAME_OFFLINE
            self.mongo_uri = DB_MONGO_URI_OFFLIN

    def __enter__(self):
        self.conn = MySQLdb.connect(host=self.host, port=int(self.port), user=self.username, passwd=self.passwd, db=self.db)
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        client = MongoClient(self.mongo_uri)
        mdb = client['crazy_bet2']
        self.mdb= mdb
        self.mdb.collections = self.c
        return self

    def __exit__(self, a, *args, **kwargs):
        if self.conn: self.conn.close()



if __name__ == '__main__':
    with DB() as db:
        sql = """SELECT VERSION()"""
        db.cursor.execute(sql)
        version = db.cursor.fetchone()
        print version 


	with DB(c='t_matches_activity') as db:
		lst = db.mdb.t_matches_activity.find({})
		for i in lst:
			print i
