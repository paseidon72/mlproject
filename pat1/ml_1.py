import numpy as np

ver1 = np.zeros(10) # массив из 10 нулей

ver2 = np.ones(10)  # массив из 10 одиниць

ver3 = np.ones(10)*5  # массив из 10 пятьорок

ver4 = np.arange(10, 51)  # массив целих чисет от 10 до 50 включительно

ver5 = np.arange(10, 51, 2)  # массив целих четних чисет от 10 до 50 включительно

ver6 = np.eye(3)  # единичная матрица

ver7 = np.random.rand(1)  # генария случайного числа

ver8 = np.random.randn(25)  # генария 25 случайних чисел из стандартного распределения

ver9 = np.arange(1, 101)/100
ver10 = ver9.reshape(10, 10) # генария матрици с шагом 0.01

ver11 = np.linspace(0, 1, 20) # создать 20 равноудалених точек между 0 и 1
ver12 = np.arange(1, 26).reshape(5, 5)

ver13 = ver12[2:] # получение строк из матрици с 3 по 5

ver14 = ver12[2:, 1:] # получение колонок из матрици с 1 до конца

ver15 = ver12[3, 4] # получение числа 20 из матрици

ver16 = ver12[:3, 1:2] # получение матрици 2, 7, 12 на основании предидущей

ver17 = ver12[4:] # получение строки матрици на основании предидущей

ver18 = ver12[3:5, :] # получение строк матрици на основании предидущей

ver19 = ver12.sum() # сумма всех чисел матрици

ver20 = ver12.std() # среднее квадратичное отклонение чисел матрици

ver21 = np.random.seed(101)
ver22 = np.random.rand(1)# получить один и тот же случайний результат

res = np.arange(0, 9).reshape(3, 3) # матрица 3х3 от 0 до 8 включительно

result = res
result1 = res.sum(axis=0) #сумма колонок
result2 = res.sum(axis=1) # сумма строк
print('массив из 10 нулей')
print(ver1)
print('-' * 20)
print('массив из 10 одиниць')
print(ver2)
print('-' * 20)
print('массив из 10 пятьорок')
print(ver3)
print('-' * 20)
print('массив целих чисет от 10 до 50 включительно')
print(ver4)
print('-' * 20)
print('массив целих четних чисет от 10 до 50 включительно')
print(ver5)
print('-' * 20)
print('единичная матрица')
print(ver6)
print('-' * 20)
print('генария случайного числа')
print(ver7)
print('-' * 20)
print('генария 25 случайних чисел из стандартного распределения')
print(ver8)
print('-' * 20)
print('генария матрици с шагом 0.01')
print(ver10)
print('-' * 20)
print('создать 20 равноудалених точек между 0 и 1')
print(ver11)
print('-' * 20)
print('матрица')
print(ver12)
print('-' * 20)
print('получение строк из матрици с 3 по 5')
print(ver13)
print('-' * 20)
print('получение колонок из матрици с 1 до конца')
print(ver14)
print('-' * 20)
print('получение числа 20 из матрици')
print(ver15)
print('-' * 20)
print('получение матрици 2, 7, 12 на основании предидущей')
print(ver16)
print('-' * 20)
print('получение строки матрици на основании предидущей')
print(ver17)
print('-' * 20)
print('получение строк матрици на основании предидущей')
print(ver18)
print('-' * 20)
print('сумма всех чисел матрици')
print(ver19)
print('-' * 20)
print('среднее квадратичное отклонение чисел матрици')
print(ver20)
print('-' * 20)
print('получить один и тот же случайний результат')
print(ver22)
print('-' * 20)
print('матрица')
print(result)
print('*' * 20 + 'матрица 3х3 от 0 до 8 включительно')
print('сумма колонок')
print(result1)
print('*' * 20)
print('сумма строк')
print(result2)