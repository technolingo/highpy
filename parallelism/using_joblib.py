"""
Joblib is an easier way to write parallel for loops.
Using Joblib, we can split generator expressions into parallel processes.
"""

import time
from joblib import Parallel, delayed, parallel_backend


def slumber(secs):
    print('starting to slumber...')
    time.sleep(secs)
    print('done slumbering.')
    return f'slept for {secs} seconds'


start = time.perf_counter()


# results = [slumber(i) for i in range(5)]
# for r in results:
#     print(r)

# the default backend is "loky", which runs the processes in parallel on multiple CPUs
# (with some serialisation overhead)
Parallel(n_jobs=5)(delayed(slumber)(i) for i in range(5))


# the backend can be changed to "threading" which uses the GIL to run jobs concurrently
# Parallel(n_jobs=5, prefer="threading")(delayed(slumber)(i) for i in range(5))

# this context manager can also be used to set joblib backend
# when calling another library that uses joblib internally
# with parallel_backend('threading', n_jobs=2):
#     Parallel()(delayed(slumber)(i) for i in range(5))


# HOW IT WORKS:
# delayed is a decorator,
# - which returns a function and input arguments as a tuple
# Parallel constructs an object,
# - which can be called with an iterable of tuples,
# - - where each tuple includes a function, positional arguments, & keyword arguments
# - when called, it executes each function with its corresponding arguments

# we can also use Parallel without delayed
# Parallel(n_jobs=5)((slumber, (i,), {}) for i in range(5))


# Shared memory (optional, with overhead)
# shared_set = set()
# def collect(x):
#     shared_set.add(x)


# Parallel(n_jobs=2, require='sharedmem')(delayed(collect)(i) for i in range(5))
# print(sorted(shared_set))


finish = time.perf_counter()

print(f'Program finished in {round(finish - start, 2)} seconds.')
