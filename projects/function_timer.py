# Part 1 - Functional - Section 5:75

import time

# def run_print(f, *args, rep=1, **kwargs):
#     for i in range(rep):
#         f(*args, **kwargs)

# run_print(print, 'life', 'is', 'good', sep='-', end='***\n', rep=10)

def time_it(f, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        f(*args, **kwargs)
    end = time.perf_counter()
    avg_time = (end-start) / rep
    return f'Average time: {avg_time}.'

# print(time_it(print, 'printing', 'a', 'bunch', end='***\n', rep=1000))

def time_for_loop(n, *, start=1, end):
    # For loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def time_list_comp(n, *, start=1, end):
    # List comprehension
    return [n**i for i in range(start, end)]

def time_generators_exp(n, *, start=1, end):
    # Generators expression
    return list((n**i for i in range(start, end)))

print(time_it(time_for_loop, 2, start=0, end=20000, rep=5))
print(time_it(time_list_comp, 2, start=0, end=20000, rep=5))
print(time_it(time_generators_exp, 2, start=0, end=20000, rep=5))