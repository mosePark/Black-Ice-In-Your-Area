import pandas as pd

# snow_2015 = pd.read_csv('snow_remove_2015.csv',encoding='euc-kr')
# snow_2016 = pd.read_csv('snow_remove_2016.csv',encoding='euc-kr')
# snow_2017 = pd.read_csv('snow_remove_2017.csv',encoding='euc-kr')
# snow_2018 = pd.read_csv('snow_remove_2018.csv',encoding='euc-kr')
# snow_2019 = pd.read_csv('snow_remove_2019.csv',encoding='euc-kr')
#
# snow_remove_data = pd.concat([snow_2015,snow_2016,snow_2017,snow_2018,snow_2019])
# snow_remove_data.to_csv('snow_remove_data.csv',encoding='euc-kr',index=False)
#데이터 import
# snow = pd.read_csv('snow_remove_data.csv',encoding='euc-kr')check_start = 1
#pavement = pd.read_csv('Pavement_data.csv',encoding='euc-kr')
#road = pd.read_csv('Data/Road_data.csv', encoding='euc-kr')
#공사형태 제거
#pavement = pavement.drop([pavement.columns[11]],axis=1)
#데이터합치기(pavement+road)

# for p_index in range(len(pavement)):
#     for r_index in range(len(road)):
#         if pavement.iloc[p_index, 2] == road.iloc[r_index, 0]:
#             for p_start in range(len(pavement)):
#                 for r_start in range(len(road)):
#                     if pavement.iloc[p_index,2] == road.iloc[r_index,0] and pavement.iloc[p_start,6] == road.iloc[r_start,2]:
#                         print(p_index,road.iloc[r_start,3])
#_data : 데이터 복사 / pavement + road 시작
# pavement_data = pavement
# road_data = road
# start_code_data = pd.DataFrame()
# end_code_data = pd.DataFrame()
# for p_start in range(len(pavement_data)):
#     check_start = 0
#     check_end = 0
#     for r_start in range(len(road_data)):
#         if pavement.iloc[p_start, 6] == road.iloc[r_start, 2] and pavement.iloc[p_start,2] == road.iloc[r_start,0]:
#             print("start:",p_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_s = {"index" : p_start ,"s_Xvalue": road.iloc[r_start, 3],"s_Yvalue":road.iloc[r_start, 4]}
#             start_code_data = start_code_data.append(new_data_s,ignore_index=True)
#             start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#             check_start = 1
#
#         if pavement.iloc[p_start, 7] == road.iloc[r_start, 2] and pavement.iloc[p_start,2] == road.iloc[r_start,0]:
#             print("end:",p_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_e = {"index" : p_start, "end_Xvalue": road.iloc[r_start, 3],"end_Yvalue":road.iloc[r_start, 4]}
#             end_code_data = end_code_data.append(new_data_e,ignore_index=True)
#             end_code_data.to_csv('end_code_data.csv',encoding='euc-kr',index=False)
#             check_end = 1
#
#     if check_start == 0:
#         print("start value not found!!")
#         new_data_err = {"index" : p_start ,"s_Xvalue": 0,"s_Yvalue":0}
#         start_code_data = start_code_data.append(new_data_err, ignore_index=True)
#         start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#     if check_end == 0:
#         print("end value not found!!")
#         new_data_err = {"index": p_start, "end_Xvalue": 0, "end_Yvalue": 0}
#         end_code_data = end_code_data.append(new_data_err, ignore_index=True)
#         end_code_data.to_csv('end_code_data.csv', encoding='euc-kr', index=False)
# pavement_data = pavement
# start_code = pd.read_csv('start_code_data.csv',encoding='euc-kr')
# end_code = pd.read_csv('end_code_data.csv',encoding='euc-kr')
# start_code = start_code.drop([start_code.columns[0]],axis=1)
# end_code = end_code.drop([end_code.columns[2]],axis=1)
# print(start_code.head())
# print(end_code.head())
# pavement_result = pd.concat([pavement,start_code,end_code],axis=1,sort=False)
# print(pavement_result.head())
# pavement_result.to_csv('pavement_result.csv',encoding='euc-kr',index=False)
#pavement + road 끝

