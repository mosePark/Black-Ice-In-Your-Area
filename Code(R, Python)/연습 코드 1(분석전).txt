# EDA

library(nnet)
# 패키지 불러오기
library(tidyverse)
library(ggplot2)
library(GGally)
library(grid)
library(gridExtra)
library(knitr)
# library(kableExtra)

# 데이터 불러오기
setwd("C:/Users/Administrator/Desktop/data")

df <- read_csv("road_2019.csv",locale=locale('ko',encoding='euc-kr')) # 데이터 구조 파악
df %>% head(5)
df %>% tail(5)

str(df)
# 범주형변수 factor 처리
df$VMS_keyword <- as.factor(df$VMS_keyword)
df$pave <- as.factor(df$pave)
df$surface <- as.factor(df$surface)
df$bridge_surface <- as.factor(df$bridge_surface)
df$classification <- as.factor(df$classification)
df$bridge_lane <- as.factor(df$bridge_lane)
df$bridge_pave <- as.factor(df$bridge_pave)
df$bridge <- as.factor(df$bridge)
df$tunnel <- as.factor(df$tunnel)
df$grooving <- as.factor(df$grooving)
df$ice_leak <- as.factor(df$ice_leak)
df$weather <- as.factor(df$weather)

# 결측값 확인
sum(is.na(df)) # 데이터내에서 결측값 수는?

# 산점도행렬

df <- df %>%
  mutate(cz_length = abs(df$czend - df$czstart))

summary(df$cz_length)

min(df$cz_length)

df$czId[df$czstart == df$czend]

# 수치형변수

#attach(df)
#df[traffic, Mini_temp_time,Mini_temp_time, Max_temp, Max_temp_time, precipitation_duration_time, day_precipitation,
#   Max_windspeed, Wind_direction, Avg_windspeed, Avg_dewpoint_temp, Avg_relative_humidity, Sunlight_time,
#   Deepest_snow, Avg_ground_temp, weather,Fog_time, cz_length]



df_numeric <- df[,c(25, 29:43, 45, 46)] # 데이터에서 수치형 변수만 추출
options(digits=3)
df_numeric > 0.3

scattermatrix <- cor(df_numeric) > 0.3
kable(scattermatrix, booktabs=T, caption = "수치형변수사이의 상관계수")

df_numeric <- df[,c(25, 29:43, 45, 46)]
x11()
pairs(df_numeric)

# 중요한 공변량에대한 히스토그램 (수치형변수), 이슬점, 습도 파악

dewpoint_hist <- ggplot(data = df, aes(x = Avg_dewpoint_temp)) + 
  geom_histogram(binwidth = , fill = "white",color = "black") + 
  xlab("Average of dew point temperature(℃)") + ylab("Frequency") + labs(title="(a)")

humidity_hist <- ggplot(data = df, aes(x = Avg_relative_humidity)) + 
  geom_histogram(binwidth = 3, fill = "white",color = "black") + 
  xlab("Average of relative humidty") + ylab("Frequency") + labs(title="(b)")

grid.arrange(dewpoint_hist, humidity_hist, ncol = 2)

sample <- sample(df$Avg_relative_humidity, 5000)
shapiro.test(sample)
shapiro.test(sample)


hist(df$traffic)
hist(df$Avg_dewpoint_temp)



# 범주형변수

pave_table <- df %>% 
                group_by(pave) %>% 
                summarize(freq=n()) %>% 
                mutate(prop=freq/sum(freq))

surface_table <- df %>% 
                  group_by(surface) %>% 
                  summarize(freq=n()) %>% 
                  mutate(prop=freq/sum(freq))

class_table <- df %>%
                group_by(classification) %>% 
                summarize(freq=n()) %>% 
                mutate(prop=freq/sum(freq))

grid.arrange(pave_table, surface_table, class_table, ncol=3)

tableGrob(class_table)
VMS_keyword_talbe <- df %>% 
                      group_by(VMS_keyword)%>% 
                      summarize(freq=n())%>% 
                      mutate(prop=freq/sum(freq))

ggplot(df, aes(x = traffic, y = VMS_keyword, colour = ice_leak)) +
  geom_point()








