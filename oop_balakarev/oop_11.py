# class ObjList:
#     def __init__(self, data):
#         self.__data = "" # начальное значение
#         self.data = data
#         self.__next = self.__prev = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         if type(value) == str:# если тип переменной str тогда присваиваем значение
#             self.__data = value
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, obj):
#         if type(obj) in (ObjList, type(None)):# если тип obj соответсвует текущему класу ObjList или type(None)
#             # тогда присваиваем значение
#             self.__prev = obj
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, obj):
#         if type(obj) in (ObjList, type(None)):
#             self.__next = obj
#
# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None
#
#     def add_obj(self, obj):
#         obj.prev = self.tail # установили связь последнего обьекта с добавляемим в конец
#
#         if self.tail:# если силается на существующий обьект
#             self.tail.next = obj # создали вторую связь последнего обьекта с добавляемим в конец
#         self.tail = obj # перемещаем tail на послендий обьект
#
#         if not self.head: # если head принимает значение None
#             self.head = obj # тогда head присвоим значение obj, добавим обьект перед первим в начало
#
#     def get_obj_by_index(self, indx):# для взятия обьекта по индексу
#         h = self.head # берем первий обьект
#         n = 0 # счетчик
#         while h and n < indx:# пока виполняется условие
#             h = h.next # переходим к следующему обьекту
#             n += 1 # увеличиваем на 1
#         return h # вернем h по индексу
#
#     def remove_obj(self, indx):
#         obj = self.get_obj_by_index(indx) # вибираем обьект по индексу
#         if obj is None: # если принимает значение None то удалять нечего
#             return
#
#         p, n = obj.prev, obj.next # силаются на предидущий и следующий после удаляемого обьекта
#         if p: # если силается на существующий обьект
#             p.next = n # настроим связь между седующим и предидущим после удаляемого обьекта
#         if n: # если силается на существующий обьект
#             n.prev = p # настроим связь между предидущим и следующим после удаляемого обьекта
#
#         if self.head == obj: # если силается на удаляемий обьект
#             self.head = n # присваиваем значение следующего обьекта
#
#         if self.tail == obj: # если силается на удаляемий обьект
#             self.tail = p # присваиваем значение предидущего обьекта
#
#     def __len__(self): # подсчет количество обьектов в связаном списке
#         n = 0
#         h = self.head
#         while h:
#             n += 1
#             h = h.next
#         return n
#
#     def __call__(self, indx, *args, **kwargs):
#         obj = self.get_obj_by_index(indx) # берем обьект по индексу
#         return obj.data if obj else None # вернем obj.data если обьект существует иначе None
###############################################################
# class Complex:
#     def __init__(self, real, img):
#         self.__real = self.__img = 0
#         self.real = real
#         self.img = img
#
#     @property
#     def real(self):
#         return self.__real
#
#     @real.setter
#     def real(self, value):
#         if type(value) not in (int, float): # если тип значения невходит в (int, float)
#             raise ValueError('неверний тип даних')
#         self.__real = value
#
#     @property
#     def img(self):
#         return self.__img
#
#     @img.setter
#     def img(self, value):
#         if type(value) not in (int, float): # если тип значения невходит в (int, float)
#             raise ValueError('неверний тип даних')
#         self.__img = value
#
#     def __abs__(self): # возвращает модуль комплексного числа
#         return (self.__real * self.__real + self.__img * self.__img) ** 0.5
#
# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)
#############################################################
class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0: # если длина равна 0, передан 1 аргумент
            self.__coords = [0] * arg1 # количество 0 дожно соотв размерности arg1
        else:
            self.__coords = [arg1] + list(args) # состоит из переданих координат

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords)) # определяем длину переданих значений
        self.__coords[:n] = args[:n]

