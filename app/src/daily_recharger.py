import sys
sys.path.append("..")
from datetime import datetime, timedelta
from lib.dbs import DB
from lib.utils import str_to_datetime, query_data_range
from collections import defaultdict 

query_per_day_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid, DATE_FORMAT(f_crtime, "%%Y-%%m-%%d") as latest
    FROM t_diamond_recharge 
    WHERE f_crtime BETWEEN %s AND %s
    GROUP BY DATE_FORMAT(f_crtime, "%%Y-%%m-%%d") , f_uid
"""

def main(begin, end):
    lst = defaultdict(list)
    with DB() as db:
        db.cursor.execute(query_per_day_recharger, (begin, end))
        d = db.cursor.fetchall()
        
        for i in d:
            date = i.get("latest")
            lst[date].append(i)
        return lst

if __name__ == '__main__':
    s=main('2017-07-01', '2017-08-07')
    print s
