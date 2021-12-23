import pandas as pd

# VDS_CZE = pd.read_csv('Data/remain/VDS_weather_2014_CZE.csv',encoding='euc-kr')
# VDS_CZS = pd.read_csv('VDS/VDS_weather_2014_CZS.csv',encoding='euc-kr')
#
# VDS_weather = pd.concat([VDS_CZE,VDS_CZS],axis=0,sort=False)
# print(VDS_weather.head())
# VDS_weather.to_csv('VDS_weather_2014.csv',encoding='euc-kr',index=False)
#
# VDS_weather_01 = pd.read_csv('VDS/201901.csv',encoding='euc-kr')
# VDS_weather_02 = pd.read_csv('VDS/201402.csv',encoding='euc-kr')
# VDS_weather_03 = pd.read_csv('VDS/201403.csv',encoding='euc-kr')
# VDS_weather_11 = pd.read_csv('VDS/201511.csv',encoding='euc-kr')
# VDS_weather_12 = pd.read_csv('VDS/201512.csv',encoding='euc-kr')
#
#
# VDS_weather = pd.concat([VDS_weather_01,VDS_weather_02,VDS_weather_03],axis=0,sort=False)
# print(VDS_weather.head())
# VDS_weather.to_csv('VDS_weather_2014.csv',encoding='euc-kr',index=False)
#
# VDS_weather = pd.read_csv('Data/VDS/VDS_weather_2019.csv',encoding='euc-kr')
# VDS_traffic = pd.read_csv('Data/VDS/VDS_2019.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_traffic, right=VDS_weather, how='outer', on=['date','czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_data_2019.csv',encoding='euc-kr',index=False)
#
# VDS_code = pd.read_csv('Data/VDS/VDS_code_pt.csv', encoding='euc-kr')
# pavment = pd.read_csv('Data/road/Pavement_data.csv', encoding='euc-kr')
# start_code_data = pd.DataFrame()
# end_code_data = pd.DataFrame()
# for v_index in range(len(VDS_code)):
#     s_check = 0
#     e_check = 0
#     for p_index in range(len(pavment)):
#         if (VDS_code.iloc[v_index, 2] == pavment.iloc[p_index, 0]) and (VDS_code.iloc[v_index, 3] == pavment.iloc[p_index, 3]):
#             if VDS_code.iloc[v_index, 5] == pavment.iloc[p_index, 1]:
#                 print("start:", v_index, pavment.iloc[p_index, 1], pavment.iloc[p_index, 2], pavment.iloc[p_index, 5],
#                       pavment.iloc[p_index, 6], pavment.iloc[p_index, 7])
#                 new_data_s = {"index": v_index, "s_방향": pavment.iloc[p_index, 1], "s_차선": pavment.iloc[p_index, 2],
#                               "s_포장형태": pavment.iloc[p_index, 5], "s_표층재": pavment.iloc[p_index, 6],
#                               "s_교면구분": pavment.iloc[p_index, 7]}
#                 start_code_data = start_code_data.append(new_data_s, ignore_index=True)
#                 start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#                 s_check = 1
#         if s_check == 1:
#             break
#     if s_check == 0:
#         print("start value not found!!")
#         new_data_err = {"index": v_index, "s_방향": 0, "s_차선": 0, "s_포장형태": 0, "s_표층재": 0, "s_교면구분": 0}
#         start_code_data = start_code_data.append(new_data_err, ignore_index=True)
#         start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#
#     for p_index in range(len(pavment)):
#         if VDS_code.iloc[v_index, 2] == pavment.iloc[p_index, 0] and VDS_code.iloc[v_index, 4] == pavment.iloc[p_index, 4]:
#             if VDS_code.iloc[v_index, 5] == pavment.iloc[p_index, 1]:
#                 print("end:", v_index, pavment.iloc[p_index, 1], pavment.iloc[p_index, 2], pavment.iloc[p_index, 5],
#                       pavment.iloc[p_index, 6], pavment.iloc[p_index, 7])
#                 new_data_e = {"index": v_index, "e_방향": pavment.iloc[p_index, 1], "e_차선": pavment.iloc[p_index, 2],
#                               "e_포장형태": pavment.iloc[p_index, 5], "e_표층재": pavment.iloc[p_index, 6],
#                               "e_교면구분": pavment.iloc[p_index, 7]}
#                 end_code_data = end_code_data.append(new_data_e, ignore_index=True)
#                 end_code_data.to_csv('end_code_data.csv', encoding='euc-kr', index=False)
#                 e_check = 1
#         if e_check == 1:
#             break
#
#     if e_check == 0:
#         print("end value not found!!")
#         new_data_err = {"index": v_index, "e_방향": 0, "e_차선": 0, "e_포장형태": 0, "e_표층재": 0, "e_교면구분": 0}
#         end_code_data = end_code_data.append(new_data_err, ignore_index=True)
#         end_code_data.to_csv('end_code_data.csv', encoding='euc-kr', index=False)
#
# start_code = pd.read_csv('start_code_data.csv',encoding='euc-kr')
# end_code = pd.read_csv('end_code_data.csv',encoding='euc-kr')
# # start_code = start_code.drop([start_code.columns[0]],axis=1)
# # end_code = end_code.drop([end_code.columns[2]],axis=1)
# print(start_code.head())
# print(end_code.head())
# VDS_result = pd.concat([VDS_code,start_code,end_code],axis=1,sort=False)
# print(VDS_result.head())
# VDS_result.to_csv('VDS_code_pavement.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('VDS_at.csv',encoding='euc-kr')
# end = pd.read_csv('end.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe,right=end,how='left', on=['czId'],sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_at.csv',encoding='euc-kr',index=False)
#
# VDS_data = pd.read_csv('Data/Info/VDS_Info.csv',encoding='euc-kr')
# year = 2016
# month = [1,2,3,11,12]
# VDS_dataframe = pd.DataFrame()
# VDS_data_set = pd.DataFrame()
# for month_index in month:
#     if month_index == 1 or month_index == 3 or month_index == 12:
#         day = 32
#     elif month_index == 11:
#         day == 31
#     elif month_index == 2:
#         day = 29
#     for day_index in range(1,day):
#         date = str(year)+'-'+str(month_index)+'-'+str(day_index)
#         for i in range(len(VDS_data)):
#             VDS_data_set = {'date' : date, 'czId' : VDS_data.iloc[i,0],'routeNo' : VDS_data.iloc[i,1],
#                 'routeName': VDS_data.iloc[i,2] , 'czstart' : VDS_data.iloc[i,3],  'czend' : VDS_data.iloc[i,4],
#                 'direction' : VDS_data.iloc[i,5], 's_Xvalue':VDS_data.iloc[i,6], 's_Yvalue' : VDS_data.iloc[i,7],
#                 's_elevation': VDS_data.iloc[i, 8], 'e_Xvalue' : VDS_data.iloc[i,9], 'e_Yvalue' : VDS_data.iloc[i,10],
#                 'e_elevation' : VDS_data.iloc[i,11],'lane' : VDS_data.iloc[i,12],'pave' : VDS_data.iloc[i,13], 'surface' : VDS_data.iloc[i,14],
#                 'classification' : VDS_data.iloc[i,15], 'bridge_lane' : VDS_data.iloc[i,16], 'bridge_pave' : VDS_data.iloc[i,17],
#                 'bridge_surface' : VDS_data.iloc[i,18], 'tunnel' : VDS_data.iloc[i,19], 'VMSID' : VDS_data.iloc[i,20]}
#             VDS_dataframe = VDS_dataframe.append(VDS_data_set,ignore_index=True)
#             print(year,'년',month_index,'월',day_index,'일',i,'is complete')
# print(VDS_dataframe.info())
# VDS_dataframe.to_csv('VDS_frame_2016.csv',encoding='euc-kr',index=False)
#
# VDS_data = pd.read_csv('Data/Info/VDS_Info.csv',encoding='euc-kr')
# year = 2017
# month = [1,2,3,11,12]
# VDS_dataframe = pd.DataFrame()
# VDS_data_set = pd.DataFrame()
# for month_index in month:
#     if month_index == 1 or month_index == 3 or month_index == 12:
#         day = 32
#     elif month_index == 11:
#         day == 31
#     elif month_index == 2:
#         day = 29
#     for day_index in range(1,day):
#         date = str(year)+'-'+str(month_index)+'-'+str(day_index)
#         for i in range(len(VDS_data)):
#             VDS_data_set = {'date' : date, 'czId' : VDS_data.iloc[i,0],'routeNo' : VDS_data.iloc[i,1],
#                 'routeName': VDS_data.iloc[i,2] , 'czstart' : VDS_data.iloc[i,3],  'czend' : VDS_data.iloc[i,4],
#                 'direction' : VDS_data.iloc[i,5], 's_Xvalue':VDS_data.iloc[i,6], 's_Yvalue' : VDS_data.iloc[i,7],
#                 's_elevation': VDS_data.iloc[i, 8], 'e_Xvalue' : VDS_data.iloc[i,9], 'e_Yvalue' : VDS_data.iloc[i,10],
#                 'e_elevation' : VDS_data.iloc[i,11],'lane' : VDS_data.iloc[i,12],'pave' : VDS_data.iloc[i,13], 'surface' : VDS_data.iloc[i,14],
#                 'classification' : VDS_data.iloc[i,15], 'bridge_lane' : VDS_data.iloc[i,16], 'bridge_pave' : VDS_data.iloc[i,17],
#                 'bridge_surface' : VDS_data.iloc[i,18], 'tunnel' : VDS_data.iloc[i,19], 'VMSID' : VDS_data.iloc[i,20]}
#             VDS_dataframe = VDS_dataframe.append(VDS_data_set,ignore_index=True)
#             print(year,'년',month_index,'월',day_index,'일',i,'is complete')
# print(VDS_dataframe.info())
# VDS_dataframe.to_csv('VDS_frame_2017.csv',encoding='euc-kr',index=False)
#
# VDS_data = pd.read_csv('Data/Info/VDS_Info.csv',encoding='euc-kr')
# year = 2018
# month = [1,2,3,11,12]
# VDS_dataframe = pd.DataFrame()
# VDS_data_set = pd.DataFrame()
# for month_index in month:
#     if month_index == 1 or month_index == 3 or month_index == 12:
#         day = 32
#     elif month_index == 11:
#         day == 31
#     elif month_index == 2:
#         day = 29
#     for day_index in range(1,day):
#         date = str(year)+'-'+str(month_index)+'-'+str(day_index)
#         for i in range(len(VDS_data)):
#             VDS_data_set = {'date' : date, 'czId' : VDS_data.iloc[i,0],'routeNo' : VDS_data.iloc[i,1],
#                 'routeName': VDS_data.iloc[i,2] , 'czstart' : VDS_data.iloc[i,3],  'czend' : VDS_data.iloc[i,4],
#                 'direction' : VDS_data.iloc[i,5], 's_Xvalue':VDS_data.iloc[i,6], 's_Yvalue' : VDS_data.iloc[i,7],
#                 's_elevation': VDS_data.iloc[i, 8], 'e_Xvalue' : VDS_data.iloc[i,9], 'e_Yvalue' : VDS_data.iloc[i,10],
#                 'e_elevation' : VDS_data.iloc[i,11],'lane' : VDS_data.iloc[i,12],'pave' : VDS_data.iloc[i,13], 'surface' : VDS_data.iloc[i,14],
#                 'classification' : VDS_data.iloc[i,15], 'bridge_lane' : VDS_data.iloc[i,16], 'bridge_pave' : VDS_data.iloc[i,17],
#                 'bridge_surface' : VDS_data.iloc[i,18], 'tunnel' : VDS_data.iloc[i,19], 'VMSID' : VDS_data.iloc[i,20]}
#             VDS_dataframe = VDS_dataframe.append(VDS_data_set,ignore_index=True)
#             print(year,'년',month_index,'월',day_index,'일',i,'is complete')
# print(VDS_dataframe.info())
# VDS_dataframe.to_csv('VDS_frame_2018.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/VDS/VDS_frame_2019.csv',encoding='euc-kr')
# VDS_Day = pd.read_csv('Data/VDS/VDS_data_2019.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_Day, how='left', on=['date','czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_2019_result.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('VDS_2019_result.csv',encoding='euc-kr')
# VMS_Day = pd.read_csv('Data/VMS/VMS_2019_result.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VMS_Day, how='left', on=['date','VMSID'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_2019.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/VDS/VDS_VMS_code.csv',encoding='euc-kr')
# start = pd.read_csv('start.csv',encoding='euc-kr')
#
# VDS_dataframe = pd.read_csv('Data/result_Data/VDS_frame_2019.csv',encoding='euc-kr')
# VDS_VMS = pd.read_csv('Data/Info/VDS_VMS_Info.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_VMS, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('Data/result_Data/VDS_frame_2019.csv',encoding='euc-kr',index=False)

