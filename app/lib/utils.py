from datetime import datetime, timedelta

def str_to_datetime(s):
 return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def query_data_range(f, begin=None, end=None, step=1):
    begin = str_to_datetime(begin) if begin else  datetime.today()
    end = str_to_datetime(end) if end else  datetime.today()
    day_del = (end - begin).days
    weeks, days = divmod(day_del, step)
    print 'total days ', weeks
    ret = []
    for i in range(weeks):
        limit_date = begin + timedelta(days=step * i)
        print 'limit_date -->', limit_date
        kwargs = {
            "limit_date":limit_date,
            "tomorrow":limit_date + timedelta(days=step * i),
        }
        result = f(**kwargs)
        ret.append(result)
    return ret 

def to_csv(lst):
	with open('data.csv', 'wb') as f:
		for item in lst:
		    line = ','.join(item) + '\n'
		    f.write(line.encode('utf-8'))
