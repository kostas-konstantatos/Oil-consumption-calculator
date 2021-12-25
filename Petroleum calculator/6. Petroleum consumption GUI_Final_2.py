from tkinter import *


def consumption():
    """#Not needed
    oilConsumption.configure(state=NORMAL)
    counterConsumption1.configure(state=NORMAL)
    counterConsumption2.configure(state=NORMAL)
    counterConsumption3.configure(state=NORMAL)
    counterConsumption4.configure(state=NORMAL)
    counterConsumption5.configure(state=NORMAL)
    moneyApart1.configure(state=NORMAL)
    moneyApart2.configure(state=NORMAL)
    moneyApart3.configure(state=NORMAL)
    moneyApart4.configure(state=NORMAL)
    moneyApart5.configure(state=NORMAL)
    firstMeasurment.configure(state=NORMAL)
    totalMoney.configure(state=NORMAL)
    """
    #Starts with zero
    oilConsumption.delete(0, 'end')
    counterConsumption1.delete(0, 'end')
    counterConsumption2.delete(0, 'end')
    counterConsumption3.delete(0, 'end')
    counterConsumption4.delete(0, 'end')
    counterConsumption5.delete(0, 'end')
    #test
    #caloriesPercent1.delete(0, 'end')
    #caloriesPercent2.delete(0, 'end')
    #caloriesPercent3.delete(0, 'end')
    #caloriesPercent4.delete(0, 'end')
    #caloriesPercent5.delete(0, 'end')
    #test
    #weightedHours1.delete(0, 'end')
    #weightedHours2.delete(0, 'end')
    #weightedHours3.delete(0, 'end')
    #weightedHours4.delete(0, 'end')
    #weightedHours5.delete(0, 'end')

    #Sum of residual liters and new liters
    totalLiters=float(residualOil.get())+float(litersNow.get())
    #Insert into the appropriate cell the consumption in euros per apartment
    firstMeasurment.insert(0, totalLiters)
    #Disable cell after calculation
    #firstMeasurment.configure(state=DISABLED)
    
    #Performs the subtraction between 2nd and 1st measurment
    oil=float(totalLiters)-float(secondMeasurment.get())
    count1=float(secondMeasurment1.get())-float(firstMeasurment1.get())
    count2=float(secondMeasurment2.get())-float(firstMeasurment2.get())
    count3=float(secondMeasurment3.get())-float(firstMeasurment3.get())
    count4=float(secondMeasurment4.get())-float(firstMeasurment4.get())
    count5=float(secondMeasurment5.get())-float(firstMeasurment5.get())
    #Insert into the appropriate cell the deference of counters and oil consumption
    oilConsumption.insert(0, oil)
    counterConsumption1.insert(0, count1)
    counterConsumption2.insert(0, count2)
    counterConsumption3.insert(0, count3)
    counterConsumption4.insert(0, count4)
    counterConsumption5.insert(0, count5)
    
    #When the calculation occurs the cell closes
    #oilConsumption.configure(state=DISABLED)
    #counterConsumption1.configure(state=DISABLED)
    #counterConsumption2.configure(state=DISABLED)
    #counterConsumption3.configure(state=DISABLED)
    #counterConsumption4.configure(state=DISABLED)
    #counterConsumption5.configure(state=DISABLED)
    
    #Sum of total calories of all apartments
    totalCalories=float(heatingCalories1.get())+float(heatingCalories2.get())+float(heatingCalories3.get())+float(heatingCalories4.get())+float(heatingCalories5.get())
    #Percentage of calories per apartment relative to total calories
    percent1=float(heatingCalories1.get())/totalCalories
    percent2=float(heatingCalories2.get())/totalCalories
    percent3=float(heatingCalories3.get())/totalCalories
    percent4=float(heatingCalories4.get())/totalCalories
    percent5=float(heatingCalories5.get())/totalCalories                                                                                                              
    #Test_Insert into the appropriate cell the calories of each apartment in percentage relative to the total calories(testing code)
    #caloriesPercent1.insert(0, percent1)
    #caloriesPercent2.insert(0, percent2)
    #caloriesPercent3.insert(0, percent3)
    #caloriesPercent4.insert(0, percent4)
    #caloriesPercent5.insert(0, percent5)                                                                                                              

    #Calories (%) per appartment * hours per apartment (weighted hours)
    wHours1=count1*percent1
    wHours2=count2*percent2
    wHours3=count3*percent3
    wHours4=count4*percent4
    wHours5=count5*percent5                                                                                                              
    #Test_Insert into the appropriate cell the weighted hours(testing code)
    #weightedHours1.insert(0, wHours1)
    #weightedHours2.insert(0, wHours2)
    #weightedHours3.insert(0, wHours3)
    #weightedHours4.insert(0, wHours4)
    #weightedHours5.insert(0, wHours5)

    #Total weighted hours
    totalWeightedHours=wHours1+wHours2+wHours3+wHours4+wHours5
    #Weighted hours of each apartment as percentage of the total weighted hours of all apartments
    percentWHours1=wHours1/totalWeightedHours
    percentWHours2=wHours2/totalWeightedHours
    percentWHours3=wHours3/totalWeightedHours
    percentWHours4=wHours4/totalWeightedHours
    percentWHours5=wHours5/totalWeightedHours


    #Consumption in liters per apartment
    liters1=oil*percentWHours1
    liters2=oil*percentWHours2
    liters3=oil*percentWHours3
    liters4=oil*percentWHours4
    liters5=oil*percentWHours5

    #Insert into the appropriate cell the consumption in liters per apartment
    litersApart1.insert(0, liters1)
    litersApart2.insert(0, liters2)
    litersApart3.insert(0, liters3)
    litersApart4.insert(0, liters4)
    litersApart5.insert(0, liters5)


    #I multiply percentWHours with total ammount consumed by all apartments in order to find its apartment's consumption in €
    #First I will find the price paid per liter weighted by the price of residual oil and new oil
    pricePerLiter=float(residualOil.get())/float(totalLiters)*float(pricePerLiterOfResOil.get())+float(litersNow.get())/float(totalLiters)*float(priceOfNewLiters.get())
    #Then I will find the oil consumed for all apartments expressed in money
    allApartmentsInMoney=float(pricePerLiter*oil)
    #Consumption in liters per apartment expressed in money
    money1=percentWHours1*allApartmentsInMoney
    money2=percentWHours2*allApartmentsInMoney
    money3=percentWHours3*allApartmentsInMoney
    money4=percentWHours4*allApartmentsInMoney
    money5=percentWHours5*allApartmentsInMoney

    #Insert into the appropriate cell the consumption in euros per apartment
    moneyApart1.insert(0, money1)
    moneyApart2.insert(0, money2)
    moneyApart3.insert(0, money3)
    moneyApart4.insert(0, money4)
    moneyApart5.insert(0, money5)
    
    #When the calculation occurs the money per apartment cell closes
    #moneyApart1.configure(state=DISABLED)
    #moneyApart2.configure(state=DISABLED)
    #moneyApart3.configure(state=DISABLED)
    #moneyApart4.configure(state=DISABLED)
    #moneyApart5.configure(state=DISABLED)
    
    #Total oil expressed in money in the oil tank
    totalMoneyInOilTank=float(residualOil.get())*float(pricePerLiterOfResOil.get())+float(totalAmmountOfMoneyOfLitersBeenPutNow.get())
    #Put the above on the proper cell
    totalMoney.insert(0, totalMoneyInOilTank)
    #The cell closes after calculation
    #totalMoney.configure(state=DISABLED)

