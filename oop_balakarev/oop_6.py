from random import randint
from string import ascii_lowercase, digits, ascii_uppercase
# class Cloc:
#     def __init__(self, tm):
#         self.__time = 0 # присваиваем начально значение
#         if self.__check_time(tm): # визиваем проверку
#             self.__time = tm
#
#     @classmethod
#     def __check_time(cls, tm): # проверяем что ето число в диапозоне
#         return type(tm) == int and 0 <= tm < 100000
#
#     def set_time(self, tm):
#         if self.__check_time(tm): # визиваем проверку
#             self.__time = tm # устанавливаем текущее время
#
#     def get_time(self):
#         return self.__time # получаем значение приватной локальной переменной
###################################################################
# class Money:
#     def __init__(self, mn):
#         self.__money = 0
#         if self.__check_money(mn):
#             self.__money = mn
#
#     @classmethod
#     def __check_money(cls, mn):
#         return type(mn) == int and mn >= 0
#
#     def set_money(self, money):
#         if self.__money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.get_money()
####################################################################
# class Book:
#     def __init__(self, title, author, price):
#         self.__title = title
#         self.__author = author
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price
##########################################################################
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.set_coords(x1, y1, x2, y2)
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(*self.get_coords())
#############################################################
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
# class Rectangel:
#     def __init__(self, a, b, c=None, d=None):
#         self.__sp = self.__ep = None # если параметри не силается на обьект класа Point
#         if isinstance(a, Point) and isinstance(b, Point): # если єто обьекти класа Point
#             self.__sp = a
#             self.__ep = b # формируем прямоугольник через клас Point
#         elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))): # если все числа
#             self.__sp = Point(a, b)
#             self.__ep = Point(c, d) # формируем прямоугольник таким способом
#
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')
# rect = Rectangel(0, 0, 20, 34)
# rect.draw()
##############################################################
# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = self.__prev = None
#
#     def set_next(self, obj):
#         self.__next = obj
#
#     def set_prev(self, obj):
#         self.__prev = obj
#
#     def get_next(self):
#         return self.__next
#
#     def get_prev(self):
#         return self.__prev
#
#     def set_data(self, data):
#         self.__data = data
#
#     def get_data(self):
#         return self.__data
#
# class LinkedList:
#     def __init__(self):
#         self.had = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if self.tail:
#             self.tail.set_next(obj) # передаем связь на новий обьект
#         obj.set_prev(self.tail) # устанавливаем связь нового обьекта с последним
#         self.tail = obj # переопределяем атрибут и новий обьект становиться (tail)
#         if not self.had: # если первий обьект не None ми его инициализируем, если да то неменяем
#             self.had = obj
#
#     def remove_obj(self):
#         if self.tail is None: # если нет обьектов для удаления
#             return
#         prev = self.tail.set_prev()
#         if prev: # если есть предидущий обьект присвоить ему (None)
#             prev.set_next(None)
#         self.tail = prev  # переопределяем атрибут и предпоследний обьект становиться (tail)
#         if self.tail is None:
#             self.had = None # если обьектов в списке больше нет
#
#     def get_data(self):
#         s = []
#         h = self.had # силается на первий обьект
#         while h:
#             s.append(h.get_data()) # пока h не равен None добавляем строку в s
#             h = h.get_next() # переходим на следующий обьект связаного списка
#         return s # возвращаем список
##############################################################
class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + '_.@' # для проверки допустимости символов в email
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + '_' # для генерации email

    def __new__(cls, *args, **kwargs):
        return None # запрещаем создавать екземпляри класа

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email): # проверяем что email строка
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False # если в email входят запрещение символи возвращаем False
        s = email.split('@')
        if len(s) != 2:
            return False # если @ нет или больше одной возвращаем False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False # если длина до @ больше 100 и после @ больше 50 вернем False
        if '.' not in s[1]:
            return False # если точки нет после @ вернем False
        if email.count('..') > 0:
            return False # усли есть две точки подряд вернем False
        return True

    @staticmethod
    def __is_email_str(email): # возвращает True если email строка
        return type(email) == str

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20) # вибираем число символов до @
        length = len(cls.EMAIL_RANDOM_CHARS) - 1 # определим длину колекции
        return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + 'gmail.com' # гунератор случайного email






