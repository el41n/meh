from tailrecursion import tailrec
import threading
import time
from timer import timer


@timer
def fact(n):
    @tailrec
    def tail_fact(n, acc=1):
        if n == 0:
            print('over')
            return acc
        else:
            return tail_fact(n-1, acc*n)

    return tail_fact(n)


if __name__ == '__main__':
    N = 80000
    N1 = 10
    t = threading.Thread(target=lambda: fact(N), daemon=True)
    t.start()
    fact(N1)
    t.join()