#snow + road 시작
# snow_data = snow
# road_data = road
# start_snow_data = pd.DataFrame() #제설작업시점데이터
# end_snow_data = pd.DataFrame() #제설작업종접데이터
# for s_start in range(len(snow_data)):
#     check_start = 0
#     check_end = 0
#     for r_start in range(len(road_data)):
#         if snow_data.iloc[s_start, 3] == road.iloc[r_start, 0] and snow_data.iloc[s_start,4] == road.iloc[r_start,2]:
#             print("start:",s_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_s = {"index" : s_start ,"s_Xvalue": road.iloc[r_start, 3],"s_Yvalue":road.iloc[r_start, 4]}
#             start_snow_data = start_snow_data.append(new_data_s,ignore_index=True)
#             start_snow_data.to_csv('start_snow_data.csv', encoding='euc-kr', index=False)
#             check_start = 1
#
#         if snow_data.iloc[s_start, 3] == road.iloc[r_start, 0] and snow_data.iloc[s_start,5] == road.iloc[r_start,2]:
#             print("end:",s_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_e = {"index" : s_start, "end_Xvalue": road.iloc[r_start, 3],"end_Yvalue":road.iloc[r_start, 4]}
#             end_snow_data = end_snow_data.append(new_data_e,ignore_index=True)
#             end_snow_data.to_csv('end_snow_data.csv',encoding='euc-kr',index=False)
#             check_end = 1
#
#     if check_start == 0:
#         print("start value not found!!")
#         new_data_err = {"index" : s_start ,"s_Xvalue": 0,"s_Yvalue":0}
#         start_snow_data = start_snow_data.append(new_data_err, ignore_index=True)
#         start_snow_data.to_csv('start_snow_data.csv', encoding='euc-kr', index=False)
#     if check_end == 0:
#         print("end value not found!!")
#         new_data_err = {"index": s_start, "end_Xvalue": 0, "end_Yvalue": 0}
#         end_snow_data = end_snow_data.append(new_data_err, ignore_index=True)
#         end_snow_data.to_csv('end_snow_data.csv', encoding='euc-kr', index=False)

# snow_data = snow
# start_snow = pd.read_csv('start_snow_data.csv',encoding='euc-kr')
# end_snow = pd.read_csv('end_snow_data.csv',encoding='euc-kr')
# start_snow = start_snow.drop([start_snow.columns[0]],axis=1)
# end_snow = end_snow.drop([end_snow.columns[2]],axis=1)
# print(start_snow.head())
# print(end_snow.head())
# snow_result = pd.concat([snow_data,start_snow,end_snow],axis=1,sort=False)
# print(snow_result.head())
# snow_result.to_csv('snow_result.csv',encoding='euc-kr',index=False)
#snow + road 끝

