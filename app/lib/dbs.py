from config import *
import MySQLdb

class DB(object):
    def __enter__(self):
        self.conn = MySQLdb.connect(host=DB_HOST, port=DB_PORT, user=DB_USERNAME, passwd=DB_PASSWD, db=DB_NAME)
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        return self

    def __exit__(self, a, *args, **kwargs):
        if self.conn: self.conn.close()



if __name__ == '__main__':
    with DB() as db:
        sql = """SELECT VERSION()"""
        db.cursor.execute(sql)
        version = db.cursor.fetchone()
        print version 
