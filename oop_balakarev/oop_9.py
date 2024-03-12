import time
# class Book:
#     attrs = {'title': str, 'author': str, 'pages': int, 'year': int} # словарь для проверки значений
#
#     def __init__(self, title="", author="", pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         # если ключ key есть в словаре и значения ключа key соответствуют типам даних type(value)
#         if key in self.attrs and self.attrs[key] == type(value):
#             super().__setattr__(key, value) # делаем присвоение даних
#         else:
#             raise TypeError ('неверний тип даних')
#
# book =Book()
####################################################
# class Product:
#     _id_instance = 1 # начальное значение атрибута класа
#     attrs = {'name': (str, ), 'weight': (int, float), 'price': (int, float)}
#
#     def __init__(self, name, weight, price):
#         self.id = Product._id_instance # обращаемся к атрибуту класа
#         Product._id_instance += 1 # увеличиваем на единицу
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __setattr__(self, key, value):
#         # если key входит в колекцию словаря attrs принимает одно из значений имен то тип значений должен принадлежать
#         # одному из кортежей
#         if key in self.attrs and type(value) in self.attrs[key]:
#             if (key == 'weight' or key == 'price') and value <= 0:
#                 raise TypeError('неверний тип даних')
#             elif key in self.attrs: # если неверний тип даних
#                 raise TypeError('неверний тип даних')
#             object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):# запрет на удаление локального атрибута id
#         if item == 'id':
#             raise TypeError('удаление запрещено')
#         object.__delattr__(self, item)
#
#
# class Shop:
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
###########################################################
# class LessonItem:
#     attrs = {'title': str, 'practices': int, 'duration': int}
#
#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if key in self.attrs: # если key принадлежит одному из атрибутов словаря
#             if type(value) != self.attrs[key]:# если тип присваиваемого значения не соотв типу кот должен бить
#                 raise TypeError('неверний тип даних')
#             if (key == 'practices' or key == 'duration') and value <= 0:
#                 raise TypeError('неверний тип даних')
#
#         super().__setattr__(key, value)
#
#     def __getattr__(self, item):# при обращении к несуществующим атрибутам LessonItem возвращает False
#         return False
#
#     def __delattr__(self, item):
#         if item is self.attrs:# запрет на удаление атрибутов словаря в обьектах класа
#             raise AttributeError()
#
#         super().__delattr__(item) # другие атрибути удаляются
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.pop(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_modul(self, modul):
#         self.modules.pop(modul)
#
#     def remove_modul(self, indx):
#         self.modules.pop(indx)
##############################################################################
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
#
# class Papyri:
#     def __init__(self, name, data, descr):
#         self.name = name
#         self.data = data
#         self.descr = descr
#
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         if obj in self.exhibits:
#             self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         ex = self.exhibits[indx]
#         return f'Описание експоната {ex.name}: {ex.descr}'
########################################################
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         # если обьекта такого типа нет в списке apps тогда ми его добавляем
#         if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
#             self.apps.append(app)
#
#     def remove_app(self, app):
#         if app in self.apps:
#             self.apps.remove(app)
#
# class AppVK:
#     def __init__(self):
#         self.name = 'В контакте'
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.memory_max = memory_max
#         self.name = 'YouTube'
#
# class AppPhone:
#     def __init__(self, phone):
#         self.name = 'Phone'
#         self.phone_list = phone
##################################################################
# class Circle:
#     attrs = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}
#
#     def __init__(self, x, y, radius):
#         self.__x = self.__y = self.__radius = None
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         self.__y = value
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         self.__radius = value
#
#     def __setattr__(self, key, value):
#         # если key входит в словарь и тип данних несоответствует нужн типу
#         if key in self.attrs and type(value) not in self.attrs[key]:
#             raise TypeError('неверний тип даних')
#         if key == 'radius' and value <= 0: # для радиуса если значение <=0 то присвоение неделаем
#             return
#         super().__setattr__(key, value)
#
#     def __getattr__(self, item):# при обращении к несуществующим атрибутам LessonItem возвращает False
#         return False
##################################################
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 100
#
#     def __init__(self, a, b, c):
#         self.__a = self.__b = self.__c = None
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @classmethod
#     def __is_verify(cls, value): # вспомагательний приватний метод класа для проверки
#         return type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
#
#     @property
#     def a(self):
#         return  self.__a
#
#     @a.setter
#     def a(self, value):
#         if self.__is_verify(value): # если проверка проходит
#             self.__a = value
#
#     @property
#     def b(self):
#         return  self.__b
#
#     @b.setter
#     def b(self, value):
#         if self.__is_verify(value):
#             self.__b = value
#
#     @property
#     def c(self):
#         return  self.__c
#
#     @c.setter
#     def c(self, value):
#         if self.__is_verify(value):
#             self.__c = value
#
#     def __setattr__(self, key, value): # запрет создания или замени атрибутов
#         if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
#             raise AttributeError('Менять атрибути нельзя')
#         super().__setattr__(key, value)
###############################################################
class GeyserClassic:
    MAX_DATA_FILTER = 100

    def __init__(self):
        self.filter_class = ('Mechanical', 'Aragon', 'Calcium')# кортеж для созд ключа по названию слота
        # описивает слоти номер и название куда ставить фильтр
        self.filters = {(1, self.filter_class[0]): None, (2, self.filter_class[1]): None, (3, self.filter_class[2]): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__) # формируем ключ словаря каждого слота
        if key in self.filters and not self.filters[key]: # если ключ сформирован правильно и по нему нет фильтра
            self.filters[key] = filter # добавляем фильтр в свой слот

    def remove_filter(self, slot_num):
        if type(slot_num) == int and 1 <= slot_num <= 3: # проверяем slot_num ето число
            key = (slot_num, self.filter_class[slot_num - 1]) # формируем ключ словаря каждого слота по названию слота
            if key in self.filters: # если key есть в словаре
                self.filters[key] = None # присваиваем None удаляем фильтр

    def get_filter(self):
        return tuple(self.filters.values()) # возвращаем кортеж фильтров в порядке установки

    def water_on(self):
        end = time.time() # текущее время
        for f in self.filters.values():# перебираем все фильтри
            if f is None:# если фильтр неустановлен
                return False
            start = f.data # текущее время фильтра
            if end - start > self.MAX_DATA_FILTER: # проверяем срок служби фильтра
                return False
        return True

class Mechanical:
    def __init__(self, data):
        self.data = data

    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__: # если ключ с именем 'data' есть в словаре ничего не меняем
            return
        super().__setattr__(key, value)

class Aragon:
    def __init__(self, data):
        self.data = data

    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__: # если ключ с именем 'data' есть в словаре ничего не меняем
            return
        super().__setattr__(key, value)

class Calcium:
    def __init__(self, data):
        self.data = data

    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__: # если ключ с именем 'data' есть в словаре ничего не меняем
            return
        super().__setattr__(key, value)






