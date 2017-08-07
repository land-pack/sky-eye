import sys
sys.path.append("..")

import bisect
from big_user import main as wmain 
from daily_recharger import main as dmain
from h5_uid import query_uids 
from lib.utils import to_csv

wd = wmain()
dd = dmain('2017-07-01', '2017-08-01')
noapp_users = query_uids()
noapp_uids = [i.get("uid") for i in noapp_users]

vip_user_hash = wd.get('vip')
no_vip_user_hash = wd.get('novip')


def sum_recharger_by_uids_level(days, vip_uids, uid_src=[]):
    all_list = []
    print 'days length', len(days)
    for date, orders in days.items():

        total_vip_money = 0
        total_vip_users = 0

        total_nor_money = 0
        total_nor_users = 0
        
        total_nor_app_money = 0
        total_nor_app_users = 0
        week_edges = vip_uids.keys()

        index = bisect.bisect(week_edges, date)

        index_key = week_edges[index - 1]
        #week_edges.sort()
        week_edges = sorted(week_edges)
        print 'week_edges',week_edges, 'date', date, 'index', index
        #print 'current date is ', date, 'week_edge :', index_key 
        vip_list = vip_uids.get(index_key) or []
        vip_uid_list = [i.get("uid") for i in vip_list]
        for i in orders:
            uid = i.get("uid")
            if uid in vip_uid_list:
                total_vip_money += i.get("moneys")
                total_vip_users += 1
            else:
                if uid in uid_src:
                    total_nor_money += i.get("moneys")
                    total_nor_users += 1
                else:
                    total_nor_app_money += i.get("moneys")
                    total_nor_app_users += 1
        index += 1
        all_list.append([date, str(total_vip_money), str(total_vip_users), str(total_nor_app_money), str(total_nor_app_users),str(total_nor_money), str(total_nor_users)])

    return all_list 

if __name__ == '__main__':
    lst = sum_recharger_by_uids_level(dd, vip_user_hash, noapp_uids)
    lst.sort(key=lambda x:x[0])
    to_csv(lst)

