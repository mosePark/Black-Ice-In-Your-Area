import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, BatchNormalization
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from keras.optimizers import SGD

def z_score_normalize(lst):
    normalized = []
    for value in lst:
        normalized_num = (value - np.mean(lst)) / np.std(lst)
        normalized.append(normalized_num)

    return normalized

def min_max_normalize(lst):
    normalized = []
    for value in lst:
        normalized_num = (value - min(lst)) / (max(lst) - min(lst))
        normalized.append(normalized_num)
        print(value,normalized_num)
    return normalized

def normalize(numeric_dataset):
    # normalized_value = (x - minimum_value) / (maximum_value - minimum_value) # calculate mean and standard deviation per numeric columns
    min_val = numeric_dataset.min(axis=0)
    max_val = numeric_dataset.max(axis=0)
    ranges = max_val - min_val
    # normalization,min_max_scaling
    matrix_normalized = (numeric_dataset - min_val)/ ranges
    return matrix_normalized, ranges, min_val

def demormalize(matrix_dataset,min_val,ranges):
    numeric_dataset = (matrix_dataset * ranges)+min_val
    return numeric_dataset


# def generate_time_series(batch_size,n_steps):
#     freq1,freq2,offsets1,offsets2 = np.random.rand(4,batch_size,1)
#     time = np.linspace(0,1,n_steps)
#     series = 0.5 * np.sin((time - offsets1) * (freq1 * 10 + 10))
#     series += 0.2 * np.sin((time - offsets2) * (freq2 * 20 + 20))
#     series += 0.1 * (np.random.rand(batch_size,n_steps)-0.5)
#     return series[...,np.newaxis].astype(np.float32)

data_2016 = pd.read_csv('Data/road_2016_testing.csv',encoding='euc-kr')
data_2017 = pd.read_csv('Data/road_2017_testing.csv',encoding='euc-kr')
data_2018 = pd.read_csv('Data/road_2018_testing.csv',encoding='euc-kr')
data_2019 = pd.read_csv('Data/road_2019_testing.csv',encoding='euc-kr')
train_data = pd.concat([data_2016,data_2017,data_2018],axis=0,sort=False)
test_data = data_2019

#default 데이터셋
# train_x = train_data[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
#                     's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#                     'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#                     'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
#                     '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
#                     '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
#                     ]]
# test_x = test_data[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
#                     's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#                     'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#                     'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
#                     '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
#                     '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
#                     ]]

#상관계수분석 후 1회차
# train_x = train_data[['s_elevation','e_elevation','traffic','bridge','tunnel','pave','surface','classification',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]
# test_x = test_data[['s_elevation','e_elevation','traffic','bridge','tunnel','pave','surface','classification',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]

#final
train_x = train_data[['s_elevation','e_elevation','pave','surface','classification','grooving',
                    '안개계속시간(hr)','합계일조시간(hr)','일강수량(mm)','강수계속시간(hr)','평균풍속(m/s)','평균이슬점온도(°C)',
                    ]]
test_x = test_data[['s_elevation','e_elevation','pave','surface','classification','grooving',
                    '안개계속시간(hr)','합계일조시간(hr)','일강수량(mm)','강수계속시간(hr)','평균풍속(m/s)','평균이슬점온도(°C)',
                    ]]

train_y = train_data['VMS_keyword']
test_y = test_data['VMS_keyword']

train_x, ranges_trx, min_val_trx = normalize(train_x)
train_y, ranges_try, min_val_try = normalize(train_y)
test_X, ranges_te, min_val_tex = normalize(test_x)
test_Y, ranges_tey, min_val_tey = normalize(test_y)

# X = np.zeros(shape=(len(train_x),42))  #default용
# Y = np.zeros(shape=(len(train_y),1))
# test_x = np.zeros(shape=(len(test_X),42))
# test_y = np.zeros(shape=(len(test_Y),1))

X = np.zeros(shape=(len(train_x),12))  #상관.분석후 최종
Y = np.zeros(shape=(len(train_y),1))
test_x = np.zeros(shape=(len(test_X),12))
test_y = np.zeros(shape=(len(test_Y),1))

X = train_x.values
Y = train_y.values
test_x = test_X.values
test_y = test_Y.values

# print(X)
#default
# model1 = keras.models.Sequential([
#         keras.layers.Flatten(input_shape=[42]),
#         keras.layers.BatchNormalization(),
#         keras.layers.Dense(256,activation="relu"),
#         keras.layers.BatchNormalization(),
#         keras.layers.Dense(128,activation="relu"),
#         keras.layers.BatchNormalization(),
#         keras.layers.Dense(10,activation="softmax")
# ])

#상관분석후 1회차
# model2 = keras.models.Sequential(
#     [keras.layers.Flatten(input_shape=[19]),
#     keras.layers.BatchNormalization(),
#     keras.layers.Dense(512,activation="relu"),
#     keras.layers.BatchNormalization(),
#     keras.layers.Dense(300,activation="relu"),
#     keras.layers.BatchNormalization(),
#     keras.layers.Dense(10,activation="softmax")
# ])

#final
model3 = keras.models.Sequential(
    [keras.layers.Flatten(input_shape=[12]),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(256,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(32,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(1,activation="sigmoid")
])

print(model3.summary())

model3.compile(loss="mean_squared_error",optimizer=SGD(lr=0.01),metrics=["accuracy"])
hist = model3.fit(X,Y,batch_size=32 ,epochs=10,validation_data=(test_x,test_y))
# model3.save('512_300_80_10_Sequential.h5')
y_pred = model3.predict(test_x)
# print(y_pred)
# print(test_y)
# test_mse_score, test_mae_score = model3.evaluate(test_x,test_y)
# print(test_mse_score)
cm = confusion_matrix(test_y, y_pred)
print(cm)

# model3 = keras.models.load_model("512_300_80_10_Sequential.h5")
# print(model3.summary())
# print(model3.predict(test_x))
# model3.compile(loss="sparse_categorical_crossentropy",optimizer="sgd",metrics=["accuracy"])
# hist = model3.fit(X,Y,batch_size=32 ,epochs=30,validation_data=(test_x,test_y))