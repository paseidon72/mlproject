class Router:
    def __init__(self):
        self.buffer = [] # список принятих от серверов пакетов (обьектов класа Data)
        self.servers = {} # локальний словарь

    def link(self, server):
        self.servers[server.ip] = server # подключили сервер к роутеру
        server.router = self

    def unlink(self, server):
        s = self.servers.pop(server.ip, False) # удаляем сервер из словаря по ip адресу
        if s: # обнуляем атрибут router если сервер бил удален
            s.router = None

    def send_data(self):
        for d in self.buffer: # перебираем все информ. пакета (обьекти d класа Data)
            if d.ip in self.servers: # если в словаре есть ключ с d.ip
                self.servers[d.ip].buffer.append(d) # обращаемся к серверу и отправляем ему пакет append(d)
        self.buffer.clear() # в конце очищаем сам буфер

class Server:
    server_ip = 1 # каждий новий обьект будет содержать свой ip
    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        if self.router: # если router не None
            self.router.buffer.append(data) # добавляем в него инфопакет data

    def get_data(self):
        b = self.buffer[:] # создаем копию буфера
        self.buffer.clear() # очищаем буфер
        return b # возвращаем список из входних пакетов и очищаем буфер

    def get_ip(self):
        return self.ip # возвращаем адрес сервера

class Data:
    def __init__(self, msg, ip): # передаем сообщение и адрес назначнения
        self.data = msg
        self.ip = ip

