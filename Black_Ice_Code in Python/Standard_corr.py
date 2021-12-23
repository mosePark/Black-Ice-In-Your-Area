import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
import xgboost as xgb

# road_19 = pd.read_csv("Data/previous/road_2019_testing.csv",encoding='euc-kr')
# road_18 = pd.read_csv("Data/previous/road_2018_testing.csv",encoding='euc-kr')
# road_17 = pd.read_csv("Data/previous/road_2017_testing.csv",encoding='euc-kr')
# road_16 = pd.read_csv("Data/previous/road_2016_testing.csv",encoding='euc-kr')
#
# road = pd.concat([road_16,road_17,road_18,road_19],axis=0,sort=True)
#
# final_road_E = pd.read_csv("Data/final_E.csv",encoding='euc-kr')
# final_roed_S = pd.read_csv("Data/final_S.csv",encoding='euc-kr')
# final_road = pd.concat([final_road_E,final_roed_S],axis=0,sort=True)
#
# road1 = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
#                     's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#                     'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#                     'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
#                     '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
#                     '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)','VMS_keyword'
#                     ]]
# corr_matrix = road1.corr() #피어슨상관관계
# print(corr_matrix['VMS_keyword'].sort_values(ascending=False))
road = pd.read_csv('Data/final.csv',encoding='euc-kr')

# corr_matrix = road1.corr() #피어슨상관관계
# print(corr_matrix['Risk_score'].sort_values(ascending=False))
#최종
# X = road[['VMS_time','강수계속시간(hr)','평균상대습도(%)','일강수량(mm)','최저기온시각(hhmi)','일최심적설(cm)','최대풍속(m/s)',
#           '평균이슬점온도(°C)','평균풍속(m/s)','안개계속시간(hr)','routeNo','pave','최저기온(°C)','bridge_surface','s_elevation',
#           'ice_leak','e_elevation','s_Xvalue','e_Xvalue','bridge','AWS_weather']]

# X = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
#                     's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#                     'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#                     'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
#                     '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
#                     '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
#                     ]]

# #only road
# X = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
#                     's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
#                     'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
#                     'VMS_time']]
# #only weather
# # X = road[['AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
# #                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
# #                     '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
# #                     '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
# #                     ]]
# Y = road['VMS_keyword']

# final = final_road[['VMS_time','강수계속시간(hr)','평균상대습도(%)','일강수량(mm)','최저기온시각(hhmi)','일최심적설(cm)','최대풍속(m/s)',
#           '평균이슬점온도(°C)','평균풍속(m/s)','안개계속시간(hr)','routeNo','pave','최저기온(°C)','bridge_surface','s_elevation',
#           'ice_leak','e_elevation','s_Xvalue','e_Xvalue','bridge','AWS_weather']]
# final_Y = final_road['VMS_keyword']

X1 = road[['사망자수','중상자수','경상자수']] #X1 : AIC - 51713.7302 / BIC - 51737.1643
X2 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)']]#X2 : AIC - 34897.7861 / BIC - 34929.0315
X3 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수']] #X3 : AIC - 34884.7124 / BIC - 34923.7692
X4 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도']] #X4 : AIC - -23046.9146 / BIC - -23000.0464
X5 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date']] #X5 : AIC - -23893.6852 / BIC - -23839.0056
X6 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)']] #X6 : AIC - -25750.1173 / BIC - -25687.6263
X7 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)']] #X7 : AIC - -25959.0075 / BIC - -25888.7051
X8 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)']] #X8 : AIC - -26136.3480 / BIC - -26058.2343
X9 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)']] #X9 : AIC - -28045.6053 / BIC - -27959.6802
X10 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)']]
#x10 : AIC - -49370.5107 / BIC - -49276.7742
X11 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)']]
#X11 : AIC - -49942.0131 / BIC - -49840.4653
X12 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue']]
#X12 : AIC - -50809.7359 / BIC - -50700.3767
X13 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)']]
#X13 : AIC - -51079.0288 / BIC - -50961.8582
X14 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic']]
#X14 : AIC - -51175.7847 / BIC - -51050.8028
X15 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)']]
#X15 : AIC - -52141.2172 / BIC - -52008.4239

