library(readr)
child_marriage <- read_csv("~/Downloads/DDWC_000004-2001.csv") #reading data
View(child_marriage)
attach(child_marriage)
percent_female_marriage<-(india_marriage$`Number of ever Married Persons - Females`/273405276)*100
plot(as.factor(india_marriage$`Age at Marriage`),percent_female_marriage,col = rainbow(length(percent_female_marriage)),xlab="age-group",ylab="percentage",main="female_marriages")

#india_total female marriages
india_total<-india_marriages[india_marriage$`Total/ Rural/ Urban` == "Total",]
plot(as.factor(india_total$`Age at Marriage`),((india_total$`Number of ever Married Persons - Females`/273405276)*100),main="female_marriage/total")

#india_urban female marriages
india_urban<-india_marriage[india_marriage$`Total/ Rural/ Urban`== "Urban",]
plot(as.factor(india_total$`Age at Marriage`),(india_urban$`Number of ever Married Persons - Females`/273405276)*100,main="female_marriage/urban")

#india_rural female marriages

india_rural<-india_marriage[india_marriage$`Total/ Rural/ Urban`== "Rural",]
plot(as.factor(india_total$`Age at Marriage`),(india_rural$`Number of ever Married Persons - Females`/273405276)*100,main="female_marriage/rural")

par(mfrow=c(3,1)) #combined plots





#statewise less than 10 male
less_10_male<-child_marriage[`Age at Marriage`=="Less than 10",c(2,5,6,8),]
attach(less_10_male)
levels(`Total/ Rural/ Urban`)
levels(as.factor(`State Code`))
data <-`Number of ever Married Persons - Males`
data=matrix(data,ncol=3,byrow=T)
colnames(data)=c("Total","Rural","Urban")
rownames(data)=levels(as.factor(`State Code`))
data<-data[-1,] #excluding india
prop = prop.table(data,margin=2) #calculatign percentage for each column(total,rural,urban)



#The default margin is: c(5, 4, 4, 2) + 0.1 .
#As a result, we have exploded the right-hand side of the figure to hold legend.

#xpd=TRUE forces all plotting to be clipped to the figure region
par(mar=c(6.9, 3, 3, 7.1), xpd=TRUE)
par(mar =c(1,0,0,1))
barplot(prop, main="male_lessthan_10",col=heat.colors(length(rownames(prop))), width=2, beside=TRUE)
legend("bottom",inset=c(5.0,-0.9), fill=heat.colors(length(rownames(prop))), legend=rownames(data),ncol = 8)
barplot(prop, main="male_lessthan_10",col=heat.colors(length(rownames(prop))), beside=TRUE)



#female lessthan 10 statewise
less_10_female<-child_marriage[`Age at Marriage`=="Less than 10",c(2,5,6,9),]
attach(less_10_female)
levels(`Total/ Rural/ Urban`)
levels(as.factor(`State Code`))
data_female <-`Number of ever Married Persons - Females`
data_female=matrix(data_female,ncol=3,byrow=T)
colnames(data_female)=c("Total","Rural","Urban")
rownames(data_female)=levels(as.factor(`State Code`))
data_female<-data_female[-1,] #excluding india
prop_female = prop.table(data_female,margin=2) #calculatign percentage for each column(total,rural,urban)

par(mar=c(6.9, 3, 3, 7.1), xpd=TRUE)
barplot(prop_female, main="female_lessthan_10",col=heat.colors(length(rownames(prop_female))), width=2, beside=TRUE)
legend("bottom",inset=c(5.0,-0.9), fill=heat.colors(length(rownames(prop_female))), legend=rownames(data_female),ncol = 8)
barplot(prop, main="male_lessthan_10",col=heat.colors(length(rownames(prop_female))), beside=TRUE)


temp<-less_10_female[less_10_female$`Total/ Rural/ Urban` == "Rural",4,]
temp1<-less_10_female[less_10_female$`Total/ Rural/ Urban` == "Urban",4,]
par(mfrow=c(2,1)) #combined plots

#total male_10
barplot(as.numeric(temp$`Number of ever Married Persons - Females`) ,xlab ="state code" ,ylab = "number" ,names.arg = c(1:36),col = rainbow(length(36)))
barplot(as.numeric(temp$`Number of ever Married Persons - Females`)  ,xlab ="state code" ,ylab = "number",main = "female_10/rural", names.arg = c(1:36),col = "blue")
barplot(as.numeric(temp1$`Number of ever Married Persons - Females`)  ,xlab ="state code" ,ylab = "number",main = "female_10/urban", names.arg = c(1:36),col = "orange")