# VDS_weather = pd.read_csv('Data/remain/VDS_data_2018.csv',encoding='euc-kr')
# VDS_AWS = pd.read_csv('Data/Info/VDS_weather_Info.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_weather, right=VDS_AWS, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('Data/remain/VDS_data_2018.csv',encoding='euc-kr',index=False)

# VDS_dataframe = pd.read_csv('Data/result_Data/VDS_frame_2016.csv',encoding='euc-kr')
# VMS_Day = pd.read_csv('Data/remain/VMS_2016.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VMS_Day, how='left', on=['date','vmsmul'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_2016.csv',encoding='euc-kr',index=False)

# road = pd.read_csv('road_2016.csv',encoding='euc-kr')
# print(road.info())
# road['message'].fillna(method='ffill')
# print(road.info())

# VDS_dataframe = pd.read_csv('Data/result_Data/VDS_frame_2019.csv',encoding='euc-kr')
# VDS_grooving = pd.read_csv('Data/Info/VDS_grooving_Info.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_grooving, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('Data/result_Data/VDS_frame_2019.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/result_Data/VDS_frame_2016.csv',encoding='euc-kr')
# VDS_leak = pd.read_csv('Data/Info/VDS_leak_Info.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_leak, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('Data/result_Data/VDS_frame_2016.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/VDS/VDS_weather.csv',encoding='euc-kr')
# VDS_AWS = pd.read_csv('Data/VDS/VDS_AWS.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_AWS, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('Data/VDS/VDS_weather.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/final/road_2019.csv',encoding='euc-kr')
# VDS_AWS = pd.read_csv('Data/VDS/VDS_weather.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_AWS, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_weather.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('road_weather.csv',encoding='euc-kr')
# VDS_AWS = pd.read_csv('Data/VDS/VDS_data_2019.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=VDS_AWS, how='left', on=['date','czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_weather_VDS.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/final/road_2019.csv',encoding='euc-kr')
# AWS = pd.read_csv('Data/VDS/AWS_data_2019.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VDS_dataframe, right=AWS, how='left', on=['date','AWSID'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_weather_VDS.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('road_weather_VDS.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/weather/weather_2019.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=VDS_dataframe, right=weather, how='left', on=['date','area_code'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_weather_VDS_2019.csv',encoding='euc-kr',index=False)
#
# VDS_dataframe = pd.read_csv('Data/road_2019.csv',encoding='euc-kr')
# print(VDS_dataframe.info())