#units_code + units_data
# units_code = pd.read_csv('units_code.csv',encoding='euc-kr')
# units_data = pd.read_csv('units_data.csv',encoding='euc-kr')
# print(len(units_code))
# print(len(units_data))
# start_units_data = pd.DataFrame() #VDS시점데이터
# end_unist_data = pd.DataFrame() #VDS종접데이터
# for s_start in range(len(units_data)):
#     check = 0
#     for r_start in range(len(units_code)):
#         if units_data.iloc[s_start, 1] == units_code.iloc[r_start, 1]:
#             print("start:",s_start,units_code.iloc[r_start, 0],units_code.iloc[r_start, 1],units_code.iloc[r_start, 2],units_code.iloc[r_start, 3],units_code.iloc[r_start, 4])
#             new_data_s = {"index" : s_start ,"영업소코드":units_code.iloc[r_start,1],"s_Xvalue": units_code.iloc[r_start, 3],"s_Yvalue":units_code.iloc[r_start, 4]}
#             start_units_data = start_units_data.append(new_data_s,ignore_index=True)
#             start_units_data.to_csv('units_data_checked.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("start value not found!!")
#         new_data_err = {"index" : s_start ,"s_Xvalue": 0,"s_Yvalue":0}
#         start_units_data = start_units_data.append(new_data_err, ignore_index=True)
#         start_units_data.to_csv('units_data_checked.csv', encoding='euc-kr', index=False)
#
# checked_units = pd.read_csv('units_data_checked.csv',encoding='euc-kr')
# checked_units = checked_units.drop([checked_units.columns[0],checked_units.columns[3]],axis=1)
# print(checked_units.head())
# units_result = pd.concat([units_data,checked_units],axis=1,sort=False)
# print(units_result.head())
# units_result.to_csv('units_result.csv',encoding='euc-kr',index=False)
#units_code + units_data

#VDS_code + VDS_data
# import pandas as pd
# VDS_data = pd.read_csv('VDS/VDS_2014.csv',encoding='euc-kr')
# VDS_code = pd.read_csv('VDS/VDS_code.csv',encoding='euc-kr')
#
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2014.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2014.csv', encoding='euc-kr', index=False)
#
# VDS_data_check = pd.read_csv('VDS_weather_check_201401.csv',encoding='euc-kr') #VDS_data_check_YYYYMM.csv
# VDS_result = pd.concat([VDS_data,VDS_data_check],axis=1,sort=False)
# print(VDS_result.head())
# VDS_result.to_csv('VDS_result_201401.csv',encoding='euc-kr',index=False) #VDS_result_YYYYMM.csv

# VDS_data = pd.read_csv('VDS/VDS_2015.csv',encoding='euc-kr')
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2015.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2015.csv', encoding='euc-kr', index=False)
#
# VDS_data = pd.read_csv('VDS/VDS_2016.csv',encoding='euc-kr')
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2016.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2016.csv', encoding='euc-kr', index=False)
#
# VDS_data = pd.read_csv('VDS/VDS_2017.csv',encoding='euc-kr')
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2017.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2017.csv', encoding='euc-kr', index=False)
#
# VDS_data = pd.read_csv('VDS/VDS_2018.csv',encoding='euc-kr')
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2018.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2018.csv', encoding='euc-kr', index=False)
#
# VDS_data = pd.read_csv('VDS/VDS_2019.csv',encoding='euc-kr')
# start_VDS_data = pd.DataFrame() #VDS시점데이터
# end_VDS_data = pd.DataFrame() #VDS종접데이터
# for VD_start in range(len(VDS_data)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_data.iloc[VD_start, 1] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VD_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VD_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             start_VDS_data = start_VDS_data.append(new_data_s,ignore_index=True)
#             start_VDS_data.to_csv('VDS_data_check_2019.csv', encoding='euc-kr', index=False)
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VD_start ,"Xvalue": 0,"Yvalue":0}
#         start_VDS_data = start_VDS_data.append(new_data_err, ignore_index=True)
#         start_VDS_data.to_csv('VDS_data_check_2019.csv', encoding='euc-kr', index=False)
#VDS_code + VDS_data

