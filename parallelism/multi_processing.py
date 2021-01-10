import time
import multiprocessing


def slumber(secs):
    print('starting to slumber...')
    time.sleep(secs)
    print('done slumbering.')


start = time.perf_counter()

# slumber(1)
# slumber(1)
# slumber(1)
# slumber(1)

processes = []
for _ in range(4):
    p = multiprocessing.Process(target=slumber, args=(1,))
    p.start()
    processes.append(p)

print('Continue with other tasks in the meanwhile...')

for p in processes:
    p.join()  # wait for the processes to finish before continuing

finish = time.perf_counter()

print(f'Program finished in {round(finish - start, 2)} seconds.')
