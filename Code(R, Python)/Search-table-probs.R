
abc <- as.data.frame(table(df$Risk, df$Avg_windspeed))

result <- c()
for (i in 1:nrow(abc)){
  result[i] <- abc$Freq[i+1]/(abc$Freq[i]+abc$Freq[i+1])  
}

abc$prop <- result[1:nrow(abc) %% 2 == 1] # 각 풍속별 확률

abc
