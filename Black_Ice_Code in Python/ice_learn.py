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
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
import seaborn as sns



road2 = pd.read_csv("Data/road_2019_testing.csv",encoding='euc-kr')
road_18 = pd.read_csv("Data/road_2018_testing.csv",encoding='euc-kr')
road_17 = pd.read_csv("Data/road_2017_testing.csv",encoding='euc-kr')
road_16 = pd.read_csv("Data/road_2016_testing.csv",encoding='euc-kr')

road = pd.concat([road_16,road_17,road_18],axis=0,sort=True)

#road.to_csv('road.csv',encoding='euc-kr',index=False)

#default
X = road[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
                    's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
                    'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
                    'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
                    '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
                    '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
                    '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
                    ]]
X_val = road2[['date','routeNo','direction','s_Xvalue','s_Yvalue','e_Xvalue','e_Yvalue','czstart','czend',
                    's_elevation','e_elevation','lane','pave','surface','classification', 'traffic',
                    'bridge_lane','bridge_pave','bridge_surface','bridge','tunnel','ice_leak','grooving',
                    'VMS_time','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
                    '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
                    '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
                    '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)'
                    ]]
#1times
# X = road[['s_elevation','e_elevation','traffic','bridge','tunnel','pave','surface','classification',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]
# X_val = road2[['s_elevation','e_elevation','traffic','bridge','tunnel','pave','surface','classification',
#                     '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]
#2times
# X = road[['평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]
# X_val = road2[['평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','일강수량(mm)',
#                     '평균이슬점온도(°C)','평균상대습도(%)','강수계속시간(hr)','최고기온시각(hhmi)',
#                     '합계일조시간(hr)','평균지면온도(°C)']]
#final
# X = road[['s_elevation','e_elevation','pave','surface','classification','grooving','traffic',
#         '합계일조시간(hr)','일강수량(mm)','강수계속시간(hr)','평균풍속(m/s)','평균이슬점온도(°C)',
#         ]]
# X_val = road2[['s_elevation','e_elevation','pave','surface','classification','grooving','traffic',
#         '합계일조시간(hr)','일강수량(mm)','강수계속시간(hr)','평균풍속(m/s)','평균이슬점온도(°C)',
#         ]]

Y = road['VMS_keyword']
Y_val = road2[['VMS_keyword']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=100,shuffle=True, test_size=0.4)

forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, Y_train)
print("\n랜덤포레스트(n_estimators=100)")
print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
print('confusion_matirix :\n',confusion_matrix(Y_test,forest.predict(X_test)))
print('classification_report:\n',classification_report(Y_test,forest.predict(X_test)))
print("특성 중요도:\n{}".format(forest.feature_importances_))
file_name = 'forest_n_est100.pkl'
joblib.dump(forest, file_name)

forest = RandomForestClassifier(n_estimators=10, random_state=0)
forest.fit(X_train, Y_train)
print("\n랜덤포레스트(n_estimators=10)")
print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
#print("특성 중요도:\n{}".format(forest.feature_importances_))
file_name = 'forest_n_est10.pkl'
joblib.dump(forest, file_name)

forest = RandomForestClassifier(n_estimators=10,max_leaf_nodes=16, random_state=0)
forest.fit(X_train, Y_train)
print("\n랜덤포레스트(n_estimators=10,max_leaf_nodes=16)")
print("훈련 세트 정확도: {:.3%}".format(forest.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format((forest.score(X_test, Y_test))))
print("검증세트 정확도: {:.3%}".format((forest.score(X_val,Y_val))))
file_name = 'forest_n_est10_max_leaf_nodes16.pkl'
joblib.dump(forest, file_name)

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, Y_train)
print("\n의사결정트리 default(max_depth=5)")
print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
#print("특성 중요도:\n{}".format(tree.feature_importances_))
file_name = 'tree_default.pkl'
joblib.dump(tree, file_name)

tree = DecisionTreeClassifier(max_depth=7, random_state=0)
tree.fit(X_train, Y_train)
print("\n의사결정트리(max_depth=7)")
print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
#print("특성 중요도:\n{}".format(tree.feature_importances_))
file_name = 'tree_max_depth7.pkl'
joblib.dump(tree, file_name)

tree = DecisionTreeClassifier(max_depth=10, random_state=0)
tree.fit(X_train, Y_train)
print("\n의사결정트리(max_depth=10)")
print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
#print("특성 중요도:\n{}".format(tree.feature_importances_))
file_name = 'tree_max_depth10.pkl'
joblib.dump(tree, file_name)

