import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import column_or_1d
from tqdm import tqdm
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.tree import DecisionTreeClassifier


road = pd.read_csv('Data/final.csv',encoding='euc-kr')

# X = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend','czlen',
#               's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#               'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#               'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
#               '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
#               '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
#               '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)','VMS_keyword',
#               '사고건수','사망자수','중상자수','경상자수','부상신고','평균속도']]
X = road[['date','routeNo','e_Xvalue','e_Yvalue','czlen',
              'e_elevation','lane','pave','surface','classification', 'traffic',
              'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
              'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
              '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
              '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
              '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)','VMS_keyword',
              '사고건수','사망자수','중상자수','경상자수','부상신고','평균속도']]
Y = road[['Risk_score']]
#corr_matrix = X.corr() #피어슨상관관계
#print(corr_matrix['Risk'].sort_values(ascending=False))
#y1 = road[['Risk_score']]
#print(X.isnull().sum())
for j in range(3,31):
    model = RandomForestClassifier(n_estimators=100,random_state=0)
    rfe=RFE(model,j)
    fit=rfe.fit(X,Y)
    #print(fit.n_features_,fit.support_,fit.ranking_)
    print(fit.n_features_)
    for i in range(len(fit.support_)):

        print(fit.support_[i],X.columns[i],fit.ranking_[i])