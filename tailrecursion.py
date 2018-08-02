from functools import wraps


def tailrec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.called:
            return lambda: func(*args, **kwargs)
        else:
            wrapper.called = True
        res = func(*args, **kwargs)
        while callable(res):
            res = res()
        return res

    wrapper.called = False
    return wrapper
