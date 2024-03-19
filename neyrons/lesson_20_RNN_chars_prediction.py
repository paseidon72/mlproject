"""Строим рекуррентную нейросеть для прогнозирования символов последовательности. Узнаете, как правильно
кодировать и подавать на вход сети текстовую информацию в виде One-hot encoding (OHE) векторов. Рассказывается
про инструмент Tokenizer пакета Keras. Его методы: fit_on_texts, texts_to_matrix и коллекцию word_index.
Строится архитектура нейронной сети с помощью слоя SimpleRNN пакета Keras."""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import re

from keras.layers import Dense, SimpleRNN, Input
from keras.models import Sequential
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer


with open('train_data_true', 'r', encoding='utf-8') as f:
    text = f.read()
    text = text.replace('\ufeff', '')  # убираем первый невидимый символ
    text = re.sub(r'[^А-я ]', '', text)  # заменяем все символы кроме кириллицы на пустые символы

# парсим текст, как последовательность символов
num_characters = 34  # 33 буквы + пробел
tokenizer = Tokenizer(num_words=num_characters, char_level=True)  # токенизируем на уровне символов
tokenizer.fit_on_texts([text])  # формируем токены на основе частотности в нашем тексте
print(tokenizer.word_index)

inp_chars = 6
data = tokenizer.texts_to_matrix(text)  # преобразуем исходный текст в массив OHE
n = data.shape[0] - inp_chars  # так как мы предсказываем по трем символам - четвертый

X = np.array([data[i:i + inp_chars, :] for i in range(n)])
Y = data[inp_chars:]  # предсказание следующего символа

print(data.shape)

model = Sequential()
model.add(Input((inp_chars,
                 num_characters)))  # при тренировке в рекуррентные модели keras подается сразу вся последовательность, поэтому в input теперь два числа. 1-длина последовательности, 2-размер OHE
model.add(SimpleRNN(128, activation='tanh'))  # рекуррентный слой на 500 нейронов
model.add(Dense(num_characters, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

history = model.fit(X, Y, batch_size=32, epochs=100)


def buildPhrase(inp_str, str_len=50):
    for i in range(str_len):
        x = []
        for j in range(i, i + inp_chars):
            x.append(tokenizer.texts_to_matrix(inp_str[j]))  # преобразуем символы в One-Hot-encoding

        x = np.array(x)
        inp = x.reshape(1, inp_chars, num_characters)

        pred = model.predict(inp)  # предсказываем OHE четвертого символа
        d = tokenizer.index_word[pred.argmax(axis=1)[0]]  # получаем ответ в символьном представлении

        inp_str += d  # дописываем строку

    return inp_str


res = buildPhrase("утренн")
print(res)