#This function opens a file with instructions about how to fill in the white cells of the oil consumption calculator
def instructions():
    import os
    file = "notepad.exe Filling_instructions.txt"
    os.system(file)

def clear_all():
    firstMeasurment.delete(0,'end')
    secondMeasurment.delete(0,'end')
    oilConsumption.delete(0,'end')
    firstMeasurment1.delete(0,'end')
    secondMeasurment1.delete(0,'end')
    counterConsumption1.delete(0,'end')
    heatingCalories1.delete(0,'end')
    #caloriesPercent1.delete(0,'end')
    #weightedHours1.delete(0,'end')
    litersApart1.delete(0,'end')
    moneyApart1.delete(0,'end')
    firstMeasurment2.delete(0,'end')
    secondMeasurment2.delete(0,'end')
    counterConsumption2.delete(0,'end')
    heatingCalories2.delete(0,'end')
    #caloriesPercent2.delete(0,'end')
    #weightedHours2.delete(0,'end')
    litersApart2.delete(0,'end')
    moneyApart2.delete(0,'end')
    firstMeasurment3.delete(0,'end')
    secondMeasurment3.delete(0,'end')
    counterConsumption3.delete(0,'end')
    heatingCalories3.delete(0,'end')
    #caloriesPercent3.delete(0,'end')
    #weightedHours3.delete(0,'end')
    litersApart3.delete(0,'end')
    moneyApart3.delete(0,'end')
    firstMeasurment4.delete(0,'end')
    secondMeasurment4.delete(0,'end')
    counterConsumption4.delete(0,'end')
    heatingCalories4.delete(0,'end')
    #caloriesPercent4.delete(0,'end')
    #weightedHours4.delete(0,'end')
    litersApart4.delete(0,'end')
    moneyApart4.delete(0,'end')
    firstMeasurment5.delete(0,'end')
    secondMeasurment5.delete(0,'end')
    counterConsumption5.delete(0,'end')
    heatingCalories5.delete(0,'end')
    #caloriesPercent5.delete(0,'end')
    #weightedHours5.delete(0,'end')
    litersApart5.delete(0,'end')
    moneyApart5.delete(0,'end')
    totalMoney.delete(0, 'end')
    residualOil.delete(0, 'end')
    pricePerLiterOfResOil.delete(0, 'end')
    litersNow.delete(0, 'end')
    totalAmmountOfMoneyOfLitersBeenPutNow.delete(0, 'end')
    priceOfNewLiters.delete(0, 'end')
    
