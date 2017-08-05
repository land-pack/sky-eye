import sys
sys.path.append("..")
from datetime import datetime, timedelta
from lib.dbs import DB

big_user_limit = 20


def str_to_datetime(s):
 return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


query_total_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid, max(f_crtime) as latest
    FROM t_diamond_recharge 
    WHERE f_crtime < %s
    GROUP BY f_uid
"""

query_per_day_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid, max(f_crtime) as latest
    FROM t_diamond_recharge 
    WHERE f_crtime BETWEEN %s AND %s
    GROUP BY f_uid
"""

def query_by_max_date(**kwargs):
    print 'kwargs ', kwargs 
    with DB() as db:
        db.cursor.execute(query_total_recharger, (kwargs.get("limit_date"), ))
        d = db.cursor.fetchall()
        for i in d:
            print i
        return d


def query_by_day_date(**kwargs):
    print 'kwargs ', kwargs 
    with DB() as db:
        print '(kwargs.get("limit_date"), kwargs.get("tomorrow") ))', kwargs.get('limit_date'), kwargs.get('tomorrow')
        db.cursor.execute(query_per_day_recharger, (kwargs.get("limit_date"), kwargs.get("tomorrow") ))
        d = db.cursor.fetchall()
        for i in d:
            print i
        return d


def query_data_range(f, begin=None, end=None, step=1):
    begin = str_to_datetime(begin) if begin else  datetime.today()
    end = str_to_datetime(end) if end else  datetime.today()
    day_del = (end - begin).days
    print 'sub day', day_del
    weeks, days = divmod(day_del, step)
    print 'weeks ------->', weeks 
    ret = []
    for i in range(weeks):
        print 'weeks ---------',i
        limit_date = begin + timedelta(days=step * i)
        kwargs = {
            "limit_date":limit_date,
            "tomorrow":limit_date + timedelta(days=step * i),
        }
        result = f(**kwargs)
        ret.append(result)
    return ret 

# ===================



if __name__ == '__main__':
    big_user_total_recharger_by_week = query_data_range(query_by_max_date,
        '2017-07-01 00:00:00', 
        '2017-08-01 00:00:00', 
        7)
    print '='*100
    print '='*100
    query_data_range(query_by_day_date,
        '2017-07-01 00:00:00', 
        '2017-08-01 00:00:00', 
        1)
