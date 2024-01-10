# class User:
#     count = 1
#
#     __slots__ = ("name", "age")
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User('max', 15)
#
# print(user.name)
# print(user.age)
# user.status = True
# print(user.status)
#
# print(User.count)


# class User:
#     __count = 1
#
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         print(self.__name)
#
#
# user = User('Max')
# print(user._User__name)
#
# print(User._User__count)


# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#
# class Tools:
#     def greeting(self):
#         print('hello')
#
#
# class SuperCar(Car, Tools):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#
#         self.model = model
#
#
# car = SuperCar('Mercedes', 's2')
#
# car.greeting()


# class User:
# #     def __init__(self, name, age):
# #         self.__name = name
# #         self.age = age
# #
# #     def __get_name(self):
# #         return self.__name
# #
# #     def __set_name(self, name):
# #         self.__name = name
# #
# #     def __del_name(self):
# #         del self.__name
# #
# #     name = property(fget=__get_name, fset=__set_name, fdel=__del_name)
#
# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max', 15)
# print(user.name)
# user.name = 'Karina'
# print(user.name)
# del user.name
# print(user.name)
# # print(user.get_name())
# # user.set_name('Karina')
# # print(user.get_name())
# # user.del_name()
# # print(user.get_name())


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return self.b + self.a
#
#     def area(self):
#         return self.a * self.b
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         return self.a * self.b + self.c
#
#
# shapes: list[Shape] = [
#     Triangle(1, 2, 3),
#     Rectangle(2, 3),
#     Triangle(3, 4, 5)
# ]
#
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())


# class User:
#     __count = 0
#
#     @classmethod
#     def inc_count(cls):
#         cls.__count += 1
#
#     @classmethod
#     def print_count(cls):
#         print(cls.__count)
#
#     @staticmethod
#     def hello():
#         print('Hello World!')
#
#
# User.print_count()
# User.inc_count()
# User.print_count()
# User.hello()
#
# user = User()
# user.hello()

# from typing import Self
#
# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other:Self):
#         return other.age * self.age
#
#     def __str__(self):
#         return f'{self.name} -- {self.age}'
#
#     def __len__(self):
#         return len(self.name)


# user = User('max', 15)
# user2 = User('kira', 2)
# user3 = User('kira', 3)
# # print(user.age)
# # print(user.name)
# # print(user)
#
# print(user + user2)
# print(user - user2)
# print(len(user))


# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# user1 = User('Max')
# user2 = User('Kira')
# user3 = User('Oleh')
#
# print(user1.name)
# print(user2.name)
# print(user3.name)


# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, new_value):
#         self.value += new_value
#
#
# prod = Prod(555)
#
# print(prod.value)
# prod(1000)
#
# print(prod.value)

# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other):
#         return other.age * self.age
#
#     def __str__(self):
#         return f'{self.name} -- {self.age}'
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __len__(self):
#         return len(self.name)
#
#
# user1 = User('max', 15)
# user2 = User('Kira', 8)
#
# print(user1)
# print(user2)

# print([user1, user2])


class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


arr = Array(2, 8, 7, 9, 10)

# print(len(arr))

arr[1] = 555
print(arr)
print(arr[0])
arr.push(777)
print(arr)

arr_map = arr.map(lambda x: x * -1)
print(arr_map)

arr_filter = arr.filter(lambda x: x < 10)

print(arr_filter)

