import tensorflow as tf
import numpy as np

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import RMSprop

tf.random.set_seed(777)

data = np.array([[0,0],[1,0],[0,1],[1,1]])
label = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(32, input_shape = (2, ), activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

'''# 평균 제곱 오차 회귀 문제
model.compile(optimizer = RMSprop(),
              loss = 'mse',
              metrics = [])'''

# 이항 분류 문제
model.compile(optimizer = RMSprop(),
              loss = 'binary_crossentropy',
              metrics = ['acc'])

'''# 다항 분류 문제
model.compile(optimizer = RMSprop(),
              loss = 'categorical_crossentropy',
              metrics = ['acc'])'''

model.fit(data, label, epochs = 100)

model.evaluate(data, label)
# result = model.predict(data)
# print(result)