window=Tk()
window.title('Petroleum consumption calculator')
window.geometry("1300x750")
window['background']='#edf1f2'

label_1 = Label(window, font='calibri 10', text = "Oil tank (liters)")
label_1.grid(row = 6, column = 0, sticky = W, pady = 2)
label_2 = Label(window, font='calibri 10', text = "Counter 1 (hours)")
label_2.grid(row = 9, column = 0, sticky = W, pady = 2)
label_3 = Label(window, font='calibri 10', text = "Counter 2 (hours)")
label_3.grid(row = 12, column = 0, sticky = W, pady = 2)
label_4 = Label(window, font='calibri 10', text = "Counter 3 (hours)")
label_4.grid(row = 15, column = 0, sticky = W, pady = 2)
label_5 = Label(window, font='calibri 10', text = "Counter 4 (hours)")
label_5.grid(row = 18, column = 0, sticky = W, pady = 2)
label_6 = Label(window, font='calibri 10', text = "Counter 5 (hours)")
label_6.grid(row = 21, column = 0, sticky = W, pady = 2)                                                                                                                  
label_7 = Label(window, font='calibri 10', text = "       1st measurmemt")
label_7.grid(row = 0, column = 3, sticky = W, pady = 2)
label_8 = Label(window, font='calibri 10', text = "       2nd measurmemt")
label_8.grid(row = 0, column = 6, sticky = W, pady = 2)
label_9 = Label(window, font='calibri 10', text = "         Comsumption")
label_9.grid(row = 0, column = 9, sticky = W, pady = 2)
#label_10 = Label(window, font='calibri 10', text = "         cal/totalcal")
#label_10.grid(row = 0, column = 12, sticky = W, pady = 2)
#label_11 = Label(window, font='calibri 10', text = "    (cal/totalcal)*hours")
#label_11.grid(row = 0, column = 15, sticky = W, pady = 2)
label_12 = Label(window, font='calibri 10', text = "    liters/apartment")
label_12.grid(row = 0, column = 18, sticky = W, pady = 2)
label_13 = Label(window, font='calibri 10', text = "    money/apartment")
label_13.grid(row = 0, column = 21, sticky = W, pady = 2)
label_14 = Label(window, font='calibri 10', text = "    Total money for oil")
label_14.place(x=0, y=400)
label_15 = Label(window, font='calibri 10', text = "       Heating calories")
label_15.grid(row = 0, column = 27, sticky = W, pady = 2)
label_16 = Label(window, font='calibri 10', text = "    Residual oil(liters)")
label_16.place(x=0, y=500)
label_17 = Label(window, font='calibri 10', text = "    Price of residual oil")
label_17.place(x=0, y=450)
label_18 = Label(window, font='calibri 10', text = "    New oil(liters)")
label_18.place(x=0, y=550)
label_19 = Label(window, font='calibri 10', text = "    Money for new oil")
label_19.place(x=0, y=600)
label_20 = Label(window, font='calibri 10', text = "    Price of new liters")
label_20.place(x=0, y=650)

