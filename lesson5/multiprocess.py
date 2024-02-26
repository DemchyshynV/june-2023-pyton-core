import time
import math
import multiprocessing


def time_decor(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time() - start_time)

    return inner


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(num / 2) / 15 * 5000))) + 'H'


@time_decor
def main_process():
    print('main')
    r = range(50_000_000)
    with open('file.txt', 'w') as file:
        for i in r:
            result = work(i)
            print(result, file=file)


# main_process()

@time_decor
def mp():
    print('mp')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')

    with multiprocessing.Pool(count) as p:
        r = range(50_000_000)
        with open('file2.txt', 'w') as file:
            tasks = p.map(work, r)
            for res in tasks:
                print(res, file=file)


mp()
