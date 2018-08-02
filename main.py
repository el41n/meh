import threading
import multiprocessing
import sys
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


@timer
def seq_fun(callback, amount):
    while amount > 0:
        callback()
        amount -= 1


@timer
def thread_fun(callback, amount):
    threads = []
    while amount > 0:
        threads.append(threading.Thread(target=callback))
        amount -= 1
    for i in threads:
        i.start()
    for i in threads:
        i.join()


@timer
def proc_fun(callback, amount):
    processes = []
    while amount > 0:
        processes.append(multiprocessing.Process(target=callback))
        amount -= 1
    for i in processes:
        i.start()
    for i in processes:
        i.join()


if __name__ == '__main__':
    print(sys.version)
    N = 60000
    CPU_CORES_AMOUNT = multiprocessing.cpu_count() + 1
    seq_fun(lambda: fact(N), CPU_CORES_AMOUNT)
    thread_fun(lambda: fact(N), CPU_CORES_AMOUNT)
    proc_fun(lambda: fact(N), CPU_CORES_AMOUNT)