#Measurments for oil tank
firstMeasurment=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
firstMeasurment.grid(row=6,column=3,padx=10,pady=10)
secondMeasurment=Entry(window, font='calibri 18', width=10)
secondMeasurment.grid(row=6,column=6,padx=10,pady=10)
oilConsumption=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
oilConsumption.grid(row=6,column=9,padx=10,pady=10)


#Measurments for counter 1 and heating calories
firstMeasurment1=Entry(window, font='calibri 18', width=10)
firstMeasurment1.grid(row=9,column=3,padx=10,pady=10)
secondMeasurment1=Entry(window, font='calibri 18', width=10)
secondMeasurment1.grid(row=9,column=6,padx=10,pady=10)
counterConsumption1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption1.grid(row=9,column=9,padx=10,pady=10)
heatingCalories1=Entry(window, font='calibri 18', width=10)
heatingCalories1.grid(row=9,column=27,padx=10,pady=10)
#testing percentage of calories
#caloriesPercent1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#caloriesPercent1.grid(row=9,column=12,padx=10,pady=10)
#testing weighted hours of 1st counter
#weightedHours1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#weightedHours1.grid(row=9,column=15,padx=10,pady=10)
#Consumption in liters for the 1st appartment
litersApart1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
litersApart1.grid(row=9,column=18,padx=10,pady=10)
#Consumption in euros for the 1st appartment
moneyApart1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
moneyApart1.grid(row=9,column=21,padx=10,pady=10)

#Measurments for counter 2 and heating calories
firstMeasurment2=Entry(window, font='calibri 18', width=10)
firstMeasurment2.grid(row=12,column=3,padx=10,pady=10)
secondMeasurment2=Entry(window, font='calibri 18', width=10)
secondMeasurment2.grid(row=12,column=6,padx=10,pady=10)
counterConsumption2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption2.grid(row=12,column=9,padx=10,pady=10)
heatingCalories2=Entry(window, font='calibri 18', width=10)
heatingCalories2.grid(row=12,column=27,padx=10,pady=10)
#testing percentage of calories
#caloriesPercent2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#caloriesPercent2.grid(row=12,column=12,padx=10,pady=10)
#testing weighted hours of 2nd counter
#weightedHours2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#weightedHours2.grid(row=12,column=15,padx=10,pady=10)
#Consumption in liters for the 2nd appartment
litersApart2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
litersApart2.grid(row=12,column=18,padx=10,pady=10)
#Consumption in euros for the 2nd apartment
moneyApart2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
moneyApart2.grid(row=12,column=21,padx=10,pady=10)

#Measurments for counter 3 and heating calories
firstMeasurment3=Entry(window, font='calibri 18', width=10)
firstMeasurment3.grid(row=15,column=3,padx=10,pady=10)
secondMeasurment3=Entry(window, font='calibri 18', width=10)
secondMeasurment3.grid(row=15,column=6,padx=10,pady=10)
counterConsumption3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption3.grid(row=15,column=9,padx=10,pady=10)
heatingCalories3=Entry(window, font='calibri 18', width=10)
heatingCalories3.grid(row=15,column=27,padx=10,pady=10)
#testing percentage of calories
#caloriesPercent3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#caloriesPercent3.grid(row=15,column=12,padx=10,pady=10)
#testing weighted hours of 3rd counter
#weightedHours3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#weightedHours3.grid(row=15,column=15,padx=10,pady=10)
#Consumption in liters for the 3rd apartment
litersApart3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
litersApart3.grid(row=15,column=18,padx=10,pady=10)
#Consumption in euros for the 3rd apartment
moneyApart3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
moneyApart3.grid(row=15,column=21,padx=10,pady=10)

