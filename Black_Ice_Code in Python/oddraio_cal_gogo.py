import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm

road = pd.read_csv('Data/traffic_road.csv',encoding='euc-kr')
data = pd.read_csv('Data/speed/2016_2019.csv',encoding='euc-kr')
road1 = pd.merge(left=road, right=data, how='left', on=['date','czId'], sort=False)
road1.to_csv('Data/traffic_road_usethis.csv',encoding='euc-kr')
print(road1)