# road = pd.read_csv('road_2018.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/remain/VDS_data_2018.csv',encoding='euc-kr')
# road = pd.merge(left=road, right=weather, how='left', on=['date','czId'], sort=False)
# print(road.info())
# road.to_csv('road_2018_w.csv',encoding='euc-kr',index=False)

# road = pd.read_csv('road_2018.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/Info/VDS_weather_Info.csv',encoding='euc-kr')
# road = pd.merge(left=road, right=weather, how='left', on=['czId'], sort=False)
# print(road.info())
# road.to_csv('road_2018.csv',encoding='euc-kr',index=False)

# road = pd.read_csv('road_2017.csv',encoding='euc-kr')
# traffic = pd.read_csv('Data/remain/VDS_traffic_2017.csv',encoding='euc-kr')
# road = pd.merge(left=road, right=traffic, how='left', on=['date','czId'], sort=False)
# print(road.info())
# road.to_csv('road_2017.csv',encoding='euc-kr',index=False)

# VDS_dataframe = pd.read_csv('Data/result_Data/VDS_set_2018.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/Info/VDS_weather_Info.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=VDS_dataframe, right=weather, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_set_2018.csv',encoding='euc-kr',index=False)

# VDS_dataframe = pd.read_csv('Data/remain/VDS_w_2016.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/Info/VDS_weather_Info.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=VDS_dataframe, right=weather, how='left', on=['czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_w_2016.csv',encoding='euc-kr',index=False)

