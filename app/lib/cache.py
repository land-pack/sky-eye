import sys
sys.path.append("..")

from lib.utils import to_cache, from_cache

def cache(f):
    def __decorator(*args, **kwargs):
        param = "{}".format(args, kwargs)
        file_name = ".{}-{}.cache".format(f.func_name, param)
        d = from_cache(file_name)
        if d: return d
        ret = f(*args, **kwargs)
        to_cache(ret, file_name)
        return ret
    return __decorator 


def bulking(f):
    pass

@cache
def hxxo(a):
    print 'a',a



if __name__ == '__main__':
    hxxo(99)




            
