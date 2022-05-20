import time

l = []






def in_list(n):
    l = [1,2,3]
    for i in range(n):
        1 in l
        2 in l
        3 in l
        4 in l


def in_tuple(n):
    t = (1,2,3)
    for i in range(n):
        1 in t
        2 in t
        3 in t
        4 in t

def in_set(n):
    s = {1,2,3}
    for i in range(n):
        1 in s
        2 in s
        3 in s
        4 in s

def char_in_set(n):
    s = {'a', 'b', 'c'}
    for i in range(n):
        'a' in s
        'b' in s
        'c' in s
        'd' in s

def char_in_str(n):
    s = 'abc'
    for i in range(n):
        'a' in s
        'b' in s
        'c' in s
        'd' in s

n = 100000000

start = time.perf_counter()
in_list(n)
end = time.perf_counter()
print(f"List: {end - start}")

start = time.perf_counter()
in_tuple(n)
end = time.perf_counter()
print(f"Tuple: {end - start}")

start = time.perf_counter()
in_set(n)
end = time.perf_counter()
print(f"Set: {end - start}")

start = time.perf_counter()
char_in_set(n)
end = time.perf_counter()
print(f"Char in Set: {end - start}")

start = time.perf_counter()
char_in_str(n)
end = time.perf_counter()
print(f"Char Str: {end - start}")
