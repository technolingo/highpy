import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def slumber(secs):
    print('starting to slumber...')
    time.sleep(secs)
    print('done slumbering.')
    return f'slept for {secs} seconds'


start = time.perf_counter()


with ProcessPoolExecutor() as executor:  # auto joins processes
    values = [2, 4, 1, 3, 5]

    # map vals to the func & get results in the order of submission
    # results = executor.map(slumber, values)
    # for r in results:
    #     print(r)  # NOTE: exceptions only get raised here

    # submit vals to the func & get future objs that can be materialised in the order of completion
    results = [executor.submit(slumber, v) for v in values]
    for f in as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Program finished in {round(finish - start, 2)} seconds.')
