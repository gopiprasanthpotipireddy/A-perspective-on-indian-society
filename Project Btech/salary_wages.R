wage<-read.table(file.choose(),header = TRUE); # reading file 
attach(WageData);                           #attaching to rstudio
WS5<-as.factor(WS5);           
wage_source_count<-table(WS5);   #source categories
wage_source_count<-as.factor(WS5);  
wage_source_count
class((WS5));
WageData$WS5
WS5<-WageData$WS5;
wage_source_count<-table(WS5) 
wage_source_percent<-(wage_source_count/64289)*100;     #perecnteage contribution of variuos sources
pie(wage_source_percent,main = "WAGES",xlab = "SOURCE",ylab = "PERCENTAGE",col ="orange",las =2); #bar graph of sources
state_cat<-table(agri_industry$STATEID);
pie(state_cat,main = "state/agri background",col = rainbow(length(state_cat)),las = 2)                   #state wise projection
summary(agri_industry)               #summary of agriculture data
per_day<-WageData[WS9==1,]           #to know per day wages vs agriculture
View(per_day)
per_day_extract<-per_day[9:12]  #only use ful columns
View(per_day_extract)
#works more than 200 days/year and more than 12 hours/day
count_agri_labour<-nrow( per_day_extract[per_day_extract$WS7 >200 & per_day_extract$WS8 >12,])
#work hours total 
work_hours_plot<-table(per_day_extract$WS7 * per_day_extract$WS8) 
#plot for more work hours vs number of people
barplot(work_hours_plot,main="workdays/year",ylab="people",xlab="hours",horiz ="FALSE",col = "blue")
pie(table(per_day_extract[per_day_extract$WS7 ,3]),xlab = "hours",col = rainbow(length(work_hours_plot))) #morethan 250 days

#deleting small percentages from wages
t<-table(WS5)
d<-data.frame(t)
d$Perc <- d$Freq / sum(d$Freq) * 100
d<-d[d$Perc > 1.5,c(1,3)]
pie(c(d$Perc),labels = d$WS5,main = "wage and salaries dependency",col = c(3,8))

#new working hours plot
new_work_hours<-as.data.frame(work_hours_plot)
View(new_work_hours)
new_work_hours$Perc <- new_work_hours$Freq / sum((new_work_hours$Freq)) *100
work_table<-new_work_hours[new_work_hours$Perc > 1.5,c(1,3)]
pie(c(work_table$Perc),labels = work_table$Var1,main = "work hours/ year", col = c(3,8))

#new working days plot
work_days<-as.data.frame(table(WS7))
View(work_days)
work_days$Perc <- work_days$Freq / sum((work_days$Freq)) *100
work_days_table<-work_days[work_days$Perc > 2,]
pie(c(work_days_table$Perc),labels = work_days_table$WS7,main = "work days/ year", col = c(3,8))

