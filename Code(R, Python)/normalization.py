import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
#CSV 파일 받아오기
df = pd.read_csv("total_0819.csv", low_memory=False, sep=';')
print("print1")
print(df.columns)

#칼럼명에서 유의미한거 추려서 새로운 데이터프레임 리스트 생성하기 <- 1차적 추리기
cleansing = ['산도', '유기물함량', '유효인산농도', '유효규산농도', '실제비료칼리사용량', '실제비료석회사용량', '실제비료마그네슘사용량', '석회소요량', '질산태질소용량', '염기치환용량', '전기전도도', '암모니아태질소용량',
'강수량', '기온150CM', '기온400CM', '기온50CM', '습도150CM', '습도400CM', '습도50CM','일사량', '증발량', '지중온도10CM', '지중온도20CM', '지중온도5CM', '초상온도', '토양수분10CM', '토양수분20CM', '토양수분30CM','풍속1000CM', '풍속150CM', '풍속300CM', '풍향1000CM', '풍향150CM', '풍향300CM', '일강수량', '지중온도100CM', '지중온도150CM', '지중온도300CM', '지중온도500CM', '지중온도50CM', '최고기온', '최대풍속', '최대풍속풍향', '최저기온', '최저상대습도','최저초상온도', '평균상대습도', '평균이슬점온도', '평균지면온도', '평균지중온도10CM', '평균지중온도20CM','평균지중온도30CM', '평균지중온도5CM', '평균풍속', '평균현지기압']

clean_df = df[cleansing]

#원본 파일에서 선택된 칼럼들 제외하기
df.drop(cleansing, axis = 1, inplace=True)
print("print2")
print(df.columns)


trans_df = clean_df.select_dtypes(include=[object])
le = preprocessing.LabelEncoder()

trans_df = clean_df.apply(le.fit_transform)
print(trans_df)

#정규화하기
normalizeddf_train = Normalizer().fit_transform(trans_df)
print (normalizeddf_train)

#전처리된 데이터와 원본 파일 합치기
result = pd.concat([df,pd.DataFrame(normalizeddf_train)], axis= 1)
print(result)

result.to_csv("newfile_2_normalize.csv")
