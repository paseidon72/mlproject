# class Car:
#     def __init__(self): # создаем локальную переменную
#         self.__model = None
#
#     @property
#     def model(self): # возвращаем локальную переменную
#         return self.__model
#
#     @model.setter
#     def model(self, value): # проверяем что єто строка в диапозоне от 2 до 100 и присваиваем новое значение
#         if type(value) == str and 2 <= len(value) <= 100:
#             self.__model = value
#####################################################
# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width = self.__height = None # для дальнейшей проверки и изменения даних сразу для двух атрибутов
#         self.height = height # тут само присвоєние даних
#         self.width = width # тут само присвоєние даних
#
#     @property
#     def width(self): # возвращает локальний атрибут
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if type(value) == int and 0 <= value <= 10000: # проверяем и присваиваем значение локальному атрибуту
#             if self.__width: # если аргумент не None  визиваем свойство show()
#                 self.show()
#             self.__width = value
#
#     @property
#     def height(self): # возвращает локальний атрибут
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if type(value) == int and 0 <= value <= 10000: # проверяем и присваиваем значение локальному атрибуту
#             if self.__height: # если аргумент не None  визиваем свойство show()
#                 self.show()
#             self.__height = value
#
#     def show(self):
#         print(f'{self.__title}: {self.__width}, {self.__height}')
###############################################################
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj): # если __next силается на обьект класа StackObj или None
#         if isinstance(obj, StackObj) and obj is None:
#             self.__next = obj
#
# class Stack:
#     def __init__(self):
#         self.top = None # силается на первий обьект односвязного списка
#         self.last = None # силается на последний обьект односвязного списка
#
#     def push(self, obj):
#         if self.last:
#             self.last.next = obj # перенаправляем силку с None на добавляемий обьект obj
#
#         self.last = obj
#         if self.top is None:
#             self.top = obj # при добавлении самого первого обьекта top уже силается на obj
#
#     def pop(self):
#         h = self.top
#         if h is None: # если нет обьектов удалять нечего
#             return
#         while h and h.next != self.last: # доходим до последнего обьекта
#             h = h.next # присваиваем силку на предпоследний обьект
#         if h:
#             h.next = None # если предпоследний обьект есть перенаправляем его силку на None
#         last = self.last # удаляемий обьект ми его возвращаем return last
#         self.last = h
#         if self.last is None: # если удаляем самий последний обьект списка то top должен силаться на None
#             self.top = None
#         return last
#
#     def get_data(self):
#         s = []
#         h = self.top
#         while h: # перебираем с первого обьекта односвязного списка
#             s.append(h.data) # добавляем атрибут data в список
#             h = h.next # переходим к следующему обьекту односвязного списка
#         return s # возвращаем список атрибутов data
##################################################################
# class RadiusVector2D:
#     MIN_CORD = -100
#     MAX_CORD = 1024
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def __is_verify(cls, value): # вспомагательний приватний метод класа для проверки
#         return type(value) in (int, float) and cls.MIN_CORD <= value <= cls.MAX_CORD
#
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__is_verify(value):
#             self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__is_verify(value):
#             self.__y = value
#
#     @staticmethod
#     def norm2(vector): # вичисление квадратической норми обьекта класа RadiusVector2D
#         return vector.x * vector.x + vector.y * vector.y
##################################################################
# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.index = indx
#         self.value = value
#         self.left = self.right = None
#
#     @property
#     def left(self): # возвращает приватний атрибут
#         return self.__left
#
#     @left.setter
#     def left(self, obj): # присваиваем аргумент локальному свойству left
#         self.__left = obj
#
#     @property
#     def right(self): # возвращает приватний атрибут
#         return self.__right
#
#     @right.setter
#     def right(self, obj): # присваиваем аргумент локальному свойству right
#         self.__right = obj
#
# class DecisionTree:
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node: # усли node не None добавляем некорневой обьект
#             if left: # проверяем left
#                 node.left = obj # если он True присваиваем значение obj левая ветвь
#             else:
#                 node.right = obj # иначе к правой ветви
#         return obj # возвращает новий добавленний обьект
#
#     @classmethod
#     def predict(cls, root, x):
#         obj = root # первий корневой обьект дерева
#         while obj:
#             obj_next = cls.get_next(obj, x) # силается на следующий обьект решающего дерева
#             if obj_next is None:
#                 break # проходим по дереву пока не дойдем до лист. вершини кот. силается на None
#             obj = obj_next
#         return obj.value # хранит одну из строк листовой вершини
#
#     @classmethod
#     def get_next(cls, obj, x): # первий обьект obj  у кот. есть индекси [0, 1, 2]
#         if x[obj.index] == 1: # если значение Х по индексу 1 идем по левой ветви
#             return obj.left
#         return obj.right # нет по правой
###########################################################################
# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class PathLines:
#     def __init__(self, *args):
#         self.coords = list((LineTo(0, 0),) + args) # список из всех переданих обьекто LineTo начиная с координати (0, 0)
#
#     def get_path(self):
#         return self.coords[1:] # возвращает все обьекти исключая первий LineTo(0, 0)
#
#     def get_length(self):
#         g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords))) # генератор видает координати
#         # точек отрезков начало и конец начиная с координати LineTo(0, 0)
#         return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g)) # подсчет длини
#         # всех линейних сегментов, длина каждого опред. как Евклидово растояние
#
#     def add_line(self, line):
#         self.coords.append(line) # добавляем новий линейний сегмент в конец маршрута
###########################################
class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, indx):
        self.phones.pop(indx)

    def get_phone_list(self):
        return self.phones



