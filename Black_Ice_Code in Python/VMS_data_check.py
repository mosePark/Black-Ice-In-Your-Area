import pandas as pd

# VMS_data_1 = pd.read_csv('Data/remain/2018/Vms_Day_20180201.csv',encoding='euc-kr')
# VMS_data_2 = pd.read_csv('Data/remain/2018/Vms_Day_20180202.csv',encoding='euc-kr')
# VMS_data_3 = pd.read_csv('Data/remain/2018/Vms_Day_20180203.csv',encoding='euc-kr')
# VMS_data_4 = pd.read_csv('Data/remain/2018/Vms_Day_20180204.csv',encoding='euc-kr')
# VMS_data_5 = pd.read_csv('Data/remain/2018/Vms_Day_20180205.csv',encoding='euc-kr')
# VMS_data_6 = pd.read_csv('Data/remain/2018/Vms_Day_20180206.csv',encoding='euc-kr')
# VMS_data_7 = pd.read_csv('Data/remain/2018/Vms_Day_20180207.csv',encoding='euc-kr')
# VMS_data_8 = pd.read_csv('Data/remain/2018/Vms_Day_20180208.csv',encoding='euc-kr')
# VMS_data_9 = pd.read_csv('Data/remain/2018/Vms_Day_20180209.csv',encoding='euc-kr')
# VMS_data_10 = pd.read_csv('Data/remain/2018/Vms_Day_20180210.csv',encoding='euc-kr')
# VMS_data_11 = pd.read_csv('Data/remain/2018/Vms_Day_20180211.csv',encoding='euc-kr')
# VMS_data_12 = pd.read_csv('Data/remain/2018/Vms_Day_20180212.csv',encoding='euc-kr')
# VMS_data_13 = pd.read_csv('Data/remain/2018/Vms_Day_20180213.csv',encoding='euc-kr')
# VMS_data_14 = pd.read_csv('Data/remain/2018/Vms_Day_20180214.csv',encoding='euc-kr')
# VMS_data_15 = pd.read_csv('Data/remain/2018/Vms_Day_20180215.csv',encoding='euc-kr')
# VMS_data_16 = pd.read_csv('Data/remain/2018/Vms_Day_20180216.csv',encoding='euc-kr')
# VMS_data_17 = pd.read_csv('Data/remain/2018/Vms_Day_20180217.csv',encoding='euc-kr')
# VMS_data_18 = pd.read_csv('Data/remain/2018/Vms_Day_20180218.csv',encoding='euc-kr')
# VMS_data_19 = pd.read_csv('Data/remain/2018/Vms_Day_20180219.csv',encoding='euc-kr')
# VMS_data_20 = pd.read_csv('Data/remain/2018/Vms_Day_20180220.csv',encoding='euc-kr')
# VMS_data_21 = pd.read_csv('Data/remain/2018/Vms_Day_20180221.csv',encoding='euc-kr')
# VMS_data_22 = pd.read_csv('Data/remain/2018/Vms_Day_20180222.csv',encoding='euc-kr')
# VMS_data_23 = pd.read_csv('Data/remain/2018/Vms_Day_20180223.csv',encoding='euc-kr')
# VMS_data_24 = pd.read_csv('Data/remain/2018/Vms_Day_20180224.csv',encoding='euc-kr')
# VMS_data_25 = pd.read_csv('Data/remain/2018/Vms_Day_20180225.csv',encoding='euc-kr')
# VMS_data_26 = pd.read_csv('Data/remain/2018/Vms_Day_20180226.csv',encoding='euc-kr')
# VMS_data_27 = pd.read_csv('Data/remain/2018/Vms_Day_20180227.csv',encoding='euc-kr')
# VMS_data_28 = pd.read_csv('Data/remain/2018/Vms_Day_20180228.csv',encoding='euc-kr')
# VMS_data_29 = pd.read_csv('Data/remain/2018/Vms_Day_20180201.csv',encoding='euc-kr')
# VMS_data_20 = pd.read_csv('Data/remain/2018/Vms_Day_20180201.csv',encoding='euc-kr')
# VMS_data_31 = pd.read_csv('Data/remain/2018/Vms_Day_20180201.csv',encoding='euc-kr')

# for i in range(1,29):
#     # if i == 1:
#     #     continue
#     if i < 10:
#         text = 'Data/remain/2018/Vms_Day_2018020'+str(i)+'.csv'
#     # elif i == 27:
#     #     continue
#     else:
#         text = 'Data/remain/2018/Vms_Day_201802' + str(i) + '.csv'
#     VMS_data = pd.read_csv(text,encoding='euc-kr')
#     VMS_data.columns = ['생성시간','기관코드','VMSID','VMSTYPE','VMSSEQNO','VMSMSGCODE','표출시간','내용']
#     VMS_data.to_csv(text,encoding='euc-kr',index=False)
#     print(text+' is complete!')
#
# VMS_data = pd.DataFrame()
# for i in range(1,29):
#
#     if i < 10:
#         text = 'Data/remain/2018/Vms_Day_2018020'+str(i)+'.csv'
#     # elif i == 27:
#     #     continue
#     else:
#         text = 'Data/remain/2018/Vms_Day_201802' + str(i) + '.csv'
#     VMS_data_Day = pd.read_csv(text,encoding='euc-kr')
#     VMS_data = VMS_data.append(VMS_data_Day,ignore_index=True)
#     print(text+' is complete!')
# VMS_data.to_csv('VMS_Day_201802.csv',encoding='euc-kr',index=False)

