attach(birth_data)
child_death<-birth_data[as.numeric(BH7) == 3 & BH8A == 0,] #child less than 0 years
tem = table(child_death[child_death$BH5B != -1,13,])
#yearwise child deaths
yd<-barplot(sort(tem/sum(tem)*100),col = "palegreen",xlab = "year",ylab = "percentage",main = "childdeath(<1)/year")

#death at age
age_death<-birth_data[as.numeric(birth_data$BH7) == 3 & birth_data$BH8A != -1,]
barplot((table(age_death$BH8A)),main = "death/age",xlab = "age",ylab = "count",col = "palegreen")

#child death statewise

h<-barplot(table(child_death$STATEID),las = 2,main = "child death/state", ylab = "count", col = "orange")
text(h, y = as.numeric(h), label = as.numeric(h), pos = 3, cex = 0.8, col = "red")