####################################################################################################################################################################################################
X16 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)']]
#X16 : AIC - -52139.9305 / BIC - -51999.3258
####################################################################################################################################################################################################

X17 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen']]
#X17 : AIC - -52155.2479 / BIC - -52006.8319
X18 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation']]
#X18 : AIC - -52177.9062 / BIC - -52021.6787
X19 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)']]
#X19 : AIC - -52741.7477 / BIC - -52577.7089
X20 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)','최대풍속풍향(16방위)']]
#X20 : AIC - -53037.5420 / BIC - -52865.6918
X21 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane']]
#X21 : AIC - -53127.7241 / BIC - -52948.0626
X22 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상']]
#X22 : AIC - -53183.4965 / BIC - -52996.0235
X23 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword']]
#X23 : AIC - -53181.8585 / BIC - -52986.5742
X24 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword','lane']]
#X24 : AIC - -53247.3320 / BIC - -53044.2363
X25 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword','lane','부상신고']]
#X25 : AIC - -53253.5897 / BIC - -53042.6826
X26 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword','lane','부상신고','surface']]
#X26 : AIC - -53253.4277 / BIC - -53034.7092
X27 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword','lane','부상신고','surface',
            'routeNo']]
#X27 : AIC - -53268.0619 / BIC - -53041.5321
X28 = road[['사망자수','중상자수','경상자수','최저기온시각(hhmi)','사고건수','평균속도','date','평균기온(°C)','평균지면온도(°C)','평균이슬점온도(°C)','최대풍속(m/s)','평균상대습도(%)','최저기온(°C)','e_Xvalue',
            '평균풍속(m/s)','traffic','최고기온시각(hhmi)','최고기온(°C)','czlen','e_elevation','합계일조시간(hr)', '최대풍속풍향(16방위)','bridge_lane','기상','VMS_keyword','lane','부상신고','surface',
            'routeNo','bridge_surface']]
#X28 : AIC - -53923.1300 / BIC - -53688.7888
X = road[['date','routeNo','e_Xvalue','e_Yvalue','czlen',
              'e_elevation','lane','pave','surface','classification', 'traffic',
              'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
              'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
              '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
              '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
              '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)','VMS_keyword',
              '사고건수','사망자수','중상자수','경상자수','부상신고','평균속도']]
Y = road['Risk']
X_train, X_t, Y_train, Y_t = train_test_split(X, Y, random_state=100,shuffle=True, test_size=0.5)
X_val, X_test, Y_val, Y_test = train_test_split(X_t, Y_t, random_state=100,shuffle=True, test_size=0.4)

# # ensemble 할 model 정의
models = [
    ('dtc', DecisionTreeClassifier(max_depth=15, random_state=0)),
    ('mlp', MLPClassifier(activation='relu', alpha=0.0001, batch_size=32, beta_1=0.9, beta_2=0.999,
                    early_stopping=False, epsilon=1e-08, hidden_layer_sizes=(256, 128, 32),
                    learning_rate='constant', learning_rate_init=0.001, max_iter=15, momentum=0.9,
                    nesterovs_momentum=True, power_t=0.5, random_state=21, shuffle=True, solver='adam', tol=0.0001,
                    validation_fraction=0.1, verbose=True, warm_start=False))
]

# hard vote
# hard_vote = VotingClassifier(models, voting='hard')
# # hard_vote_cv = cross_validate(hard_vote, X_train, Y_train, cv=k_fold)
# hard_vote.fit(X_train, Y_train)
# print("hard_vote")
# print("훈련 세트 정확도: {:.3%}".format(hard_vote.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((hard_vote.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format((hard_vote.score(X_test, Y_test))))

