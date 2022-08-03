'''Redis client'''
import redis

POOL = redis.ConnectionPool(host='redis', port=6379, db=0)


class TryAquireLock():
    '''Allows you to aquire a lock and auto releases it.'''

    def __init__(self, key):
        self.key = key
        self.did_aquire = False

    def __enter__(self):
        self.did_aquire = try_aquire_lock(self.key, 600)
        return self.did_aquire

    def __exit__(self, _ex_type, _ex_value, _ex_traceback):
        if self.did_aquire:
            del_key(self.key)


def try_aquire_lock(key, ex=120):
    '''aquire_lock'''
    host = get_host()
    return host.set(key, 1, ex=ex, nx=True)


def get_host():
    '''get_host'''
    return redis.Redis(connection_pool=POOL)


def set_if_not_exist(key, value, expire):
    '''set_if_not_exist'''
    host = get_host()
    result = host.set(name=key, value=value, nx=True, ex=expire)
    return result


def get_key(key):
    '''get_key'''
    host = get_host()
    result = host.get(key)
    return result


def set_key(key, value):
    '''set_key'''
    host = get_host()
    result = host.set(key, value)
    return result


def set_ex(key, value, expire):
    '''set_key'''
    host = get_host()
    result = host.set(key, value, ex=expire)
    return result


def del_key(key):
    '''del_key'''
    host = get_host()
    host.delete(key)
