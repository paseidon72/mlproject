from random import randint

# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):
#         n = randint(self.min_length, self.max_length) # длина пароля
#         len_chars = len(self.psw_chars)
#
#         return "".join(self.psw_chars[randint(0, len_chars - 1)] for _ in range(n))# генератор паролей из
#     # символов psw_chars и цифр range(n) длиной len_chars - 1
# rnd = RandomPassword('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!_@#$%&*', 7, 20)
# lst_pass = rnd()
# print(lst_pass)
#####################################################
# class ImageFileAcceptor:
#     def __init__(self, extensions):
#         self.extensions = extensions
#
#     def __call__(self, name, *args, **kwargs):
#         start = name.rfind('.') # ищем индекс ближайшей точки с конца -1 ненайдена, любое положительное найдена
#         ext = "" if start == -1 else name[start + 1:] # виделяем расширение из имени файла где start == -1 расширения нет
#         # name[start + 1:] расширение есть, start сама точка
#         return ext in self.extensions # проверка расширение входит в одно из искомих расширений
############################################
# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""
#
#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")
#
#     def is_validate(self):
#         if not self.validators:
#             return True
#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False
#         return True
#
# class LengthValidator:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, string, *args, **kwargs):
#         return self.min_length <= len(string) <= self.max_length # проверяет длину даних в строке string от и до
#
# class CharsValidator:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string, *args, **kwargs):
#         return set(string) <= set(self.chars) # если символи строки string входят в множество chars
###############################################################
# class DigitRetrieve:
#     def __call__(self, string, *args, **kwargs):
#         if string[0] == "-": # если в строке первий символ "-"
#             if string[1:].isdigit(): # если строка без "-" содержит целие числа
#                 return int(string) # тогда ето целое отрицательное число
#             elif string.isdigit(): # если строка состоит только из чисел
#                 return int(string) # тогда ето целое положительное число
#             return None # все остальние варианти вернем None
########################################################
# class RenderList:
#     def __init__(self, type_list):
#         # если значения параметра type_list не ("ul", "ol") тогда применяется тег "ul"
#         self.type_list = type_list if type_list in ("ul", "ol") else "ul"
#
#     def __call__(self, lst, *args, **kwargs):
#         # вернем многострочную строку в формате html где "х" обьекти списка "lst" кот ми передаем
#         return "\n".join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', lst), f'</{self.type_list}>'])
######################################################
# class HandlerGet: # клас декоратор с силкой func на декарируемую функцию
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, request, *args, **kwargs):
#         m = request.get('method', 'GET') # в словаре request берем ключ 'method' если его нет берем ключ 'GET'
#         if m == 'GET': # если m соответсвует ключу 'GET'
#             return self.get(self.func, request) # визовем вспом метод для обраб запроса, передаем ему функц и словарь
#         return # не проходит проверка вернем None
#
#     def get(self, func, request, *args, **kwargs): # метод обработки 'get' запроса
#         return f'GET: {func(request)}' # возвращаем строку в нужном формате
#####################################################
# class Handler: # клас декоратор с параметрами
#     def __init__(self, methods=('GET', )):
#         self.__methods = methods
#
#     def __call__(self, func, *args, **kwargs): # в етом методе реализуем декоратор
#         def wrapper(request): # обертка передает словарь
#             m = request.get('method', 'GET') # в словаре request берем ключ 'method' если его нет берем ключ 'GET'
#             if m in self.__methods:# если значение m есть в списке разрешених методов __methods
#                 method = m.lower() # переводим строки в нижний регистр
# #берем атрибут класа по имени (method) передаем ему силку на декарируемую функцию и словарь запроса (func, request) для обработки
#                 return self.__getattribute__(method)(func, request)
#         return wrapper # вернем силку на внутренюю функцию
#
#     def get(self, func, request, *args, **kwargs):
#         return f'GET: {func(request)}' # вернем обработку GET запроса
#
#     def post(self, func, request, *args, **kwargs):
#         return f'POST: {func(request)}' # вернем обработку POST запроса
############################################################
# class InputDigits:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return list(map(int, self.func().split()))# получаем список из целих чисел
#
# input_bg = InputDigits(input) # задекорировали стандартную функцию input
# res = input_bg() # визвая декорировану функ input вводя значения через пробел получим список
# print(res)
#########################################################
class RenderDigit:
    def __call__(self, string, *args, **kwargs):
         try:# если в строке есть целие числа вернем их из строки
             return int(string)
         except:# остальное вернем None
             return None

class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
#визиваем обьекти класа RenderDigit через self.__render в декарируемую функ передаем парам и рабиваем по пробелам
# func(*args, **kwargs).split() сохраняем все в список list(map)
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper

render = RenderDigit() # обьект класа
input_bg = InputValues(render)(input) #передаем параметр и декарируем функцию input
res = input_bg()