# VDS_dataframe = pd.read_csv('VDS_set_2018.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/remain/VDS_w_2018.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=VDS_dataframe, right=weather, how='left', on=['date','AWSID'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VDS_set_2018.csv',encoding='euc-kr',index=False)

# road = pd.read_csv('road_2016.csv',encoding='euc-kr')
# weather = pd.read_csv('VDS_set_2016.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=road, right=weather, how='left', on=['date','czId'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_2016.csv',encoding='euc-kr',index=False)

# road = pd.read_csv('road_2018.csv',encoding='euc-kr')
# weather = pd.read_csv('Data/remain/weather_2018.csv',encoding='euc-kr')
# VDS_data = pd.merge(left=road, right=weather, how='left', on=['date','area_code'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('road_2018_result.csv',encoding='euc-kr',index=False)

import missingno as msno
import matplotlib.pyplot as plt
# import pandas as pd
#
# VDS_dataframe = pd.read_csv('Data/road_2019.csv',encoding='euc-kr')
# VDS_dataframe['안개계속시간(hr)'] = VDS_dataframe['안개계속시간(hr)'].fillna(0)
# VDS_dataframe['일강수량(mm)'] = VDS_dataframe['일강수량(mm)'].fillna(0)
# VDS_dataframe['강수계속시간(hr)'] = VDS_dataframe['강수계속시간(hr)'].fillna(0)
# VDS_dataframe['평균이슬점온도(°C)'] = VDS_dataframe['평균이슬점온도(°C)'].fillna(method='ffill')
# VDS_dataframe['평균상대습도(%)'] = VDS_dataframe['평균상대습도(%)'].fillna(method='ffill')
#VDS_dataframe['합계일조시간(hr)'] = VDS_dataframe['합계일조시간(hr)'].fillna(method='ffill')
# VDS_dataframe['최대풍속(m/s)'] = VDS_dataframe['최대풍속(m/s)'].fillna(method='ffill')
# VDS_dataframe['최대풍속풍향(16방위)'] = VDS_dataframe['최대풍속풍향(16방위)'].fillna(method='ffill')
# VDS_dataframe['평균풍속(m/s)'] = VDS_dataframe['평균풍속(m/s)'].fillna(method='ffill')
# VDS_dataframe['평균지면온도(°C)'] = VDS_dataframe['평균지면온도(°C)'].fillna(method='ffill')
# VDS_dataframe['최고기온시각(hhmi)'] = VDS_dataframe['최고기온시각(hhmi)'].fillna(method='ffill')
# VDS_dataframe['최저기온시각(hhmi)'] = VDS_dataframe['최저기온시각(hhmi)'].fillna(method='ffill')
# print(VDS_dataframe.info())
# msno.matrix(VDS_dataframe)
# plt.show()
# VDS_dataframe.to_csv('Data/road_2019.csv',encoding='euc-kr',index=False)

