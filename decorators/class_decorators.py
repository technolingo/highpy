class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = repr(args) + repr(sorted(kwargs.items()))
        output = self.cache.get(key)
        if output is None:
            output = self.func(*args, **kwargs)
            self.cache[key] = output
        return output


@Memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(10):
    print(factorial(i))
