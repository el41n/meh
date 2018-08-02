import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('^^^Start {}^^^'.format(func.__name__))
        start = time.time()
        res = func(*args, **kwargs)
        print("---Finish {} execution time = {}---".format(func.__name__,
                                                       time.time() - start))
        return res
    return wrapper
