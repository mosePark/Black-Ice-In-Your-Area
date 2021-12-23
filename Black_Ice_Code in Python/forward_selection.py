import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

road = pd.read_csv('Data/road_stat_bin_bina_bridge.csv',encoding='euc-kr')
df = road[['e_Xvalue','e_Yvalue','czlen',
          'e_elevation','lane','pave','surface','traffic',
          'tunnel','ice_leak','grooving',
          'VMS_time_r','AWS_weather','기상','안개계속시간(hr)','합계일조시간(hr)','평균지면온도(°C)',
          '평균기온(°C)','최저기온(°C)','최저기온시각(hhmi)','최고기온(°C)','최고기온시각(hhmi)',
          '최대풍속(m/s)','평균풍속(m/s)','강수계속시간(hr)','일강수량(mm)',
          '일최심적설(cm)','최대풍속풍향(16방위)','평균이슬점온도(°C)','평균상대습도(%)',"VMS_keyword",'acc'
          ]]
# corr_matrix = df.corr() #피어슨상관관계
# print(corr_matrix['acc'].sort_values(ascending=True))
# for i in X:
#     print(i, stats.pointbiserialr(df[i],road['acc']))
#p-value
variables = df.columns[:-1].tolist()  ## 설명 변수 리스트

y = df['acc']  ## 반응 변수
selected_variables = []  ## 선택된 변수들
sl_enter = 0.05

sv_per_step = []  ## 각 스텝별로 선택된 변수들
adjusted_r_squared = []  ## 각 스텝별 수정된 결정계수
steps = []  ## 스텝
step = 0
while len(variables) > 0:
    remainder = list(set(variables) - set(selected_variables))
    pval = pd.Series(index=remainder)  ## 변수의 p-value
    ## 기존에 포함된 변수와 새로운 변수 하나씩 돌아가면서
    ## 선형 모형을 적합한다.
    for col in remainder:
        X = df[selected_variables + [col]]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        pval[col] = model.pvalues[col]

    min_pval = pval.min()
    if min_pval < sl_enter:  ## 최소 p-value 값이 기준 값보다 작으면 포함
        selected_variables.append(pval.idxmin())

        step += 1
        steps.append(step)
        adj_r_squared = sm.OLS(y, sm.add_constant(df[selected_variables])).fit().rsquared_adj
        adjusted_r_squared.append(adj_r_squared)
        sv_per_step.append(selected_variables.copy())
    else:
        break

print('전진 선택법 :',selected_variables)

variables = df.columns[:-1].tolist()  ## 설명 변수 리스트

y = df['acc']  ## 반응 변수
selected_variables = variables  ## 초기에는 모든 변수가 선택된 상태
sl_remove = 0.05

sv_per_step = []  ## 각 스텝별로 선택된 변수들
adjusted_r_squared = []  ## 각 스텝별 수정된 결정계수
steps = []  ## 스텝
step = 0
while len(selected_variables) > 0:
    X = sm.add_constant(df[selected_variables])
    p_vals = sm.OLS(y, X).fit().pvalues[1:]  ## 절편항의 p-value는 뺀다
    max_pval = p_vals.max()  ## 최대 p-value
    if max_pval >= sl_remove:  ## 최대 p-value값이 기준값보다 크거나 같으면 제외
        remove_variable = p_vals.idxmax()
        selected_variables.remove(remove_variable)

        step += 1
        steps.append(step)
        adj_r_squared = sm.OLS(y, sm.add_constant(df[selected_variables])).fit().rsquared_adj
        adjusted_r_squared.append(adj_r_squared)
        sv_per_step.append(selected_variables.copy())
    else:
        break

print('후진 소거법 :',selected_variables)

variables = df.columns[:-1].tolist()  ## 설명 변수 리스트

y = df['acc']  ## 반응 변수
selected_variables = []  ## 선택된 변수들
sl_enter = 0.05
sl_remove = 0.05

sv_per_step = []  ## 각 스텝별로 선택된 변수들
adjusted_r_squared = []  ## 각 스텝별 수정된 결정계수
steps = []  ## 스텝
step = 0
while len(variables) > 0:
    remainder = list(set(variables) - set(selected_variables))
    pval = pd.Series(index=remainder)  ## 변수의 p-value
    ## 기존에 포함된 변수와 새로운 변수 하나씩 돌아가면서
    ## 선형 모형을 적합한다.
    for col in remainder:
        X = df[selected_variables + [col]]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        pval[col] = model.pvalues[col]

    min_pval = pval.min()
    if min_pval < sl_enter:  ## 최소 p-value 값이 기준 값보다 작으면 포함
        selected_variables.append(pval.idxmin())
        ## 선택된 변수들에대해서
        ## 어떤 변수를 제거할지 고른다.
        while len(selected_variables) > 0:
            selected_X = df[selected_variables]
            selected_X = sm.add_constant(selected_X)
            selected_pval = sm.OLS(y, selected_X).fit().pvalues[1:]  ## 절편항의 p-value는 뺀다
            max_pval = selected_pval.max()
            if max_pval >= sl_remove:  ## 최대 p-value값이 기준값보다 크거나 같으면 제외
                remove_variable = selected_pval.idxmax()
                selected_variables.remove(remove_variable)
            else:
                break

        step += 1
        steps.append(step)
        adj_r_squared = sm.OLS(y, sm.add_constant(df[selected_variables])).fit().rsquared_adj
        adjusted_r_squared.append(adj_r_squared)
        sv_per_step.append(selected_variables.copy())
    else:
        break

print('단계별 선택법 :',selected_variables)