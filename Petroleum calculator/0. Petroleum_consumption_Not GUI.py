# -*- coding: cp1253 -*-


print ('Heating oil comsuption calculator')
litersAtTheStart=int(input('Liters in the barrel at the first measurement: '))
#We will make an array of measurments for the first time we measure the hour counters
hourCounters1=[]
for i in range (1, 3, 1):
    print ('Hour counter', i)
    counter=int(input('Counter indication (first measurment): '))
    hourCounters1.append(counter)

print ('Indications of hour counters at the 1st measurment: ', hourCounters1)
    
#We will make an array of measurments for the second time we measure the hour counters
hourCounters2=[]
for i in range (1, 3, 1):
    print ('Hour counter', i)
    counter=int(input('Counter indication (2nd measurment): '))
    hourCounters2.append(counter)

print ('Indications of hour counters at the 2nd measurment: ', hourCounters2)


hours2=0
workingHours=[]
# We will make an array that shows how many hours each appartement counter worked
for i in range (0, 2, 1):
    hours2=hourCounters2[i]-hourCounters1[i]
    workingHours.append(hours2)
 
print ('The working hours of each counter are: ', workingHours)

Liters2=int(input('Liters in the barrel at the second measurement: '))

totalLitersConsumption=0
totalLitersConsumption=litersAtTheStart-Liters2
print ('The consumption in liters at the second measurement is: ', totalLitersConsumption)

percentageOfWorkingHours1=0
percentageOfWorkingHours2=0
TotalWorkingHours=0
#Estimation of the total working hours of all counters
for i in range (0, 2, 1):   
    TotalWorkingHours=TotalWorkingHours+workingHours[i]
print ('The total working hours of all the countres are ', TotalWorkingHours)

#Express as percentage the working hours of each apartement relative to the total working hours of all counters     
percentageOfWorkingHours1=(workingHours[0]/TotalWorkingHours)
percentageOfWorkingHours2=(workingHours[1]/TotalWorkingHours)

consumptionInLiters1=0
consumptionInLiters2=0
#Consumption in liters expressed per apartement
consumptionInLiters1=percentageOfWorkingHours1*totalLitersConsumption
consumptionInLiters2=percentageOfWorkingHours2*totalLitersConsumption
print ('The consumption of the first apartement in liters is ', consumptionInLiters1, 'liters')
print ('The consumption of the first apartement in liters is ',consumptionInLiters2, 'liters')