#Measurments for counter 4 and heating calories
firstMeasurment4=Entry(window, font='calibri 18', width=10)
firstMeasurment4.grid(row=18,column=3,padx=10,pady=10)
secondMeasurment4=Entry(window, font='calibri 18', width=10)
secondMeasurment4.grid(row=18,column=6,padx=10,pady=10)
counterConsumption4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption4.grid(row=18,column=9,padx=10,pady=10)
heatingCalories4=Entry(window, font='calibri 18', width=10)
heatingCalories4.grid(row=18,column=27,padx=10,pady=10)
#testing percentage of calories
#caloriesPercent4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#caloriesPercent4.grid(row=18,column=12,padx=10,pady=10)
#testing weighted hours of 4th counter
#weightedHours4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#weightedHours4.grid(row=18,column=15,padx=10,pady=10)
#Consumption in liters for the 4th apartment
litersApart4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
litersApart4.grid(row=18,column=18,padx=10,pady=10)
#Consumption in euros for the 4th apartment
moneyApart4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
moneyApart4.grid(row=18,column=21,padx=10,pady=10)

#Measurments for counter 5 and heating calories
firstMeasurment5=Entry(window, font='calibri 18', width=10)
firstMeasurment5.grid(row=21,column=3,padx=10,pady=10)
secondMeasurment5=Entry(window, font='calibri 18', width=10)
secondMeasurment5.grid(row=21,column=6,padx=10,pady=10)
counterConsumption5=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption5.grid(row=21,column=9,padx=10,pady=10)
heatingCalories5=Entry(window, font='calibri 18', width=10)
heatingCalories5.grid(row=21,column=27,padx=10,pady=10)
#testing percentage of calories
#caloriesPercent5=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#caloriesPercent5.grid(row=21,column=12,padx=10,pady=10)
#testing weighted hours of 5th counter
#weightedHours5=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
#weightedHours5.grid(row=21,column=15,padx=10,pady=10)
#Consumption in liters for the 5th appartment
litersApart5=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
litersApart5.grid(row=21,column=18,padx=10,pady=10)
#Consumption in euros for the 5th apartment
moneyApart5=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
moneyApart5.grid(row=21,column=21,padx=10,pady=10)

#This is the entry box for the total money paid for the oil of all apartments
totalMoney=Entry(window, font='calibri 18', width=10, bg='#ebc8a4') 
totalMoney.place(x=130, y=400)
#This is the entry box for the price per liter of the residual liters left in the oil tank from the previous year
pricePerLiterOfResOil=Entry(window, font='calibri 18', width=10) 
pricePerLiterOfResOil.place(x=130, y=450)
#This is the entry box for the residual liters left in the oil tank from the previous year
residualOil=Entry(window, font='calibri 18', width=10) 
residualOil.place(x=130, y=500)
#This is the entry box for the new liters been put in the oil tank now
litersNow=Entry(window, font='calibri 18', width=10) 
litersNow.place(x=130, y=550)
#This is the entry box for the price of new liters been put in the oil tank now
totalAmmountOfMoneyOfLitersBeenPutNow=Entry(window, font='calibri 18', width=10) 
totalAmmountOfMoneyOfLitersBeenPutNow.place(x=130, y=600)
#This is the entry box for the price per liter of new liters been put in the oil tank now
priceOfNewLiters=Entry(window, font='calibri 18', width=10) 
priceOfNewLiters.place(x=130, y=650)

#Clear all button
clear=Button(window, text='Clear all', font='calibri 16', command=lambda:clear_all())
clear.place(x=400, y=400)

#Calculation button
calc=Button(window, text='Calculation', font='calibri 20', command=lambda:consumption())
calc.place(x=1000, y=400)

#Open file with instructions
instruct=Button(window, text='Filling instructions', font='calibri 16', command=lambda:instructions())
instruct.place(x=600, y=400)

window.mainloop()
