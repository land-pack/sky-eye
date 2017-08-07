import sys
sys.path.append("..")
from datetime import datetime, timedelta
from lib.dbs import DB
from lib.utils import str_to_datetime, query_data_range

query_per_day_recharger = """
    SELECT sum(f_money) as moneys, f_uid as uid, max(f_crtime) as latest
    FROM t_diamond_recharge 
    WHERE f_crtime BETWEEN %s AND %s
    GROUP BY f_uid
"""

def query_by_day_date(**kwargs):
    with DB() as db:
        db.cursor.execute(query_per_day_recharger, (kwargs.get("limit_date"), kwargs.get("tomorrow") ))
        d = db.cursor.fetchall()
        return d

def main():
    daily_data = query_data_range(query_by_day_date,
        '2017-07-01 00:00:00', 
        '2017-08-07 00:00:00', 
        1)
    return daily_data

if __name__ == '__main__':
    main()