# road16 = pd.read_csv('Data/road_2016.csv',encoding='euc-kr')
# road17 = pd.read_csv('Data/road_2017.csv',encoding='euc-kr')
# road18 = pd.read_csv('Data/road_2018.csv',encoding='euc-kr')
# road19 = pd.read_csv('Data/road_2019.csv',encoding='euc-kr')
#
# print('2016년')
# print(road16.info())
# print('\n2017년')
# print(road17.info())
# print('\n2018년')
# print(road18.info())
# print('\n2019년')
# print(road19.info())
#
# msno.matrix(road16)
# msno.matrix(road17)
# msno.matrix(road18)
# msno.matrix(road19)
# plt.show()

# import pandas as pd
#
# data = pd.read_csv('Data/Info/VDS_Info.csv',encoding='euc-kr')
# road = pd.read_csv('Data/Info/Road_Info.csv',encoding='euc-kr')
#
# df = pd.DataFrame()
# for i in range(len(data)):
#     for j in range(len(road)):
#         if data['direction'].iloc[i] == 'E':
#             if data['routeNo'].iloc[i] == road['노선번호'].iloc[j]:
#                 if data['czstart'].iloc[i] <= road['이정'].iloc[j] and data['czend'].iloc[i] >= road['이정'].iloc[j]:
#                     road_data = {'czId' : data['czId'].iloc[i],'routeNo':data['routeNo'].iloc[i],'direction':data['direction'].iloc[i],
#                                  'Xvalue' : road['X좌표값'].iloc[j],'Yvalue':road['Y좌표값'].iloc[j]}
#                     print(i,road_data,road['이정'].iloc[j])
#                     df = df.append(road_data,ignore_index=True)
#         else:
#             if data['routeNo'].iloc[i] == road['노선번호'].iloc[j]:
#                 if data['czstart'].iloc[i] >= road['이정'].iloc[j] and data['czend'].iloc[i] <= road['이정'].iloc[j]:
#                     road_data = {'czId' : data['czId'].iloc[i],'routeNo':data['routeNo'].iloc[i],'direction':data['direction'].iloc[i],
#                                  'Xvalue' : road['X좌표값'].iloc[j],'Yvalue':road['Y좌표값'].iloc[j]}
#                     print(i,road_data,road['이정'].iloc[j])
#                     df = df.append(road_data,ignore_index=True)
#
# print(df.head())
# df.to_csv('GPSData.csv',encoding='euc-kr')