# VMS_data = pd.concat([VMS_data_1,VMS_data_2,VMS_data_3,VMS_data_4,VMS_data_5,VMS_data_6,VMS_data_7,VMS_data_8,VMS_data_9,VMS_data_10,
#                       VMS_data_11,VMS_data_12,VMS_data_13,VMS_data_14,VMS_data_15,VMS_data_16,VMS_data_17,VMS_data_18,VMS_data_19,VMS_data_20
#                       ,VMS_data_21,VMS_data_22,VMS_data_23,VMS_data_24,VMS_data_25,VMS_data_26,VMS_data_27,VMS_data_28],axis=0,sort=False)


# VMS_01 = pd.read_csv('VMS_Day_201801.csv',encoding='euc-kr')
# VMS_02 = pd.read_csv('VMS_Day_201802.csv',encoding='euc-kr')
# VMS_03 = pd.read_csv('VMS_Day_201803.csv',encoding='euc-kr')
# VMS_11 = pd.read_csv('VMS_Day_201811.csv',encoding='euc-kr')
# VMS_12 = pd.read_csv('VMS_Day_201812.csv',encoding='euc-kr')
#
# VMS_data = pd.concat([VMS_01,VMS_02,VMS_03,VMS_11,VMS_12],axis=0,sort=False)
# print(VMS_data.head())
# VMS_data.to_csv('VMS_Day_2018.csv',encoding='euc-kr',index=False)

# VMS_data = pd.read_csv('Data/VMS/VMS_code.csv',encoding='euc-kr')
# year = 2019
# month = [1,2,3,11,12]
# columns = ['date','VMSID']
# VMS_dataframe = pd.DataFrame(columns=columns)
# VMS_data_set = pd.DataFrame()
# for month_index in month:
#     if month_index == 1 or month_index == 3 or month_index == 12:
#         day = 32
#     elif month_index == 11:
#         day == 31
#     elif month_index == 2:
#         day = 29
#     for day_index in range(1,day):
#         date = str(year)+'-'+str(month_index)+'-'+str(day_index)
#         for i in range(len(VMS_data)):
#             VMS_data_set = {'date' : date, 'VMSID' : VMS_data.iloc[i,0],'도로명' : VMS_data.iloc[i,3],
#                 '노선번호': VMS_data.iloc[i,4] ,'방향' : VMS_data.iloc[i,5]}
#             VMS_dataframe = VMS_dataframe.append(VMS_data_set,ignore_index=True)
#             print(month_index,'월',day_index,'일',i,'is complete')
# print(VMS_dataframe.info())
# VMS_dataframe.to_csv('Data/VMS/VMS_frame_2019.csv',encoding='euc-kr',index=False)

# VMS_dataframe = pd.read_csv('Data/VMS/VMS_frame_2019.csv',encoding='euc-kr')
# VMS_Day = pd.read_csv('Data/VMS/VMS_Day_2019.csv',encoding='euc-kr')
#
# VDS_data = pd.merge(left=VMS_dataframe, right=VMS_Day, how='left', on=['date','VMSID'], sort=False)
# print(VDS_data.info())
# VDS_data.to_csv('VMS_2019_result.csv',encoding='euc-kr',index=False)

# VMS_dataframe = pd.read_csv('VMS_frame_12.csv',encoding='euc-kr')
# VMS_data = pd.read_csv('Data/VMS_Day_2019.csv',encoding='euc-kr')
# index_frame = pd.DataFrame()
# for frame in range(len(VMS_dataframe)):
#     check = 0
#     for Day in range(len(VMS_data)):
#         if VMS_dataframe.iloc[frame,0] == VMS_data.iloc[Day,0] and VMS_dataframe.iloc[frame,1] == VMS_data.iloc[Day,2]:
#             print('index :',frame,VMS_data.iloc[Day,0],VMS_data.iloc[Day,1],VMS_data.iloc[Day,2],VMS_data.iloc[Day,3],
#                   VMS_data.iloc[Day,4],VMS_data.iloc[Day,5],VMS_data.iloc[Day,6],VMS_data.iloc[Day,7])
#             index_frame = {"기관코드" : VMS_data.iloc[Day,1] ,"VMSTYPE": VMS_data.iloc[Day,3],"VMSSEQNO":VMS_data.iloc[Day,4],
#                         "VMSMSGCODE" : VMS_data.iloc[Day,5],"표출시간" : VMS_data.iloc[Day,6] ,"Message" : VMS_data.iloc[Day,7] }
#             VMS_dataframe = VMS_dataframe.append(index_frame,ignore_index=True)
#     if check == 0:
#         print(frame,'Value not found')
#         index_frame = {"기관코드": -1, "VMSTYPE": -1,"VMSSEQNO": -1,"VMSMSGCODE": -1, "표출시간": -1,"Message": -1}
#         VMS_dataframe = VMS_dataframe.append(index_frame, ignore_index=True)
#
# print(VMS_dataframe.head())
# VMS_dataframe.to_csv('VMS_frame_2019_12.csv',encoding='euc-kr',index=False)