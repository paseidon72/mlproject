# class RealValue: # дескриптор даних
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
# class Point:
#     x = RealValue()
#     y = RealValue()
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1.5, 2.3)
# pt.__dict__['x'] = 10
# print(pt.x, pt.__dict__)
#############################################################
# class StringFaild: # дескриптор даних
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
# class DataBase:
#     x = StringFaild()
#     y = StringFaild()
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# db = DataBase('hi', 'low')
# db.__dict__['x'] = 'top'
# print(db.x, db.__dict__)
#####################################################
# class FloatValue: # дескриптор даних
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __set__(self, instance, value):
#         if type(value) != float:
#             raise TypeError('Присвоить можно только вещественние числа')
#         instance.__dict__[self.name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
# class Cell:
#     value = FloatValue()
#     def __init__(self, value=0.0):
#         self.value = value
#
# class TableSheet:
#     def __init__(self, N, M):
#         self.cells = [[Cell() for _ in range(M)] for _ in range(N)] # генератор вложеного списка (М строк, N столбцов)
#
# table = TableSheet(5, 3)
# n = 1.0
# for i in range(5):
#     for j in range(3):
#         table.cells[i][j].value = n
#         n += 1.0
###########################################
# class ValidateString:
#     def __init__(self, min_length=3, max_length=100):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def validate(self, string): # проверяем что ето строка  размер от и до
#         return type(string) == str and self.min_length <= len(string) <= self.max_length
#
# class StringValue: # дескриптор даних
#     def __init__(self, validator):
#         self.validator = validator
#
#     def __set_name__(self, owner, name): # формируем имена атрибутов дискриптора
#         self.name = '_' + name
#
#     def __get__(self, instance, owner): # возвращаем созданий атрибут
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.validator.validate(value): # проверяем прохождение проверки и добавляем значение
#             setattr(instance, self.name, value)
#
# class RegisterForm:
#     login = StringValue(validator=ValidateString())
#     password = StringValue(validator=ValidateString())
#     email = StringValue(validator=ValidateString())
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         print(f'<form>\n Логин: {self.login}\n Пароль: {self.password}\n Почта: {self.email}</form>')
###########################################################################
# class StringValue: # дескриптор даних
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#
#     def __set_name__(self, owner, name): # формируем имена атрибутов дискриптора
#         self.name = '_' + name
#
#     def __get__(self, instance, owner): # возвращаем созданий атрибут
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value): # проверяем и добавляем значение
#         if type(value) == str and self.min_length <= len(value) <= self.max_length:
#             setattr(instance, self.name, value)
#
# class PriceValue:
#     def __init__(self, max_value):
#         self.max_value = max_value
#
#
#     def __set_name__(self, owner, name): # формируем имена атрибутов дискриптора
#         self.name = '_' + name
#
#     def __get__(self, instance, owner): # возвращаем созданий атрибут
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value): # проверяем и добавляем значение
#         if type(value) in (int, float) and 0 <= value <= self.max_value:
#             setattr(instance, self.name, value)
#
# class Product:
#     name = StringValue(2, 50)
#     price = PriceValue(10000)
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class SuperShop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         if product in self.goods:
#             self.goods.remove(product)
###############################################################
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__things = []
#
#     @property # обьект свойство для доступа к __things только чтение без записи
#     def things(self):
#         return self.__things
#
#     def add_things(self, thing): # добавление
#         s = self.get_total_weigth()
#         if s + thing.weight <= self.max_weight:
#             self.__things.append(thing)
#
#     def remove_things(self, indx): # удаление по индексу
#         self.__things.pop(indx)
#
#     def get_total_weigth(self): # сумарний вес всех вещей
#         return sum(t.weigth for t in self.__things)
#######################################################
class Telecast:
    def __init__(self, uid, name, duration):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        t_lst = tuple(filter(lambda x: x.uid == indx, self.items)) # кортеж из удаляемих обьектов

        for t in t_lst: # удаляем по индексу
            self.items.remove(t)


