import sys
sys.path.append("..")
from collections import defaultdict
from datetime import datetime, timedelta
from lib.dbs import DB
from lib.utils import str_to_datetime 


sql = "SELECT f_uid as uid FROM t_user WHERE f_src != 'crazybet'"

def query_uids():
    with DB() as db:
        db.cursor.execute(sql)
        d = db.cursor.fetchall()
        return d

if __name__ == '__main__':
    lst = query_uids()
    print lst