# data_E = pd.read_csv('final_2019_E.csv',encoding='euc-kr')
# score_E = pd.read_csv('score_E.csv',encoding='euc-kr')
# data_S = pd.read_csv('final_2019_S.csv',encoding='euc-kr')
# score_S = pd.read_csv('score_S.csv',encoding='euc-kr')
#
# final_E = pd.merge(left=data_E, right=score_E, how='outer', on=['date','czId'], sort=False)
# final_E.to_csv('final_E.csv',encoding='euc-kr',index=False)
#
# final_S = pd.merge(left=data_S, right=score_S, how='outer', on=['date','czId'], sort=False)
# final_S.to_csv('final_S.csv',encoding='euc-kr',index=False)

# final_E = pd.read_csv('final_E.csv',encoding='euc-kr')
#
# df = pd.DataFrame()
# for i in range(len(final_E)):
#     if final_E['위험도'].iloc[i] == 2:
#         risk = {'score1': 'red', 'score2': '#CF1414'}
#     elif final_E['위험도'].iloc[i] == 1:
#         risk = {'score1': 'yellow', 'score2': '#FFE062'}
#     else:
#         risk = {'score1': 'green', 'score2': '#5CE546'}
#     df = df.append(risk)
# print(df)
#
# final_E = pd.concat([final_E,df],axis=1,sort=False)
# print(final_E.info())
# print(final_E.head())
# final_E.to_csv('final_E.csv',encoding='euc-kr',index=False)
#
# final_S = pd.read_csv('final_S.csv',encoding='euc-kr')

# df = pd.DataFrame()
# for i in range(len(final_S)):
#     if final_S['위험도'].iloc[i] == 2:
#         risk = {'score1': 'red', 'score2': '#CF1414'}
#     elif final_S['위험도'].iloc[i] == 1:
#         risk = {'score1': 'yellow', 'score2': '#FFE062'}
#     else:
#         risk = {'score1': 'green', 'score2': '#5CE546'}
#     df = df.append(risk)
# print(df)

# final_S = pd.concat([final_S,df],axis=1,sort=False)
# print(final_S.info())
# print(final_S.head())
# final_S.to_csv('final_S.csv',encoding='euc-kr',index=False)
