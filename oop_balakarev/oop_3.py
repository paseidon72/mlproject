# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return 'Нельзя создать обьект класса'
#
# obj = AbstractClass()
# print(obj)
##########################################
# етот клас создает только первие 5 обьектов потом всегда возвращает силку на последний 5й обьект
# class SingletonFive:
#     __instance = None # силается на последний созданий екземпляр класа
#     __count = 0 # определяет количество созданих обьектов класа
#     def __new__(cls, *args, **kwargs):
#         if cls.__count < 5: # пока виражение верно
#             cls.__instance = super().__new__(cls) # создаем обект и силку передаем в переменую
#             cls.__count += 1 # увеличиваем счетчик на 1
#         return cls.__instance # возвращаем силку на обьект класа
#
#     def __init__(self, name):
#         self.name = name
# obj = [SingletonFive(str(n)) for n in range(10)]
###################################################
# TYPE_OS = 1
# class DialogWindows:
#     name_class = 'DialogWindows'
#
# class DialogLinux:
#     name_class = 'DialogLinux'
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if TYPE_OS == 1:
#             obj = super().__new__(DialogWindows) # переопределяем метод и указиваем обьект какого класа нужно создать
#         else:
#             obj = super().__new__(DialogLinux)
#         obj.name = args[0]
#         return obj
# obj = Dialog('next')
# print(obj)
###########################################################
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self): # создает копию текущего обьекта с локальними атрибутами
#         return Point(self.x, self.y)
# pt = Point(1, 2)
# pt_clone = pt.clone()
##################################################################
# class Factory:
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         return float(string)
#
# class Loader:
#     def pars_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(','):
#             item = factory.build_number(sub)
#             seq.append(item)
#         return seq
# ld = Loader()
# s = input()
# res = ld.pars_format(s, Factory())
# print(res)
#####################################################