#VDS_code + weather
# import pandas as pd
# #VDS_weather : 기상데이터, VDS_code : VDS코드,좌표정보,
# VDS_weather = pd.read_csv('weather/201401.csv',encoding='euc-kr') #weather/YYYYMM.csv
# VDS_code = pd.read_csv('VDS/VDS_code.csv',encoding='euc-kr')
# VDS_data_frame = pd.DataFrame()
# for VW_start in range(len(VDS_weather)):
#     check = 0
#     for VC_start in range(len(VDS_code)):
#         if VDS_weather.iloc[VW_start, 2] == VDS_code.iloc[VC_start, 0]:
#             print("start:",VW_start,VDS_code.iloc[VC_start, 0],VDS_code.iloc[VC_start, 1],VDS_code.iloc[VC_start, 2],VDS_code.iloc[VC_start, 3])
#             new_data_s = {"index" : VW_start ,"Xvalue": VDS_code.iloc[VC_start, 1],"Yvalue":VDS_code.iloc[VC_start, 2]}
#             VDS_data_frame = VDS_data_frame.append(new_data_s,ignore_index=True)
#             VDS_data_frame.to_csv('VDS_weather_check_201401.csv', encoding='euc-kr', index=False) #VDS_weather_check_YYYYMM.csv
#             check = 1
#
#     if check == 0:
#         print("value not found!!")
#         new_data_err = {"index" : VW_start ,"Xvalue": 0,"Yvalue":0}
#         VDS_data_frame = VDS_data_frame.append(new_data_err, ignore_index=True)
#         VDS_data_frame.to_csv('VDS_weather_check_201401.csv', encoding='euc-kr', index=False) #VDS_weather_check_YYYYMM.csv
#
# VDS_weather_check = pd.read_csv('VDS_weather_check_201401.csv',encoding='euc-kr') #VDS_weather_check_YYYYMM.csv
# VDS_weather_result = pd.concat([VDS_weather,VDS_weather_check],axis=1,sort=False)
# print(VDS_weather_result.head())
# VDS_weather_result.to_csv('VDS_weather_result_201401.csv',encoding='euc-kr',index=False) #VDS_weather_result_YYYYMM.csv
# VDS_code + weather

#VDS_code + Road_data
# road = pd.read_csv('Data/Road_data.csv', encoding='euc-kr')
# VDS = pd.read_csv('VDS_code_E.csv',encoding='euc-kr')
# start_code_data = pd.DataFrame()
# end_code_data = pd.DataFrame()
# for V_data in range(len(VDS)):
#     check_start = 0
#     check_end = 0
#     for R_data in range(len(road)):
#         if VDS.iloc[V_data, 3] == road.iloc[R_data, 2] and VDS.iloc[V_data, 2] == road.iloc[R_data, 0]:
#                 print("start:",V_data,road.iloc[R_data, 0],road.iloc[R_data, 2],road.iloc[R_data, 3],road.iloc[R_data, 4])
#                 new_data_s = {"index" : V_data ,"s_Xvalue": road.iloc[R_data, 3],"s_Yvalue":road.iloc[R_data, 4]}
#                 start_code_data = start_code_data.append(new_data_s,ignore_index=True)
#                 start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#                 check_start = 1
#
#         if VDS.iloc[V_data, 4] == road.iloc[R_data, 2] and VDS.iloc[V_data, 2] == road.iloc[R_data, 0]:
#             print("end:",V_data,road.iloc[R_data, 0],road.iloc[R_data, 2],road.iloc[R_data, 3],road.iloc[R_data, 4])
#             new_data_e = {"index" : V_data, "end_Xvalue": road.iloc[R_data, 3],"end_Yvalue":road.iloc[R_data, 4]}
#             end_code_data = end_code_data.append(new_data_e,ignore_index=True)
#             end_code_data.to_csv('end_code_data.csv',encoding='euc-kr',index=False)
#             check_end = 1
#
#     if check_start == 0:
#         print("start value not found!!")
#         new_data_err = {"index" : V_data,"s_Xvalue": 0,"s_Yvalue":0}
#         start_code_data = start_code_data.append(new_data_err, ignore_index=True)
#         start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#     if check_end == 0:
#         print("end value not found!!")
#         new_data_err = {"index": V_data, "end_Xvalue": 0, "end_Yvalue": 0}
#         end_code_data = end_code_data.append(new_data_err, ignore_index=True)
#         end_code_data.to_csv('end_code_data.csv', encoding='euc-kr', index=False)
# VDS_data = VDS
# start_code = pd.read_csv('start_code_data.csv',encoding='euc-kr')
# end_code = pd.read_csv('end_code_data.csv',encoding='euc-kr')
# # start_code = start_code.drop([start_code.columns[0]],axis=1)
# # end_code = end_code.drop([end_code.columns[2]],axis=1)
# print(start_code.head())
# print(end_code.head())
# VDS_result = pd.concat([VDS_data,start_code,end_code],axis=1,sort=False)
# print(VDS_result.head())
# VDS_result.to_csv('VDS_code_E_result.csv',encoding='euc-kr',index=False)

