"""Установка пакета Keras - оболочки над TensorFlow. Сервис colabs от Google для экспериментов по построению и
обучению нейросетей. Пример использования API Keras для задачи перевода градусов Цельсия в градусы Фаренгейта.
Последовательная модель нейронной сети (keras.Sequential). Создание полносвязного слоя нейронов (Dense).
Линейная активационная функция: activation='linear'. Компиляция модели сети: model.compile(). Запуск обучения сети:
model.fit(). Подача на вход сети данных и вычисление выходного значения: model.predict(). Получение значений
весовых коэффициентов: model.get_weights(). """
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Keras - установка и первое знакомство

import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import Dense

c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])

model = keras.Sequential()
model.add(Dense(units=1, input_shape=(1, ), activation='linear'))
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=500, verbose=0)
print("Обучение завершено")

print(model.predict([100]))
print(model.get_weights())

plt.plot(history.history['loss'])
plt.grid(True)
plt.show()
