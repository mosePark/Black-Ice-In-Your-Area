import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.getcwd()
os.chdir('C:\\Users\\Administrator\\Desktop\\data')

df = pd.read_csv("road_2019.csv", encoding='euc-kr')

correlation_matrix = df.corr().round(2)

sns.set(rc={'figure.figsize':(20,20)})
sns.heatmap(data=correlation_matrix, annot=True) # 상관계수 분석
plt.show()
plt.close()