#soft vote
# soft_vote = VotingClassifier(models, voting='soft')
# #soft_vote_cv = cross_validate(soft_vote, X_train, Y_train, cv=k_fold)
# soft_vote.fit(X, Y)
# print("\nsoft_vote")
# print("훈련 세트 정확도: {:.3%}".format(soft_vote.score(X_train,Y_train)))
# print("검증세트 정확도: {:.3%}".format((soft_vote.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format((soft_vote.score(X_test, Y_test))))
#
# predictions = soft_vote.predict(X)
# print(confusion_matrix(Y,predictions))
# print(classification_report(Y,predictions))

#xgb
xg_reg = xgb.XGBRegressor(objective='reg:linear',colsample_bytree=0.3, learning_rate=0.1, max_depth = 5, alpha=10, n_estimators = 10)
xg_reg.fit(X_train, Y_train)
print("전체 데이터 정확도: {:.3%}".format(xg_reg.score(X,Y)))
print("훈련 세트 정확도: {:.3%}".format(xg_reg.score(X_train,Y_train)))
print("검증세트 정확도: {:.3%}".format((xg_reg.score(X_val,Y_val))))
print("테스트 세트 정확도: {:.3%}".format((xg_reg.score(X_test, Y_test))))

#predictions = xg_reg.predict(X)
#print(confusion_matrix(Y,predictions))
#print(classification_report(Y,predictions))

# print("precision_score: ",precision_score(Y_test,predictions, average='weighted'))
# print("recall_score: ",recall_score(Y_test,predictions, average='weighted'))
# file_name = 'soft_vote.pkl'
# joblib.dump(soft_vote, file_name)
# file_name = 'soft_vote.pkl'
# model = joblib.load(file_name)
# predictions = model.predict(final)
# print(confusion_matrix(final_Y,predictions))
# print(classification_report(final_Y,predictions))





