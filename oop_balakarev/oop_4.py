from string import ascii_lowercase, digits
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def pars_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(','):
#             item = factory.build_number(sub)
#             seq.append(item)
#         return seq
# res = Loader.pars_format('1, 2, 3', Factory)
#######################################################
# class TextInput:
#     CHARS = "йцукенгшщзхїфівапролджєячсмитьбю" + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     def __init__(self, name, size=10):
#         self.check_name(name) # визиваем @classmethod
#         self.name = name
#         self.size = size
#
#     def get_html(self): # возвращает строку в html формате
#         return f"<p class='login>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod  # проверяет коректность переданого имени name
#     def check_name(cls, name):
#         if type(name) != str or len(name) <3 or len(name) >50: # проверка если єто не строка или по длине
#             raise ValueError("неправильное поле name")
#         if not set(name) < set(cls.CHARS_CORRECT): # проверка соответствия символов значениям глобальних перемених через множество
#             raise ValueError("неправильное поле name")
#
# class PasswordInput:
#     CHARS = "йцукенгшщзхїфівапролджєячсмитьбю" + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     def __init__(self, name, size=10):
#         self.check_name(name) # визиваем @classmethod
#         self.name = name
#         self.size = size
#
#     def get_html(self): # возвращает строку в html формате
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod  # проверяет коректность переданого имени name
#     def check_name(cls, name):
#         if type(name) != str or len(name) <3 or len(name) >50: # проверка если єто не строка или по длине
#             raise ValueError("неправильное поле name")
#         if not set(name) < set(cls.CHARS_CORRECT): # проверка соответствия символов значениям глобальних перемених через множество
#             raise ValueError("неправильное поле name")
#
# class Formlogin:
#     def __init__(self, lgn, psv):
#         self.login = lgn
#         self.password = psv
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#################################################################
# class CardCheck:
#     CHARS_FO_NAME = ascii_lowercase.upper() + digits
#
#     @classmethod
#     def check_cart_number(cls, number):
#         if type(number) != str: # проверяем что номер ето сторока
#             return False
#         s = number.split('-') # проверяем строка содержит 4 фрагмета через дефис (хххх-хххх-хххх-хххх)
#         if len(s) != 4:
#             return False
#         if not all(map(lambda x: len(x) == 4, s)): # проверяем длина каждого фрагмента 4 символа
#             return False
#         return all(map(lambda x: x.isdigit(), s)) # проверяем что ето все цифри
#
#     @classmethod
#     def check_name(cls, name):
#         if type(name) != str: # проверяем что номер ето сторока
#             return False
#         s = name.split() # проверяем строка содержит 2 фрагмета через пробел
#         if len(s) != 2:
#             return False
#         set_chars = set(cls.CHARS_FO_NAME)
#         return all(map(lambda x: set(x) < set_chars, s)) # проверка символов слова set(x) на вхождение
#      # в  CHARS_FO_NAME (все больше букви или цифри)
####################################################
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
# v1 = Video()
# v2 = Video()
# v1.create('python')
# v2.create('python oop')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)
#############################################################
# class AppStore:
#     def __init__(self):
#         self.apps = {} # словарь для хранения приложений
#
#     def add_application(self, app):
#         self.apps[id(app)] = app # добавляем приложение в словарь по id
#
#     def remove_application(self, app):
#         self.apps.pop(id(app)) # удаление приложения по id
#
#     def block_application(self, app):
#         obj = self.apps.get(id(app), False) # блокируем нужное приложение
#         if not obj:
#             return False
#         obj.blocked = True # если оно существует устанавливаем True
#         return True
#
#     def total_apps(self):
#         return len(self.apps) # возвращаем общее число приложений, длину словаря
#
# class Application:
#     def __init__(self, name):
#         self.name = name
#         self.blocked = False
################################################################
# class Viber:
#     msgs = {} # словарь для хранения сообщений
#     @classmethod
#     def add_message(cls, msg):
#         cls.msgs[id(msg)] = msg # добавляем сообщения
#
#     @classmethod
#     def remove_message(cls, msg): # удаление сообщений
#         key = id(msg)
#         if key in cls.msgs:
#             cls.msgs.pop(key)
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like # инвертируем булевие значения для лайков
#
#     @classmethod
#     def show_last_message(cls, number): # отображение последних сообщений
#         for n in type(cls.msgs.values())[-number:]:
#             print(n)
#
#     @classmethod
#     def total_message(cls):
#         return len(cls.msgs) # возвращаем общее число сообщений, длина словаря
#
# class Message:
#     def __init__(self, text): # позволяет создавать обьекти сообщения и лайки
#         self.text = text
#         self.fl_like = False
#################################################################
