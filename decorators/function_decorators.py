def logger(func):
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    import logging
    logging.basicConfig(
        filename=f'{dir_path}/{func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        logging.info(f'Args {args} & kwards {kwargs} --> result: {output}')
        return output

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = repr(args) + repr(sorted(kwargs.items()))
        output = cache.get(key)
        if output is None:
            output = func(*args, **kwargs)
            cache[key] = output
        return output

    return wrapper


@logger
def add_three(n):
    return 3 + n


@memoize
def fib(n):
    ''' return the n-th fibonacci.'''
    assert n >= 0
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


# result = add_three(5)
# print(result)

for i in range(10):
    print(fib(i))
