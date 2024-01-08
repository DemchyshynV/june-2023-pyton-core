# l = [1,2]
#
#
# a,b = l
#
# print(a, b)

# tuple_1 = 1,2
#
# print(tuple_1)

#
# a = 5
# b = 7
#
# # res = a,b
# #
# # print(res)
#
# b, a = a, b
#
# print(b, a)


# l = [1, 2, 3, 4, 5, 6]
#
# a, b, *_, c = l
#
# print(a)
# print(b)
# print(c)
# print(_)


# l = [1,2,3,4]
#
# _,_, a,b = l
#
# print(a, b)


# l1=[1,2,3]
#
# l2 = [*l1]

# d = {
#     'name':'max',
#     'age':15
# }
#
# d2 = {**d}
#
# print(d2)

# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
# @decor
# @decor
# def greeting(a,b,c):
#     print(f'hello, {c} {b} {a}')
#

# inner = decor(greeting)
#
# inner()

# greeting('Max', 1,2)


# for i in range(5):
#     pass
#
# print(i)


# i = 666
#
# for j in range(5):
#     pass
#
# def a():
#     name = 'max'
#     print(locals())
#
# a()
#
#
# print(globals())

# name = 'Max'
#
#
# def a():
#     # name = 'Vasia'
#
#     def b():
#         # nonlocal name
#         global name
#         name = 'Petia'
#         print(locals())
#         # print(name)
#
#     b()
#     # print(name)
#
#
# a()
#
# print(name)


# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#
#     def reset():
#         nonlocal count
#         count=0
#
#     return inc, reset
#
#
# inc, reset = counter()
# inc2, reset2= counter()
#
# print(inc())
# print(inc())
# print(inc())
# print(inc())
# print(inc())
# print(inc2())
# reset()
# inc()


# l1 = [1,2,3,-1,6,8,9]
#
#
# # l.sort(reverse=True)
# l2 = sorted(l1)
#
# print(l1)
# print(l2)

# users = [
#     {'name': 'max', 'age': 15},
#     {'name': 'oleh', 'age': 23},
#     {'name': 'masha', 'age': 18},
#     {'name': 'dasha', 'age': 1},
#     {'name': 'katia', 'age': 25},
#     {'name': 'kira', 'age': 30},
#     {'name': 'karina', 'age': 12},
# ]
#
#
# # const func = (a)=>a*2
#
# # def func(item):
# #     return item['age']
# #
# #
# # func = lambda item:item['age']
#
# users.sort(key=lambda item:item['age'], reverse=True)
#
# print(users)


# a: str = 123
#
# print(a+2)
# d = {
#     'name':'max'
# }
#
# def func(string: list[str]) -> str | int:
#     return d


# t: tuple[int, ...] = (1, 1, 3)

# import typing
#
# typing.TypedDict

from typing import TypedDict, Callable


# User = TypedDict("User", {'name': str, 'age': int, 'status': bool}, total=False)
#
# user: User = {
#     "name": 'Max',
#     "status": False
# }
def counter() -> Callable[[str, int], int]:
    count = 0

    def inc(a: str, b: int) -> int:
        nonlocal count
        count += 1
        return count

    return inc
