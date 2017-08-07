import sys
sys.path.append("..")
from collections import defaultdict
from datetime import datetime, timedelta
from lib.dbs import DB
from lib.utils import str_to_datetime 

big_user_limit = 3500

query_total_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid, max(f_crtime) as latest
    FROM t_diamond_recharge 
    WHERE f_crtime < %s
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


def query_data_range(f, begin=None, end=None, step=1):
    begin = str_to_datetime(begin) if begin else  datetime.today()
    end = str_to_datetime(end) if end else  datetime.today()
    day_del = (end - begin).days
    print 'sub day', day_del
    weeks, days = divmod(day_del, step)
    print 'weeks ------->', weeks 
    week_to_data = {}
    for i in range(weeks):
        print 'weeks ---------',i
        limit_date = begin + timedelta(days=step * i)
        kwargs = {
            "limit_date":limit_date,
            "tomorrow":limit_date + timedelta(days=step * i),
        }
        result = f(**kwargs)
        week_to_data.update({i:result})

    return week_to_data
# ======================================
def split_user_by_recharger_level(lst):
    vip_user_lst = defaultdict(list)
    no_vip_user_lst = defaultdict(list)
    for week, values in lst.items():
        for i in values:
            print 'i',i
            if i.get("moneys") >= big_user_limit:
                vip_user_lst[week].append(i)
            else:
                no_vip_user_lst[week].append(i)
    
    print 'catch vip user =%s || no vip user=%s' % (len(vip_user_lst), len(no_vip_user_lst))
    return {
            'vip':vip_user_lst,
            'novip':no_vip_user_lst
    }

if __name__ == '__main__':
    big_user_total_recharger_by_week = query_data_range(query_by_max_date,
        '2017-07-01 00:00:00', 
        '2017-08-01 00:00:00', 
        7)
    print type(big_user_total_recharger_by_week)
    d= split_user_by_recharger_level(big_user_total_recharger_by_week)
    print '==vip -->'
    vip_user = d.get('vip')
    for i, v in vip_user.items():
        print 'week',i, 'length',len(v), 'lst',v
