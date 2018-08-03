import threading
import multiprocessing
import sys
import time
from functools import partial
import requests

from tailrecursion import tailrec
from timer import timer


@timer
def fact(n):
    @tailrec
    def tail_fact(n, acc=1):
        if n == 0:
            return acc
        else:
            return tail_fact(n-1, acc*n)

    return tail_fact(n)


def time_delay(delay=1):
    time.sleep(1)


@timer
def seq_fun(callback, amount=None):
    if amount:
        while amount > 0:
            callback()
            amount -= 1
    else:
        for call in callback:
            call()


@timer
def thread_fun(callback, amount=None):
    threads = []

    if amount:
        while amount > 0:
            threads.append(threading.Thread(target=callback))
            amount -= 1
    else:
        for call in callback:
            threads.append(threading.Thread(target=call))

    for i in threads:
        i.start()
    for i in threads:
        i.join()


@timer
def proc_fun(callback, amount=None):
    processes = []

    if amount:
        while amount > 0:
            processes.append(multiprocessing.Process(target=callback))
            amount -= 1
    else:
        for call in callback:
            processes.append(multiprocessing.Process(target=call))

    for i in processes:
        i.start()
    for i in processes:
        i.join()


@timer
def download_video(url):
    name = url.split('/')[-1]
    print(name)
    content = requests.get(url)
    with open(name, 'wb') as file:
        file.write(content.content)


if __name__ == '__main__':
    print(sys.version)

    N = 60000
    CPU_CORES_AMOUNT = multiprocessing.cpu_count() + 1
    #callback = lambda: fact(N, CPU_CORES_AMOUNT)
    callback = time_delay
    seq_fun(callback, CPU_CORES_AMOUNT)
    thread_fun(callback, CPU_CORES_AMOUNT)
    proc_fun(callback, CPU_CORES_AMOUNT)

    VIDEO_URLS = [
        'http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_2mb.mp4',
        'http://www.sample-videos.com/video/mp4/480/big_buck_bunny_480p_2mb.mp4',
    ]

    download_functions = [partial(download_video, url) for url in VIDEO_URLS]
    seq_fun(download_functions)
    thread_fun(download_functions)
    proc_fun(download_functions)

