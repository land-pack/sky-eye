import bisect
from collections import defaultdict
import json
import ujson

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

def to_csv(lst, name='data.csv'):
    with open(name, 'wb') as f:
        for item in lst:
            item = [str(i) for i in item]
            line = ','.join(item) + '\n'
            print 'line type', type(line)
            try:
                f.write(line.encode('utf-8'))
            except:
                f.write(line)

def to_cache(data, name='cache'):
    try:
        s = ujson.dumps(data)
        with open(name, 'wb') as fd:
            fd.write(s)
    except Exception as ex:
        print ex

def from_cache(f):
    try:
        with open(f, 'r') as fd:
            d = fd.read()
            s = ujson.loads(d)
            return s

    except Exception as ex:
        print ex
        return None

def classify(lst, field, cond):
    new_lst = defaultdict(list)
    for i in lst:
        value = i.get(field)
        key = bisect.bisect_right(cond, value)
        new_lst[key].append(i)

    return new_lst 

        

if __name__ == '__main__':
    a = {
        "name":"frank"
    }
    to_cache(a)
    d = from_cache('cache')
    print 'ddd',d

    # test classify 
    lst = [
        {
            "age": 33,
            "name":"fssk"
        },
        {
            "age": 23,
            "name":"frank"
        },
        {
            "age": 21,
            "name":"jack"
        },
        {
            "age": 11,
            "name":"jack"
        }
    ]

    cond = [0, 20, 30]
    new_a = classify(lst, 'age', cond)
    print new_a

