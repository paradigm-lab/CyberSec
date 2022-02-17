from timeit import default_timer as timer

def timefunc(func):
    def inner(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        message = f'{func.__name__} took {end - start} seconds'
        print(message)
        return result
    return inner