from collections import deque
from queue import LifoQueue
import time

def list_stack(n):
    l = []
    start = time.perf_counter()
    for _ in range(n):
        l.append(n)
    end = time.perf_counter()
    print(f"List Stack: {end - start}")


def queue_stack(n):
    q = deque()
    start = time.perf_counter()
    for _ in range(n):
        q.append(n)
    end = time.perf_counter()
    print(f"Queue Stack: {end - start}")

def lifo_queue_dtack(n):
    q = LifoQueue(maxsize=n)
    for _ in range(n):
        q.put(n)

n = 1000000000

# start = time.perf_counter()
list_stack(n)
# end = time.perf_counter()
# print(f"List Stack: {end - start}")

# start = time.perf_counter()
queue_stack(n)
# end = time.perf_counter()
# print(f"Queue Stack: {end - start}")


# start = time.perf_counter()
# lifo_queue_dtack(n)
# end = time.perf_counter()
# print(f"Lifo Queue Stack: {end - start}")
