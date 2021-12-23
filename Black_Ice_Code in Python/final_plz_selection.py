import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, \
    accuracy_score
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm
from sklearn.metrics import log_loss


road = pd.read_csv('Data/final.csv',encoding='euc-kr')

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
# xtest = road[['e_Yvalue','평균지면온도(°C)','평균기온(°C)','최저기온(°C)','평균이슬점온도(°C)',
#             '평균상대습도(%)']]
y = road[['Risk_score']]
scaler = MinMaxScaler()
X28[:] = scaler.fit_transform(X28[:])
#xtest[:] = scaler.fit_transform(xtest[:])
#xtest = xtest+0.00001*np.random.rand(18240, 6)
logit = sm.OLS(road[['Risk_score']],X28) #로지스틱 회귀분석 시행
result = logit.fit()
print(result.summary2())

# logit_mod = sm.Logit(y, xtest)
# logit_res = logit_mod.fit(disp=0)
# y_hat = logit_res.predict(xtest)
# print(log_loss(y,y_hat,normalize=False))
# mu_null = np.sum(y)/len(y)
# print(mu_null)
# y_null = np.ones_like(y) * 0.006305
# print(log_loss(y,y_null,normalize=False))
# print(1 - (log_loss(y, y_hat) / log_loss(y, y_null)))
#
# #print(np.exp(result.params))
# model = LogisticRegression()
# result = model.fit(X=xtest, y=y)
# print(result.coef_,result.intercept_)
# print('confusion_matirix :\n',confusion_matrix(y,model.predict(xtest)))
# print('classification_report:\n',classification_report(y,model.predict(xtest)))
#
# y_pred = model.predict(X16)
# acc = accuracy_score(road['acc'],y_pred)
# print(acc)
#
# tab = pd.crosstab(road['acc'], y_pred)
# print(tab)
# acc = (tab.iloc[0,0]) / len(road['acc'])
# print('accuracy =', acc)
# cm = confusion_matrix(road['acc'], y_pred)
# print(cm)