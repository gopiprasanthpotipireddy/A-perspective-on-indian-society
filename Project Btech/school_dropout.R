school_dropout_2011_12<-read_csv("~/Downloads/Statement_SES_2011-12-DropOut.csv")
View(school_dropout_2011_12)
percentage<-school_dropout_2011_12[4]  #percentage data
year_dropout_1_5<-school_dropout_2011_12[1] #year data
year<-c(1960,1970,1980,1990,1992,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011)
#all categories dropouts
percent_1_5<-as.vector(school_dropout_2011_12$`All Categories - Classes I-V - Total`) #all categories 1-5
percent_1_8<-as.vector(school_dropout_2011_12$`All Categories - Classes I-VIII - Total`)#all categories 1-8
percent_1_10<-as.vector(school_dropout_2011_12$`All Categories - Classes I-X - Total`) #all categories 1-10
plot(year,percent_1_10,type = "l",col = "blue",ylim=c(10,100),xlim=c(1960,2010) ,xlab="year",ylab="percentage",main="all categories droput rates") 
plot(year,percent_1_8,type = "l",col = "red",main="droput rates") 
plot(year,percent_1_5,type = "l",col = "green",main="droput rates") 
lines(year,percent_1_5,type = "h",col = "green",ylim=c(10,100),xlim=c(1960,2010) ,xlab="year",ylab="percentage",main="droput rates") 
lines(year,percent_1_10,col = "blue")
lines(year,percent_1_8,col = "red")
lines(year,percent_1_5,col="green")


#coordinates
coords <- locator()
text(x=coords$x, y=coords$y,label="1-8 dropout rate")
coords <- locator()
text(x=coords$x, y=coords$y,label="1-10 dropout rate")
coords<-locator()
text(x=coords$x, y=coords$y,label="1-5 dropout rate")

par(mfrow=c(3,1))

#GirlEDucation DropoutRates All catogories
girl_percent_1_5<-as.vector(school_dropout_2011_12$`All Categories - Classes I-V - Girls`)
girl_percent_1_8<-as.vector(school_dropout_2011_12$`All Categories - Classes I-VIII - Girls`)
girl_percent_1_10<-as.vector(school_dropout_2011_12$`All Categories - Classes I-X - Girls`)
plot(year,girl_percent_1_10,type = "l",col = "blue",ylim=c(10,100),xlim=c(1960,2010) ,xlab="year",ylab="percentage",main="all categories girl droput rates") 
lines(year,girl_percent_1_8,col = "red")
lines(year,girl_percent_1_10,col = "blue")
lines(year,girl_percent_1_5,col = "green")

lines(year,girl_percent_1_10,type = "h",col = "blue")
lines(year,girl_percent_1_8,type = "h",col = "red")
lines(year,girl_percent_1_5,type = "h",col = "green")


#scheduled caste girl Education

girl_sc_percent_1_5<-as.vector(school_dropout_2011_12$`Scheduled Caste - Classes I-V - Girls`)
girl_sc_percent_1_8<-as.vector(school_dropout_2011_12$`Scheduled Caste - Classes I-VIII - Girls`)
girl_sc_percent_1_10<-as.vector(school_dropout_2011_12$`Scheduled Caste - Classes I-X - Girls`)
plot(year,girl_sc_percent_1_10,type = "l",col = "blue",ylim=c(10,100),xlim=c(1990,2010) ,xlab="year",ylab="percentage",main="scheduledcast girl droput rates") 
lines(year,girl_sc_percent_1_8,col = "red")
lines(year,girl_sc_percent_1_5,col = "green")
lines(year,girl_sc_percent_1_10,col = "blue")
lines(year,girl_sc_percent_1_10,type = "h",col = "blue")
lines(year,girl_sc_percent_1_8,type = "h",col = "red")
lines(year,girl_sc_percent_1_5,type = "h",col = "green")


#scheduled tribe girl Education

girl_st_percent_1_5<-as.vector(school_dropout_2011_12$`Scheduled Tribe - Classes I-V - Girls`)
girl_st_percent_1_8<-as.vector(school_dropout_2011_12$`Scheduled Tribe - Classes I-VIII - Girls`)
girl_st_percent_1_10<-as.vector(school_dropout_2011_12$`Scheduled Tribe - Classes I-X - Girls`)
plot(year,girl_st_percent_1_10,type = "l",col = "blue",ylim=c(10,100),xlim=c(1990,2010) ,xlab="year",ylab="percentage",main="scheduledTribes girl droput rates") 
lines(year,girl_st_percent_1_8,col = "red")
lines(year,girl_st_percent_1_5,col = "green")
lines(year,girl_st_percent_1_10,col = "blue")
lines(year,girl_st_percent_1_10,type = "h",col = "blue")
lines(year,girl_st_percent_1_8,type = "h",col = "red")
lines(year,girl_st_percent_1_5,type = "h",col = "green")

#years where the percentage of dropouts more than 60
#(1-5)
school_dropout_2011_12[(as.numeric(school_dropout_2011_12$`All Categories - Classes I-V - Total`) > 50),1,]
#(1-8)
school_dropout_2011_12[(as.numeric(school_dropout_2011_12$`All Categories - Classes I-VIII - Total`) > 50),1,]
school_dropout_2011_12[(as.numeric(school_dropout_2011_12$`All Categories - Classes I-X - Total`) > 50),1,]