# forest = RandomForestClassifier(n_estimators=100, random_state=0)
# forest.fit(X_train, Y_train)
# print("\n랜덤포레스트(n_estimators=100)")
# print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
# # file_name = 'forest_n_est100.pkl'
# # joblib.dump(forest, file_name)
#
# forest = RandomForestClassifier(n_estimators=10, random_state=0)
# forest.fit(X_train, Y_train)
# print("\n랜덤포레스트(n_estimators=10)")
# print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
# # file_name = 'forest_n_est10.pkl'
# # joblib.dump(forest, file_name)
#
# forest = RandomForestClassifier(n_estimators=10,max_leaf_nodes=16, random_state=0)
# forest.fit(X_train, Y_train)
# print("\n랜덤포레스트(n_estimators=10,max_leaf_nodes=16)")
# print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
# # file_name = 'forest_n_est10_max_leaf_nodes16.pkl'
# # joblib.dump(forest, file_name)
#
# tree = DecisionTreeClassifier(random_state=0)
# tree.fit(X_train, Y_train)
# print("\n의사결정트리 default(max_depth=5)")
# print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
# # file_name = 'tree_default.pkl'
# # joblib.dump(tree, file_name)
#
# tree = DecisionTreeClassifier(max_depth=7, random_state=0)
# tree.fit(X_train, Y_train)
# print("\n의사결정트리(max_depth=7)")
# print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
# # file_name = 'tree_max_depth7.pkl'
# # joblib.dump(tree, file_name)
#
# tree = DecisionTreeClassifier(max_depth=10, random_state=0)
# tree.fit(X_train, Y_train)
# print("\n의사결정트리(max_depth=10)")
# print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
# # file_name = 'tree_max_depth10.pkl'
# # joblib.dump(tree, file_name)
#
# tree = DecisionTreeClassifier(max_depth=15, random_state=0)
# tree.fit(X_train, Y_train)
# print("\n의사결정트리(max_depth=15)")
# print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
# #print("특성 중요도:\n{}".format(tree.feature_importances_))
# # file_name = 'tree_max_depth15.pkl'
# # joblib.dump(tree, file_name)
#
# knn = KNeighborsClassifier(n_neighbors=5) #기본은 5개
# knn.fit(X_train,Y_train)
# print("\nKNN (n_neighbors=5)")
# print("훈련 세트 정확도: {:.3%}".format(knn.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((knn.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(knn.score(X_test, Y_test)))
# # file_name = 'knn_nn5.pkl'
# # joblib.dump(knn, file_name)
#
# knn = KNeighborsClassifier(n_neighbors=10)
# knn.fit(X_train,Y_train)
# print("\nKNN (n_neighbors=10)")
# print("훈련 세트 정확도: {:.3%}".format(knn.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((knn.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(knn.score(X_test, Y_test)))
# # file_name = 'knn_nn10.pkl'
# # joblib.dump(knn, file_name)
#
# mlp = MLPClassifier(activation='relu', alpha=0.0001, batch_size=32, beta_1=0.9, beta_2=0.999,
#                     early_stopping=False, epsilon=1e-08, hidden_layer_sizes=(256, 128, 32),
#                     learning_rate='constant', learning_rate_init=0.001, max_iter=10, momentum=0.9,
#                     nesterovs_momentum=True, power_t=0.5, random_state=21, shuffle=True, solver='adam', tol=0.0001,
#                     validation_fraction=0.1, verbose=True, warm_start=False)
# mlp.fit(X_train,Y_train)
# print("\nMLPhidden_layer_sizes=(256,128,32)")
# print("훈련 세트 정확도: {:.3%}".format(mlp.score(X_train, Y_train)))
# print("검증 세트 정확도: {:.3%}".format((mlp.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(mlp.score(X_test, Y_test)))
#
# bag_clf = BaggingClassifier(
#     DecisionTreeClassifier(),n_estimators=500,
#     bootstrap=True,n_jobs=-1)
# bag_clf.fit(X_train,Y_train)
# print("\nBagging (n_estimators=500,bootstrap=True,n_jobs=-1)")
# print("훈련 세트 정확도: {:.3%}".format(bag_clf.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((bag_clf.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(bag_clf.score(X_test, Y_test)))
# # file_name = 'bag_n_est500.pkl'
# # joblib.dump(bag_clf, file_name)
#
# bag_clf = BaggingClassifier(
#     DecisionTreeClassifier(),n_estimators=100,
#     bootstrap=True,n_jobs=-1)
# bag_clf.fit(X_train,Y_train)
# print("\nBagging (n_estimators=100,bootstrap=True,n_jobs=-1)")
# print("훈련 세트 정확도: {:.3%}".format(bag_clf.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((bag_clf.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(bag_clf.score(X_test, Y_test)))
# # file_name = 'bag_n_est100.pkl'
# joblib.dump(bag_clf, file_name)
#
# gbrt = GradientBoostingRegressor(max_depth=2,n_estimators=3,learning_rate=1.0)
# gbrt.fit(X_train,Y_train)
# print("\nGradientBoostingRegressor(max_depth=2,n_estimators=3,learning_rate=1.0)")
# print("훈련 세트 정확도: {:.3%}".format(gbrt.score(X_train, Y_train)))
# print("검증세트 정확도: {:.3%}".format((gbrt.score(X_val,Y_val))))
# print("테스트 세트 정확도: {:.3%}".format(gbrt.score(X_test, Y_test)))

# svc = SVC(C=1.0,gamma=0.1)
# svc.fit(X_train,Y_train)
# print("SVC(C=1.0,gamma=0.1)")
# print("훈련 세트 정확도: {:.3%}".format(svc.score(X_train, Y_train)))
# print("테스트 세트 정확도: {:.3%}".format(svc.score(X_test, Y_test)))
# file_name = 'svc_c1_gam01.pkl'
# joblib.dump(svc, file_name)


# # 객체를 pickled binary file 형태로 저장한다
# file_name = 'object_01.pkl'
# joblib.dump(tree, file_name)
# # pickled binary file 형태로 저장된 객체를 로딩한다
# file_name = 'object_01.pkl'
# obj = joblib.load(file_name)