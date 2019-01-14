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


@logger
def add_three(n):
    return 3 + n


add_three(5)
