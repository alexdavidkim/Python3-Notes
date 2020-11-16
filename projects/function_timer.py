# Part 1 - Functional - Section 5:75

import time

# def run_print(f, *args, rep=1, **kwargs):
#     for i in range(rep):
#         f(*args, **kwargs)

# run_print(print, 'life', 'is', 'good', sep='-', end='***\n', rep=10)

def avg_print_time(f, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        f(*args, **kwargs)
    end = time.perf_counter()
    avg_time = (end - start) / rep
    return f'The average print function took: {avg_time}.'

print(avg_print_time(print, 'printing', 'a', 'bunch', end='***\n', rep=1000))