tree = DecisionTreeClassifier(max_depth=15, random_state=0)
tree.fit(X_train, Y_train)
print("\n의사결정트리(max_depth=15)")
print("훈련 세트 정확도: {:.3%}".format(tree.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(tree.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((tree.score(X_val,Y_val))))
#print("특성 중요도:\n{}".format(tree.feature_importances_))
file_name = 'tree_max_depth15.pkl'
joblib.dump(tree, file_name)

knn = KNeighborsClassifier(n_neighbors=5) #기본은 5개
knn.fit(X_train,Y_train)
print("\nKNN (n_neighbors=5)")
print("훈련 세트 정확도: {:.3%}".format(knn.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(knn.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((knn.score(X_val,Y_val))))
file_name = 'knn_nn5.pkl'
joblib.dump(knn, file_name)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train,Y_train)
print("\nKNN (n_neighbors=10)")
print("훈련 세트 정확도: {:.3%}".format(knn.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(knn.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((knn.score(X_val,Y_val))))
file_name = 'knn_nn10.pkl'
joblib.dump(knn, file_name)

mlp = MLPClassifier(activation='relu', alpha=0.0001, batch_size=32, beta_1=0.9, beta_2=0.999,
                    early_stopping=False, epsilon=1e-08, hidden_layer_sizes=(256, 128, 32),
                    learning_rate='constant', learning_rate_init=0.001, max_iter=10, momentum=0.9,
                    nesterovs_momentum=True, power_t=0.5, random_state=21, shuffle=True, solver='adam', tol=0.0001,
                    validation_fraction=0.1, verbose=True, warm_start=False)
mlp.fit(X_train,Y_train)
print("\nMLPhidden_layer_sizes=(256,128,32)")
print("훈련 세트 정확도: {:.3%}".format(mlp.score(X_train, Y_train)))
print("검증 세트 정확도: {:.3%}".format(mlp.score(X_test, Y_test)))
print("테스트 세트 정확도: {:.3%}".format((mlp.score(X_val,Y_val))))
print(confusion_matrix(Y_val,mlp.predict(X_val)))
print(classification_report(Y_val,mlp.predict(X_val)))

bag_clf = BaggingClassifier(
    DecisionTreeClassifier(),n_estimators=500,
    bootstrap=True,n_jobs=-1)
bag_clf.fit(X_train,Y_train)
print("\nBagging (n_estimators=100,bootstrap=True,n_jobs=-1)")
print("훈련 세트 정확도: {:.3%}".format(bag_clf.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(bag_clf.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((bag_clf.score(X_val,Y_val))))
# file_name = 'bag_n_est500.pkl'
# joblib.dump(bag_clf, file_name)

bag_clf = BaggingClassifier(
    DecisionTreeClassifier(),n_estimators=100,
    bootstrap=True,n_jobs=-1)
bag_clf.fit(X_train,Y_train)
print("\nBagging (n_estimators=100,bootstrap=True,n_jobs=-1)")
print("훈련 세트 정확도: {:.3%}".format(bag_clf.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(bag_clf.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((bag_clf.score(X_val,Y_val))))
file_name = 'bag_n_est100.pkl'
joblib.dump(bag_clf, file_name)

gbrt = GradientBoostingRegressor(max_depth=2,n_estimators=3,learning_rate=1.0)
gbrt.fit(X_train,Y_train)
print("\nGradientBoostingRegressor(max_depth=2,n_estimators=3,learning_rate=1.0)")
print("훈련 세트 정확도: {:.3%}".format(gbrt.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(gbrt.score(X_test, Y_test)))

svc = SVC(C=1.0,gamma=0.1)
svc.fit(X_train,Y_train)
print("SVC(C=1.0,gamma=0.1)")
print("훈련 세트 정확도: {:.3%}".format(svc.score(X_train, Y_train)))
print("테스트 세트 정확도: {:.3%}".format(svc.score(X_test, Y_test)))
print("검증세트 정확도: {:.3%}".format((svc.score(X_val,Y_val))))
file_name = 'svc_c1_gam01.pkl'
joblib.dump(svc, file_name)


# 객체를 pickled binary file 형태로 저장한다
file_name = 'object_01.pkl'
joblib.dump(tree, file_name)
# pickled binary file 형태로 저장된 객체를 로딩한다
file_name = 'object_01.pkl'
obj = joblib.load(file_name)