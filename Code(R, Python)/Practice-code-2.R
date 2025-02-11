library(tidyverse)
library(ggplot2)
library(GGally)
library(grid)
library(gridExtra)
library(knitr)
################################
setwd("C:/Users/Administrator/Desktop/data")
df <- read_csv("road_2019.csv",locale=locale('ko',encoding='euc-kr'))
################################
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

df <- df %>% 
  mutate(Risk=ifelse(df$Risk_dummy == 1, "Risk", "Not Risk"))
################################

library(corrplot)
df_numeric <- df[,c(25, 29:43, 45, 46)] # 데이터에서 수치형 변수만 추출
x11()
correlations <- cor(df_numeric)
corrplot(correlations, method="circle")
################################
kable(table(df$pave, df$surface))

table(df$surface, df$Risk)

df %>%
  ggplot(aes(pave, fill=Risk)) +
  geom_density(alpha=.5)

################################ 

table(df$classification, df$Risk)
503/(1611+503)
157/(1655+157)
25055/(122019+25055)
VMS_keyword_table <- df %>%
  group_by(VMS_keyword) %>% 
  summarize(freq=n()) %>% 
  mutate(prop=freq/sum(freq))

VMS_keyword_table


df <- df %>% 
  mutate(Risk=ifelse(df$Risk_dummy == 1, "Risk", "Not Risk"))

table(df$Risk)

Risk_table <- df %>%
  group_by(Risk) %>% 
  summarize(freq=n()) %>% 
  mutate(prop=freq/sum(freq))

Risk_table





ggplot(df, aes(x=Avg_dewpoint_temp, y=Risk)) +
  geom_point(size = 2.5) +
  ylab("Risk of road icing") +
  xlab("average of dewpoint temperature")






# Model 1
glm.fit1=glm(Risk~Avg_dewpoint_temp,data=df,family=binomial)
summary(glm.fit1)

# Model 2
glm.fit2=glm(Risk~Avg_dewpoint_temp+Avg_relative_humidity, data=df, family=binomial)
summary(glm.fit2)

# Model 3
glm.fit3=glm(Risk~Avg_dewpoint_temp+Avg_relative_humidity+pave, data=df, family=binomial)
summary(glm.fit3)

# Model 4
glm.fit4=glm(Risk~Avg_dewpoint_temp+Avg_relative_humidity+pave+, data=df, family=binomial)
summary(glm.fit4)


glm = glm(Risk~., data=df, family=binomial)
summary(glm)

model12 = glm(Risk_dummy ~ Avg_dewpoint_temp*pave+surface+classification+e_elevation+Avg_windspeed
              +Sunlight_time+Fog_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+surface+pave:surface+classification+e_elevation+Avg_windspeed
              +Sunlight_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

table(df$czId, df$Risk)


df$Risk

df <- df %>%
  mutate(phat=(risk+.5)/(Notrisk+1),
         elogit=log(phat/(1-phat)))

## Plots

logblack <- ggplot(rrHale.df, aes(x=pctBlack, y=elogit))+
  geom_point(shape=1) +
  geom_smooth(method=lm,
              se=FALSE) +
  labs(x="percent black",
       y="empirical logits",
       title="Hale Empirical logits by percent black") +
  4
geom_text(aes(label=Greensboro), nudge_x = 7.5, nudge_y = -.5)
grid.arrange(logdis, logblack ,ncol=1)

elgit <- log(sum(df$Risk_dummy)+.5/(1-sum(df$Risk_dummy))+1)

logdis <- ggplot(df, aes(x=Avg_dewpoint_temp, y=elgit))+
  geom_point(shape=1) + # Use hollow circles
  geom_smooth(method=lm, # Add linear regression line
              se=FALSE) + # Don't add shaded confidence region
  labs(x="distance",
       y="empirical logits",
       title="Hale Empirical logits by distance")








ggplot(df1, aes(x = Avg_dewpoint_temp, y = Risk)) +
  geom_point(shape=1)

###########################################################
rrHale.df <- rrHale.df %>%
  mutate(phat=(YesVotes+.5)/(NumVotes+1),
         elogit=log(phat/(1-phat)),
         Greensboro= ifelse(rrHale.df$community=="Greensboro", 
                            , →"Greensboro", NA))
## Plots
logdis <- ggplot(rrHale.df, aes(x=distance, y=elogit))+
  geom_point(shape=1) + # Use hollow circles
  geom_smooth(method=lm, # Add linear regression line
              se=FALSE) + # Don't add shaded confidence region
  labs(x="distance",
       y="empirical logits",
       title="Hale Empirical logits by distance")
logblack <- ggplot(rrHale.df, aes(x=pctBlack, y=elogit))+
  geom_point(shape=1) +
  geom_smooth(method=lm,
              se=FALSE) +
  labs(x="percent black",
       y="empirical logits",
       title="Hale Empirical logits by percent black") +
  4
geom_text(aes(label=Greensboro), nudge_x = 7.5, nudge_y = -.5)
grid.arrange(logdis, logblack ,ncol=1)





# 수치형 예측변수 선택하기

df1 <- subset(df, df$date==20190101)

df1_numeric <- df1[,c(25, 29:43, 45, 46)] # 수치형변수만 불러와서 데이터프레임
colnames(df1_numeric)
df1_numeric <- df1_numeric[,-c(3, 5, 13)] # 다중공선성 영향주는 변수 제거

predictors <- colnames(df1_numeric)

# 로짓 바인딩 및 데이터 정리
model <- glm(Risk_dummy ~., data = df1_numeric, family = binomial)

probabilities <- predict(model, type = "response")


df1_numeric <- df1_numeric %>%
  mutate(logit = log(probabilities/(1-probabilities))) %>%
  gather(key = "predictors", value = "predictor.value", -logit)

ggplot(df1_numeric, aes(logit, predictor.value))+
  geom_point(size = 0.5, alpha = 0.5) +
  geom_smooth(method = "loess") + 
  theme_bw() + 
  facet_wrap(~predictors, scales = "free_y")

summary(df$Sunlight_time)

model0 = glm(Risk_dummy ~ Avg_dewpoint_temp, family=binomial, data=df)
summary(model0)


model1 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave, family=binomial, data=df)
summary(model1)