# Grooving + road
# for p_index in range(len(pavement)):
#     for r_index in range(len(road)):
#         if pavement.iloc[p_index, 2] == road.iloc[r_index, 0]:
#             for p_start in range(len(pavement)):
#                 for r_start in range(len(road)):
#                     if pavement.iloc[p_index,2] == road.iloc[r_index,0] and pavement.iloc[p_start,6] == road.iloc[r_start,2]:
#                         print(p_index,road.iloc[r_start,3])

#_data : 데이터 복사 / pavement + road 시작
# grooving_data = pd.read_csv('Data/Grooving.csv',encoding='euc-kr')
# road = pd.read_csv('Data/Road_data.csv',encoding='euc-kr')
# start_code_data = pd.DataFrame()
# end_code_data = pd.DataFrame()
# for g_start in range(len(grooving_data)):
#     check_start = 0
#     check_end = 0
#     for r_start in range(len(road)):
#         if grooving_data.iloc[g_start, 9] == road.iloc[r_start, 2] and grooving_data.iloc[g_start,2] == road.iloc[r_start,0]:
#             print("start:",g_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_s = {"index" : g_start ,"s_Xvalue": road.iloc[r_start, 3],"s_Yvalue":road.iloc[r_start, 4]}
#             start_code_data = start_code_data.append(new_data_s,ignore_index=True)
#             start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#             check_start = 1
#
#         if grooving_data.iloc[g_start, 10] == road.iloc[r_start, 2] and grooving_data.iloc[g_start,2] == road.iloc[r_start,0]:
#             print("end:",g_start,road.iloc[r_start, 0],road.iloc[r_start, 2],road.iloc[r_start, 3],road.iloc[r_start, 4])
#             new_data_e = {"index" : g_start, "end_Xvalue": road.iloc[r_start, 3],"end_Yvalue":road.iloc[r_start, 4]}
#             end_code_data = end_code_data.append(new_data_e,ignore_index=True)
#             end_code_data.to_csv('end_code_data.csv',encoding='euc-kr',index=False)
#             check_end = 1
#
#     if check_start == 0:
#         print(str(g_start) + " start value not found!!")
#         new_data_err = {"index" : g_start ,"s_Xvalue": 0,"s_Yvalue":0}
#         start_code_data = start_code_data.append(new_data_err, ignore_index=True)
#         start_code_data.to_csv('start_code_data.csv', encoding='euc-kr', index=False)
#     if check_end == 0:
#         print(str(g_start) + " end value not found!!")
#         new_data_err = {"index": g_start, "end_Xvalue": 0, "end_Yvalue": 0}
#         end_code_data = end_code_data.append(new_data_err, ignore_index=True)
#         end_code_data.to_csv('end_code_data.csv', encoding='euc-kr', index=False)
# start_code = pd.read_csv('start_code_data.csv',encoding='euc-kr')
# end_code = pd.read_csv('end_code_data.csv',encoding='euc-kr')
# start_code = start_code.drop([start_code.columns[0]],axis=1)
# end_code = end_code.drop([end_code.columns[2]],axis=1)
# print(start_code.head())
# print(end_code.head())
# pavement_result = pd.concat([grooving_data,start_code,end_code],axis=1,sort=False)
# print(pavement_result.head())
# pavement_result.to_csv('grooving_result.csv',encoding='euc-kr',index=False)