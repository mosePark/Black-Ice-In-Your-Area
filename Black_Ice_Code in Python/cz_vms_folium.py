import folium #지도를 HTML로 만들어주는 라이브러리
import pandas as pd
import numpy as np

# VMS = pd.read_csv('Data/Info/VMS_Info.csv',encoding='euc-kr')
# # VMS_data_index = VMS_data['노선번호'] == 10
# # VMS = VMS_data[VMS_data_index]
# VMS_X = VMS['X좌표']
# VMS_Y = VMS['Y좌표']
# VMS_index = VMS['VMSID']

VDS = pd.read_csv('Data/Info/VDS_Info.csv',encoding='euc=kr') #CSV파일 읽어오는 함수
# VDS_data_index = VDS_data['routeNo'] == 101
# VDS = VDS_data[VDS_data_index]
VDS_X = VDS['s_Xvalue'] #X좌표
VDS_Y = VDS['s_Yvalue'] #Y좌표
VDS_index = VDS['czId'] #여기다 팝업창에 넣을 내용 입력

# map = pd.read_csv('Data/result_Data/mapping_data.csv',encoding='euc-kr')

m = folium.Map(
    location=[36.5053542, 127.7043419],
    zoom_start=8,
    tiles='Cartodb Positron'
) #지도 선언

# for i in range(len(VMS_X)):
#     folium.Marker(
#       location=[VMS_X[i],VMS_Y[i]],
#       popup=VMS_index[i],
#       icon=folium.Icon(color='red',icon='star')
#     ).add_to(m)

for j in range(len(VDS_X)):
    folium.Marker(
      location=[VDS_X[j],VDS_Y[j]], #좌표
      popup=VDS_index[j], #팝업 내용
      icon=folium.Icon(color='blue',icon='star') #색상, 기호
    ).add_to(m) #팝업 아이콘

# map_route = map['노선번호'] == 10 #경부선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
folium.PolyLine(
    locations=[VDS_X[j],VDS_Y[j]],
    tooltip='PolyLine', #선, 점, 원
    color='#FFEBCD',
).add_to(m)

m.save('test.html')
# map_route = map['노선번호'] == 101 #남해선(영암순천)
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACA696',
# ).add_to(m)
#
# map_route = map['노선번호'] == 102 #남해선(순천부산)
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FFB6C1',
# ).add_to(m)
#
# map_route = map['노선번호'] == 121 #무안광주선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#EE8D88',
# ).add_to(m)
#
# map_route = map['노선번호'] == 122 #광주대구선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FF7F50',
# ).add_to(m)
#
# map_route = map['노선번호'] == 150 #서해안선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#0F0F0F',
# ).add_to(m)
#
# map_route = map['노선번호'] == 160 #울산선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#800010',
# ).add_to(m)
#
# map_route = map['노선번호'] == 171 #평택화성선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#E8DE73',
# ).add_to(m)
#
# map_route = map['노선번호'] == 205 #익산장수선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#218200',
# ).add_to(m)
#
# map_route = map['노선번호'] == 207 #대구포항선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#740703',
# ).add_to(m)
#
# map_route = map['노선번호'] == 250 #논산천안선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#66523C',
# ).add_to(m)
#
# map_route = map['노선번호'] == 251 #호남선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#622438',
# ).add_to(m)
#
# map_route = map['노선번호'] == 270 #순천완주선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#CD3070',
# ).add_to(m)
#
# map_route = map['노선번호'] == 290 #세종포천선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#191970',
# ).add_to(m)
#
# map_route = map['노선번호'] == 291 #구리포천선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#6300FF',
# ).add_to(m)
#
# map_route = map['노선번호'] == 292 #양주지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#9860B6',
# ).add_to(m)
#
# map_route = map['노선번호'] == 301 #상주영덕선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#06B5DB',
# ).add_to(m)
#
# map_route = map['노선번호'] == 303 #청주상주선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#99DBE9',
# ).add_to(m)
#
# map_route = map['노선번호'] == 305 #당진대전선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#CF1414',
# ).add_to(m)
#
# map_route = map['노선번호'] == 350 #통영대전선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#800010',
# ).add_to(m)
#
# map_route = map['노선번호'] == 370 #제2중부선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FFF3D4',
# ).add_to(m)
#
# map_route = map['노선번호'] == 400 #평택제천선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FFEBCD',
# ).add_to(m)
#
# map_route = map['노선번호'] == 450 #중부내륙선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#0DEEC9',
# ).add_to(m)
#
# map_route = map['노선번호'] == 500 #영동선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#00FFF0',
# ).add_to(m)
#
# map_route = map['노선번호'] == 549 #중앙선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#7FB3FA',
# ).add_to(m)
#
# map_route = map['노선번호'] == 550 #중앙선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FFE062',
# ).add_to(m)
#
# map_route = map['노선번호'] == 600 #서울양양선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#F5AA3F',
# ).add_to(m)
#
# map_route = map['노선번호'] == 650 #동해선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#A6FF4D',
# ).add_to(m)
#
# map_route = map['노선번호'] == 655 #부산포항선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#044778',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1000 #서울외곽순환선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FF6FBD',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1020 #남해제1지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FF81D3',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1040 #남해제2지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#EE8D88',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1101 #제2경인선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FF7F50',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1200 #경인선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#FF5A5A',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1300 #인천국제공항선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#CD3070',
# ).add_to(m)
#
# map_route = map['노선번호'] == 1510 #서천공주선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#EB731C',
# ).add_to(m)
#
# map_route = map['노선번호'] == 2510 #호남선의 지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#D5D679',
# ).add_to(m)
#
# map_route = map['노선번호'] == 2530 #고창담양선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#E8DE73',
# ).add_to(m)
#
# map_route = map['노선번호'] == 3000 #대전남부순환선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACB900',
# ).add_to(m)
#
# map_route = map['노선번호'] == 4000 #수도권제2순환선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACA696',
# ).add_to(m)
#
# map_route = map['노선번호'] == 4510 #중부내륙선의 지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACA696',
# ).add_to(m)
#
# map_route = map['노선번호'] == 5510 #중앙선의 지선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACA696',
# ).add_to(m)
#
# map_route = map['노선번호'] == 6000 #부산외곽순환선
# data = map[map_route]
# line = data[['X좌표값','Y좌표값']]
# folium.PolyLine(
#     locations=line,
#     tooltip='PolyLine',
#     color='#ACA696',
# ).add_to(m)

#m.save('test.html')
#m.save('map_HTML/VDS_map.html')
#m.save('map_HTML/VMS.html')
#m.save('map_HTML/VMS_VDS.html')