model2 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification, family=binomial, data=df)
summary(model2)

model3 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface, family=binomial, data=df)
summary(model3)

model4 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+traffic, family=binomial, data=df)
summary(model4)

model5 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+traffic, family=binomial, data=df)
summary(model4)

model6 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+e_elevation, family=binomial, data=df)
summary(model6)

model7 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+e_elevation+, family=binomial, data=df)
summary(model7)

model8 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+, family=binomial, data=df)
summary(model8)

model9 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+, family=binomial, data=df)
summary(model9)

summary(glm(Risk_dummy ~ ., family=binomial, data=df))

df$Sunlight_time

model <- c("Model0", "Model1", "Model2", "Model3", "Model4",
           "Model5","Model6","Model7","Model8","Model9","Model10",
           "Model11","Model12")

AIC <- c(134483, 134432, 134216, 133618, 133620,
         133555, 133279, 131042, 118576, 118467,
         117554, 115011, 114963) 

Result <- data.frame(model, AIC) ; Result



table(df$Risk, df$pave)
plot(model, AIC)


model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+surface+classification+e_elevation+Avg_windspeed
              +Sunlight_time+Fog_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

table(df$czId, df$Risk)



table(df$Risk, df$pave)

10716/(10716+56328)
14999/(14999+68957)

``

table(df$Risk, df$VMS_keyword)

table(df$routeName, df$Risk)
#############################################################################
westsea <- subset(df, df$routeName=="서해안선")
westsea_Risk <- subset(westsea, westsea$VMS_keyword=="결빙"&westsea$VMS_keyword=="노면미끄럼"&westsea$VMS_keyword=="노면습기" )

table(westsea$czId[westsea$VMS_keyword=="결빙"]) # 서해안선 결빙 콘존
table(westsea$czId[westsea$VMS_keyword=="노면미끄럼"]) #서해안선 노면미끄럼 콘존
table(westsea$czId[westsea$VMS_keyword=="노면습기"]) # 노면습기

table(westsea$VMS_keyword)


table(westsea_Risk$czId)

westsea

# 성공/실패, 위험/위험x

table(df$surface, df$Risk)



model = glm(Risk_dummy ~ surface, family=binomial, data=df)
summary(model)


model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+e_elevation+Avg_windspeed
              +Sunlight_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)
exp(model12$coefficients)
exp(model$coefficients)


model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+e_elevation+Avg_windspeed
              +Sunlight_time+Fog_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

predict(model12, newdata=)

Model <- c("Model0","Model1","Model2","Model3","Model4","Model5","Model6","Model7","Model8","Model9","Model10","Model11","Model12")

AIC <- c(134483, 134432, 134216, 133618, 133620, 133555, 133279, 131042, 118576, 118467, 117554, 115011, 114963)

result <- data.frame(Model, AIC)

kable(t(result))

plot(AIC, xlab=c("13개의 회귀모형"), type="o")

model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+s_elevation+e_elevation
              +Sunlight_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

exp(model12$coefficients)

exp(model12$coefficients)

exp(0.062068)

table(df$pave, df$Risk)

10716/(56328+10716)
14999/(68957+14999)

table(df$surface)

mod <- glm(Risk_dummy ~ Sunlight_time, family=binomial, data=df)
summary(mod)

summary(df$Avg_windspeed)

abc <- as.data.frame(table(df$Risk, df$Avg_windspeed))

result <- c()
for (i in 1:nrow(abc)){
  result[i] <- abc$Freq[i+1]/(abc$Freq[i]+abc$Freq[i+1])  
}

abc$prop <- result[1:nrow(abc) %% 2 == 1] # 각 풍속별 확률

abc

prop.plot(df$Avg_windspeed)

summary(df$Avg_dewpoint_temp)

summary(df$Sunlight_time)

summary(df$day_precipitation)

summary(df$precipitation_duration_time)

mod <- glm(Risk_dummy~surface, data=df, family=binomial)
summary(mod)



table(df$surface)


score <- as.numeric(df$score)

summary(as.numeric(df$score))

sum(is.na(score))

head(score - 1)

head(score)


normal <- (score - min(score)) / (max(score) - min(score))

df$normal <- normal

summary(df$normal)

dat <- subset(df$date, df$normal > 0.9 )

cz <- subset(df$czId, df$normal > 0.9 )

data.frame(dat, cz)

table(df$Risk_dummy)

summary(normal)

table(df$VMS_keyword)
2741/151000


table(df$VMS_keyword=="결빙", df$Avg_dewpoint_temp)

table(df$surface, df$VMS_keyword=="결빙") 

20000/151
2/15
table(df$precipitation_duration_time, df$VMS_keyword)





exp(0.123123412)


model12 = glm(Risk_dummy ~ Avg_dewpoint_temp+pave+classification+surface+s_elevation+e_elevation+Avg_windspeed
              +Sunlight_time+day_precipitation+precipitation_duration_time+grooving, family=binomial, data=df)
summary(model12)

exp(model12$coefficients)
