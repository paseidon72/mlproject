from random import randint

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self): # вернет True если клетка свободна равна 0
        return self.value == 0

class TicTacToe:
    FREE_CELL = 0 # свободная клетка
    HUMAN_X = 1 # крестик (игрок человек)
    COMPUTER_O = 2 # крестик (игрок комп)
    def __init__(self):
        self._size = 3 # переменая для определения размера игрового поля
        self._win = 0 # 0 игра дальше, 1 победил человек, 2 победил комп, 3 ничья
        # игровое поле кортеж 3х3 каждий елемент обьект класа Cell() с размером поля for _ in range(self._size)
         # получаем вложений кортеж
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __check_index(self, index):
        # если тип не (tuple, list) и длина не равна 2, с индексами что-то не так
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('неправильние индекси')
        r, c = index # распокуем в перемение котртеж или список
        if not (0 <= r < self._size) or not (0 <= c < self._size):# если значения r, c не в диапазоне от 0 до self._size
            raise IndexError('неправильние индекси')

    def __update_win_status(self):
        for row in self.pole: # переберем строки
            if all(x.value == self.HUMAN_X for x in row): # если в текущей строке все крестики
                self._win = 1 # вииграл человек
                return
            if all(x.value == self.COMPUTER_O for x in row): # если в текущей строке все нолики
                self._win = 2 # вииграл комп
                return
        for i in range(self._size): # переберем столбци
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)): # если в текущем столбце все крестики
                self._win = 1 # вииграл человек
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)): # если в текущем столбце все нули
                self._win = 2 # вииграл комп
                return
        # по диагонали все крестики
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or\
            all(self.pole[i][-1 -i].value == self.HUMAN_X for i in range(self._size)):
                self._win = 1 # вииграл человек
                return
        # по диагонали все нолики
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or\
            all(self.pole[i][-1 -i].value == self.COMPUTER_O for i in range(self._size)):
                self._win = 2 # вииграл комп
                return
        if all(x.value != self.FREE_CELL for row in self.pole for x in row): # все клетки заполнени ничия
            self._win = 3



    def __getitem__(self, item):# для считивания по индексам
        self.__check_index(item) # проверим что индекс item коректний
        r, c = item # распаковуем колекцию item
        return self.pole[r][c].value # возвращаем нужное значение

    def __setitem__(self, key, value):
        self.__check_index(key) # проверим что key коректний
        r, c = key # распаковуем key
        self.pole[r][c].value = value# записиваем новие значения
        self.__update_win_status()

    def init(self):# инициализация игри очистка игрового поля
        for i in range(self._size):
            for j in range(self._size):
                self.pole[i][j].value = 0
        self._win = 0

    def show(self): # отоброжение текущего состояния игрового поля
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))
        print('------------------------------')

    def human_go(self): # реализация хода игрока
        if not self:
            return # значит все клетки заняти

        while True:
            i, j = map(int, input('Введите координати клетки: ').split())
            if not (0 <= i < self._size) or not (0 <= j < self._size): # если координати виходят за поле вести еще раз
                continue
            if self[i, j] == self.FREE_CELL: # если поле пустое
                self[i, j] = self.HUMAN_X # присваиваем значение
                break

    def computer_go(self): # реализация хода компа
        if not self:
            return # значит все клетки заняти

        while True:
            i = randint(0, self._size - 1)
            j = randint(0, self._size - 1)# комп случайн образом вибирает поле хода
            if self[i, j] != self.FREE_CELL: # поле занято вибор ещераз
                continue
            self[i, j] = self.COMPUTER_O # ход в свободное поле
            break

    @property
    def is_human_win(self): # вернет True если победил человек
        return self._win == 1

    @property
    def is_computer_win(self): # вернет True если победил комп
        return self._win == 2

    @property
    def is_draw(self): # вернет True если ничия
        return self._win == 3

    def __bool__(self): # вернет True если игра неокончена
        return self._win == 0 and self._win not in (1, 2, 3)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    step_game += 1
game.show()
if game.is_human_win:
    print('Поздравляем ви победили!')
elif game.is_computer_win:
    print('Победил компютер!')
else:
    print('Ничия???')
