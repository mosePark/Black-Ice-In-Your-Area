install.packages("rpart")
library(tidyverse)
library(knitr)
library(gridExtra)
library(ggplot2)
library(GGally)
library(grid)
library(kableExtra)

library(tree)
library(rpart)

# 2019년 1월1일 콘존에 대한 데이터 DT

setwd("C:/Users/Administrator/Desktop/data1")

df <- read_csv("road_2019.csv",locale=locale('ko',encoding='euc-kr'))

df <- subset(df, df$date==20190101)

df <- df %>% 
  select(date, pave, surface,	classification,	bridge_lane,	bridge_pave,	bridge_surface,	bridge,	tunnel,	grooving,	ice_leak,	traffic,	VMS_keyword,
         Avg_temp	, Mini_temp, Mini_temp_time, Max_temp, Max_temp_time, precipitation_duration_time, day_precipitation, Max_windspeed	, Wind_direction, Avg_windspeed, Avg_dewpoint_temp,
         Avg_relative_humidity, Sunlight_time, Deepest_snow, Avg_ground_temp, weather, Fog_time)

df <- df %>%
  mutate(ice_leak = ifelse(ice_leak==1, "YES", "NO"))


glimpse(df)

# tree 패키지 안됌 ...ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
tree.df = tree(VMS_keyword~.-date, df)
summary(tree.df)

plot(tree.df)
text(tree.df,pretty=0,cex=0.7)

# rpart 패키지
tree.df <- rpart(ice_leak~., data = df, method="class")
summary(tree.df)
x11()
plot(tree.df)
text(tree.df,pretty=0,cex=0.7) # 시간대 변수설정 다시 범주화해서 생각해보자.

tree.df # 나무모형 텍스트화

### Test error estimation ###
set.seed(123)
train = sample(1:nrow(df), 500) # train set 0.5만큼
df.test = df[-train,]
VMS_keyword.test = df$VMS_keyword[-train]
tree.df = rpart(VMS_keyword~.-date, data=df, method="class", subset=train)
tree.pred = predict(tree.df, df.test, type="class")
table(tree.pred, VMS_keyword.test)


