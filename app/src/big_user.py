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
    with DB() as db:
        db.cursor.execute(query_total_recharger, (kwargs.get("limit_date"), ))
        d = db.cursor.fetchall()
        return d


def query_data_range(f, begin=None, end=None, step=1):
    begin = str_to_datetime(begin) if begin else  datetime.today()
    end = str_to_datetime(end) if end else  datetime.today()
    day_del = (end - begin).days
    weeks, days = divmod(day_del, step)
    print 'total weeks', weeks, 'left days', days
    week_to_data = {}
    for i in range(weeks):
        limit_date = begin + timedelta(days=step * i)
        week_edge = str(limit_date).split(' ')[0]
        kwargs = {
            "limit_date":limit_date,
            "tomorrow":limit_date + timedelta(days=step * i),
        }
        result = f(**kwargs)
        week_to_data.update({week_edge:result})

    return week_to_data

def split_user_by_recharger_level(lst):
    vip_user_lst = defaultdict(list)
    no_vip_user_lst = defaultdict(list)
    for week, values in lst.items():
        for i in values:
            if i.get("moneys") >= big_user_limit:
                vip_user_lst[week].append(i)
            else:
                no_vip_user_lst[week].append(i)
    
    print 'catch vip user =%s || no vip user=%s' % (len(vip_user_lst), len(no_vip_user_lst))
    return {
            'vip':vip_user_lst,
            'novip':no_vip_user_lst
    }

def main():
    big_user_total_recharger_by_week = query_data_range(query_by_max_date,
        '2017-07-01 00:00:00', 
        '2017-08-01 00:00:00', 
        7)
    d= split_user_by_recharger_level(big_user_total_recharger_by_week)
    return d

if __name__ == '__main__':
    main()
