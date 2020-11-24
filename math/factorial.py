# 0=1, 1=1, 2=2, 3=6

# def fact_rec(n):
#     return 1 if n < 2 else n * fact_rec(n-1)

# print(fact_rec(2))
# print(fact_rec(5))
# print(fact_rec(10))
# print(fact_rec(1))
# print(fact_rec(0))

# def fact_loop(n):
#     if n < 2:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n+1):
#             result *= i
#         return result

# print(fact_loop(2))
# print(fact_loop(5))
# print(fact_loop(10))
# print(fact_loop(1))
# print(fact_loop(0))

from functools import reduce

# def fact_reduce(n):
#     if n < 2:
#         return 1
#     else:
#         return reduce(lambda a, b: a * b, range(1, n+1))

# print(fact_reduce(2))
# print(fact_reduce(5))
# print(fact_reduce(10))
# print(fact_reduce(1))
# print(fact_reduce(0))