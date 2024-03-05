from random import randint
import sys
# class Money:
#     def __init__(self, value):
#         self.money = value
#
# my_money = Money(100)
# yor_money = Money(1000)
# print(my_money.__dict__)
# print(yor_money.__dict__)
####################################
# class Point:
#     def __init__(self, x , y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
# points = [Point(2*i+1, 2*i+1) for i in range(0, 1000)] # создаем 1000 обьектов с координатами где каждая увеличив на 2
# и сохраняем в список
# points[1].color = 'yellow'
#######################################
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4)for n in range(217)] # формируем 217 обьектов класа в случайном порядке
# for obj in elements: # обнулям координати для класа Line
#     if isinstance(obj, Line):
#         obj.sp = obj.ep = 0, 0
##############################################################
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))): # проверка (а в с) ето числа
#             return 1
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))): # проверка (а в с) положительние числа
#             return 1
#         a, b, c = self.a, self.b, self.c
#         if a >= b+c or b >= a+c or c >= a+b: # проверка (а в с) не могут бить сторонами треугольника
#             return 2
#         return 3
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
####################################################################
# class Graph:
#     def __init__(self, data):
#         self.data = data[:] # создаем копию списка которий передаем,для каждого свой
#         self.is_show = True
#
#     def set_data(self, data):
#         self.data = data[:]
#
#     def _get_str_data(self): # вспомагательная функция
#         return " ".join(map(str, self.data)) # передаем строку через пробел
#
#     def _show_closed_graph(self): # вспомогательная функция
#         print("Отображение даних закрито")
#
#     def show_table(self): # визов вспомагательной функции
#         if self.is_show:
#             print(self._get_str_data())
#         else:
#             self._show_closed_graph()
#
#     def show_graph(self): # визов вспомагательной функции
#         if self.is_show:
#             print(f"Графическое отображение даних {self._get_str_data()}")
#         else:
#             self._show_closed_graph()
#
#     def show_bar(self): # визов вспомагательной функции
#         if self.is_show:
#             print(f"Столбчатая диаграма {self._get_str_data()}")
#         else:
#             self._show_closed_graph()
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
# data_graph = list(map(int, input().split()))
# gr =Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()
#########################################################
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slot = 4
#         self.mem_slot = mems[: self.total_mem_slot] # список обьектов класа Memory макимум значений не больше total_mem_slot
#
#     def get_config(self): # возвращает список из строк
#         return [f'Материнская плата: {self.name}',
#                 f'Центральний процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slot}',
#                 'Память:' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slot))]
#
# md = MotherBoard('Gigabayt', CPU('Intel', 2000), Memory('Kingston', 1000), Memory('Kingston', 2000))
######################################################################
# class Cart:
#     def __init__(self):
#         self.goods = [] # создали  список
#
#     def add(self, gd):
#         self.goods.append(gd) # добавили в список значения
#
#     def remove(self, indx):
#         self.goods.pop(indx) # удалили из зписка значения
#
#     def get_list(self):
#         return [f'{x.name}: {x.price}' for x in self.goods] # получили список
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
######################################################################################
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
# lst_in = list(map(str.strip, sys.stdin.readlines())) # считивание спска из входного потока
# # формируем односвязний список
# head_obj = ListObject(lst_in[0]) # передаем первую строку из входного потока
# obj = head_obj # формируем вспомагательную переменную
# for i in range(1, len(lst_in)): # перебираем оставшиеся строки по индексам
#     obj_new = ListObject(lst_in[i]) # создаем новие обьекти по каждой строке
#     obj.link(obj_new) # соединяем обьекти добавляя новий в конец
#     obj = obj_new # предпоследний обьект будет ссилаться на последний всегда в цикле
#####################################################################################
# class Cell:
#     def __init__(self, around_mines=0, mine=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = True
# class GamePole:
#     def __init__(self, N, M):
#         self._n = N
#         self._m = M
#         self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)] # формируем двумерное поле
#         self.init()
#
#     def init(self): # установка мин на игровом поле случайним образом
#         m = 0 # количество раставлених мин
#         while m < self._m:
#             i = randint(0, self._n - 1) # генерируем координати на поле
#             j = randint(0, self._n - 1)
#             if self.pole[i][j].mine: # если мина есть продолжаем
#                 continue
#             self.pole[i][j].mine = True # если нет устанавливаем
#             m =+ 1 # увеличиваем на 1 чтоби избежать вечний цикл
#                 # подсчет количество мин вокруг клеток где нет мин
#         indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self._n): # проверяем наличие мин и их количество
#             for y in range(self._n):
#                 if not self.pole[x][y].mine: # если в текущей клетке нет мини
#                     mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i <= self._n and 0 <= y+j <= self._n)) # условие чтоби не вийти за граници поля
#                     self.pole[x][y].around_mines = mines # присваиваем значение по умолчанию
#
#     def show(self):
#         for row in self.pole: # перебираем вложение списки
#             # виводим клетки откритие закритие с минами
#             print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))
#
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()
####################################################################
