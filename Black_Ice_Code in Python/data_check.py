import pandas as pd
import matplotlib.pyplot as plt
import json

# Road = pd.read_csv('RoadGPS.csv',encoding='euc-kr')
# Pavement = pd.read_csv('pavement_of_a_road.csv',encoding='euc-kr')
#
# Road_data = Road.drop([Road.columns[5],Road.columns[6]],axis=1)
#Pavement_data = Pavement.drop([Pavement.columns[11]],axis=1)
#Pavement_data = Pavement_data.drop_duplicates(['지사','노선코드','노선명','방향','시점','종점','포장형태','표층재','교면구분'],keep='last')

#print(Road_data)
#print(Pavement_data)
#Pavement_data.to_csv('Pavement_data.csv',encoding='euc-kr',index=False)
# Road_data.to_csv('Road_data.csv',encoding='euc-kr',index=False)

# with open('locationinfoUnit.json','r',encoding='utf-8') as file:
#     json_data = json.load(file)
#     print(json.dumps(json_data,indent='\t'))

#VDS교통량데이터 정제
# VDS_2017 = pd.read_csv('2016.txt', delimiter = '|',encoding='utf-8')
# print(VDS_2017.head())
# VDS_2017 = VDS_2017.drop_duplicates()
# VDS_2017 = VDS_2017.drop(VDS_2017.columns[4],axis=1)
# print(VDS_2017.head())
# VDS_2017.to_csv('VDS_2016.csv',encoding='euc-kr',index=False)


# VDS_code = open('VDS/VDS_Code.txt','r',encoding='utf-8')
# VDS_data = VDS_code.readline()
# VDS_code.close()
# print(VDS_data)
# VDS_data = VDS_data.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><data><code>SUCCESS</code><message>인증키가 유효합니다.</message><count>7494</count>','')\
#     .replace('<list>','').replace('<czId>','').replace('</czId>',',').replace('<directionCode>','').replace('</directionCode>',',')\
#     .replace('<equipmentBelongingCode>','').replace('</equipmentBelongingCode>','').replace('<equipmentBelongingName>','')\
#     .replace('</equipmentBelongingName>',',').replace('<grs80x>','').replace('</grs80x>',',').replace('<grs80y>','')\
#     .replace('</grs80y>',',').replace('<roadgradeCode>','').replace('</roadgradeCode>',',').replace('<roadgradeName>','')\
#     .replace('</roadgradeName>',',').replace('<routeName>','').replace('</routeName>',',').replace('<routeNo>','')\
#     .replace('</routeNo>',',').replace('<routeSeq>','').replace('</routeSeq>',',').replace('<shift>','').replace('</shift>',',')\
#     .replace('<vdsCode>','').replace('</vdsCode>',',').replace('<vdsEndShift>','').replace('</vdsEndShift>',',')\
#     .replace('<vdsId>','').replace('</vdsId>',',').replace('<vdsLength>','').replace('</vdsLength>',',').replace('<vdsName>','')\
#     .replace('</vdsName>',',').replace('<vdsStartShift>','').replace('</vdsStartShift>','').replace('</list>','\n')
# print(VDS_data)
# with open('VDS_code.txt','a',encoding='utf-8') as file:
#     file.writelines(VDS_data)
#
# VDS_code = pd.read_csv('VDS_code.txt',encoding='utf-8')
# VDS_code.to_csv('VDS_code.csv',encoding='euc-kr',index=False)

# leak = open('snow_leak.txt','r',encoding='utf-8')
# leak_data = leak.readline()
# leak.close()
# print(leak_data)
# leak_data = leak_data.replace('<snowLeakSecLists>','').replace('<brof>','').replace('</brof>','|')\
#     .replace('<enpt>','').replace('</enpt>','|').replace('<lnctCrvn>','').replace('</lnctCrvn>','|')\
#     .replace('<mnof>','').replace('</mnof>','|').replace('<planeCrvn>','').replace('</planeCrvn>','|')\
#     .replace('<routeNm>','').replace('</routeNm>','|').replace('<slcnReason>','').replace('</slcnReason>','|')\
#     .replace('<stpn>','').replace('</stpn>','').replace('</snowLeakSecLists>','\n').replace('</data>','')
# print(leak_data)
# with open('leak_data.txt','a',encoding='utf-8') as file:
#     file.writelines(leak_data)
# for i in range(1,32):
#     if i == 9:
#         continue
#     elif i < 10:
#         text = 'VDS/VDS_data_2019120'+str(i)+'.txt'
#         csv = 'VDS/VDS_data_2019120'+str(i)+'.csv'
#     else:
#         text = 'VDS/VDS_data_201912' + str(i) + '.txt'
#         csv = 'VDS/VDS_data_201912' + str(i) + '.csv'
#     VDS_data = pd.read_csv(text,encoding='euc-kr',delimiter='|')
#     VDS_data.to_csv(csv,encoding='euc-kr',index=False)
#     print(str(i)+'success')

# data = pd.read_csv('Data/VDS_data_2019.csv',encoding='euc-kr')
# print(data['현재일기내용'].value_counts())