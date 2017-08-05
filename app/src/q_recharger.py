import sys
sys.path.append("..")
from datetime import datetime, timedelta
from lib.dbs import DB


def str_to_datetime(s):
 return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


query_total_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid
    FROM t_diamond_recharge 
    WHERE f_crtime < %s
    GROUP BY f_uid
"""

def query_by_date(util):
    with DB() as db:
        db.cursor.execute(query_total_recharger, (util, ))
        d = db.cursor.fetchall()
        for i in d:
            print i




def query_data_range(begin=None, end=None, step=1):
    begin = str_to_datetime(begin) if begin else  datetime.today()
    end = str_to_datetime(end) if end else  datetime.today()
    day_del = (end - begin).days
    print 'sub day', day_del
    weeks, days = divmod(day_del, step)
    for i in range(weeks):
        print 'weeks ---------',i
        limit_date = begin + timedelta(days=step)
        query_by_date(limit_date)



if __name__ == '__main__':
    query_data_range(
        '2017-07-01 00:00:00', 
        '2017-08-01 00:00:00', 
        7)
