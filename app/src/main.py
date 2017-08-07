from big_user import main as wmain 
from daily_recharger import main as dmain
from h5_uid import query_uids 

wd = wmain()
dd = dmain()
noapp_users = query_uids()
noapp_uids = [i.get("uid") for i in noapp_users]

vip_user_hash = wd.get('vip')
no_vip_user_hash = wd.get('novip')


def sum_recharger_by_uids_level(days, vip_uids, uid_src=[]):
    all_list = []
    index = 0
    for orders in days:

        total_vip_money = 0
        total_vip_users = 0

        total_nor_money = 0
        total_nor_users = 0
        
        total_nor_app_money = 0
        total_nor_app_users = 0
    
        w, d = divmod(index, 7)
        vip_list = vip_uids.get(w) or []
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
        all_list.append([int(total_vip_money), total_vip_users, int(total_nor_app_money), total_nor_app_users, int(total_nor_money), total_nor_users])

    return all_list 

if __name__ == '__main__':
    lst = sum_recharger_by_uids_level(dd, vip_user_hash, noapp_uids)
    for i in lst:
        print i

