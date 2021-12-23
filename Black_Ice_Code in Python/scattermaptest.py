import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

df = pd.read_csv("Data/2019.csv", encoding='euc-kr')

# fm.get_fontconfig_fonts()
# font_location = 'c:/Windows/Fonts/malgun.ttf'
# font_name = fm.FontProperties(fname=font_location).get_name()
# plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False
f_path = 'c:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname=f_path).get_name()
plt.rc('font', family=font_name)

correlation_matrix = df.corr().round(2)
#sns.set(rc={'figure.figsize':(40,40)})
plt.figure(figsize=(40,20))
plt.xticks(rotation = -90, size=7)
heat_road = sns.heatmap(data=correlation_matrix, annot=True) # 상관계수 분석
heat_road
plt.show()