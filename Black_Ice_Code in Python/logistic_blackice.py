import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm

road = pd.read_csv('Data/final.csv',encoding='euc-kr')

road1 = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend','czlen',
              's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
              'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
              'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
              '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
              '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
              '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)','VMS_keyword',
              '사고건수','사망자수','중상자수','경상자수','부상신고','평균속도']]
y = road[['Risk']]
y1 = road[['Risk_score']]


# road1['Risk'] = 0
# road1['Risk_score'] = 0
#
#
# for i in range(len(road1)):
#     if road1['기상'].iloc[i] == 0 or road1['기상'].iloc[i] == 4 or road1['기상'].iloc[i] == 5 or road1['기상'].iloc[i] == 8:
#         weather_score = 1
#     elif road1['기상'].iloc[i] == 1:
#         weather_score = 0.997
#     elif road1['기상'].iloc[i] == 2 or road1['기상'].iloc[i] == 3 or road1['기상'].iloc[i] == 6 or road1['기상'].iloc[i] == 7:
#         weather_score = 1.053
#
#     # print(weather_score)
#     if road1['평균속도'].iloc[i] >= 40:
#         traffic_score = 1
#     elif road1['평균속도'].iloc[i] < 40:
#         traffic_score = 1.05
#
#     road1['Risk'].iloc[i] = 10*(road1['사망자수'].iloc[i]*1 + road1['중상자수'].iloc[i]*0.1168+road1['경상자수'].iloc[i]*0.0068+road1['부상신고'].iloc[i]*0.0033)*weather_score*traffic_score
#     if road1['Risk'].iloc[i] < 3:
#         road1['Risk_score'].iloc[i] = 1
#     elif road1['Risk'].iloc[i] < 7:
#         road1['Risk_score'].iloc[i] = 2
#     elif road1['Risk'].iloc[i] < 12:
#         road1['Risk_score'].iloc[i] = 3
#     else:
#         road1['Risk_score'].iloc[i] = 4
#
# road1.to_csv('Data/final.csv',encoding='euc-kr',index=False)
