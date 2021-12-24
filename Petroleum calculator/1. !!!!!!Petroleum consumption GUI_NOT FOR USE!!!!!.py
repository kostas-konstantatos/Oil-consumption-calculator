from tkinter import *


def consumption():
    oilConsumption.configure(state=NORMAL)
    counterConsumption1.configure(state=NORMAL)
    counterConsumption2.configure(state=NORMAL)
    counterConsumption3.configure(state=NORMAL)
    counterConsumption4.configure(state=NORMAL)
    #Starts with zero
    oilConsumption.delete(0, 'end')
    counterConsumption1.delete(0, 'end')
    counterConsumption2.delete(0, 'end')
    counterConsumption3.delete(0, 'end')
    counterConsumption4.delete(0, 'end')
    #Performs the subtraction between 2nd and 1st measurment
    oil=int(firstMeasurment.get())-int(secondMeasurment.get())
    count1=int(secondMeasurment1.get())-int(firstMeasurment1.get())
    count2=int(secondMeasurment2.get())-int(firstMeasurment2.get())
    count3=int(secondMeasurment3.get())-int(firstMeasurment3.get())
    count4=int(secondMeasurment4.get())-int(firstMeasurment4.get())
    #Insert into the appropriate cell the deference of counters and oil consumption
    oilConsumption.insert(0, oil)
    counterConsumption1.insert(0, count1)
    counterConsumption2.insert(0, count2)
    counterConsumption3.insert(0, count3)
    counterConsumption4.insert(0, count4)
    #When the calculation occurs the cell closes
    oilConsumption.configure(state=DISABLED)
    counterConsumption1.configure(state=DISABLED)
    counterConsumption2.configure(state=DISABLED)
    counterConsumption3.configure(state=DISABLED)
    counterConsumption4.configure(state=DISABLED)

    #Percentage of calories per apartment relative to total calories
    
    
window=Tk()
window.title('Petroleum consumption calculator')
window.geometry("1000x500")
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
label_6 = Label(window, font='calibri 10', text = "       1st measurmemt")
label_6.grid(row = 0, column = 3, sticky = W, pady = 2)
label_7 = Label(window, font='calibri 10', text = "       2nd measurmemt")
label_7.grid(row = 0, column = 6, sticky = W, pady = 2)
"""
label_8 = Label(window, font='calibri 10', text = "       3rd measurmemt")
label_8.grid(row = 0, column = 9, sticky = W, pady = 2)
label_9 = Label(window, font='calibri 10', text = "       4th measurment")
label_9.grid(row = 0, column = 12, sticky = W, pady = 2)
label_10 = Label(window, font='calibri 10', text = "       5th measurmemt")
label_10.grid(row = 0, column = 15, sticky = W, pady = 2)
"""
label_11 = Label(window, font='calibri 10', text = "         Comsumption")
label_11.grid(row = 0, column = 9, sticky = W, pady = 2)
label_12 = Label(window, font='calibri 10', text = "       Heating calories")
label_12.grid(row = 0, column = 18, sticky = W, pady = 2)




#Measurments for oil tank
firstMeasurment=Entry(window, font='calibri 18', width=10)
firstMeasurment.grid(row=6,column=3,padx=10,pady=10)
secondMeasurment=Entry(window, font='calibri 18', width=10)
secondMeasurment.grid(row=6,column=6,padx=10,pady=10)

"""
thirdMeasurment=Entry(window, font='calibri 18', width=10)
thirdMeasurment.grid(row=6,column=9,padx=10,pady=10)
fourthMeasurment=Entry(window, font='calibri 18', width=10)
fourthMeasurment.grid(row=6,column=12,padx=10,pady=10)
fifthMeasurment=Entry(window, font='calibri 18', width=10)
fifthMeasurment.grid(row=6,column=15,padx=10,pady=10)
"""
oilConsumption=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
oilConsumption.grid(row=6,column=9,padx=10,pady=10)


#Measurments for counter 1 and heating calories
firstMeasurment1=Entry(window, font='calibri 18', width=10)
firstMeasurment1.grid(row=9,column=3,padx=10,pady=10)
secondMeasurment1=Entry(window, font='calibri 18', width=10)
secondMeasurment1.grid(row=9,column=6,padx=10,pady=10)

"""
thirdMeasurment1=Entry(window, font='calibri 18', width=10)
thirdMeasurment1.grid(row=9,column=9,padx=10,pady=10)
fourthMeasurment1=Entry(window, font='calibri 18', width=10)
fourthMeasurment1.grid(row=9,column=12,padx=10,pady=10)
fifthMeasurment1=Entry(window, font='calibri 18', width=10)
fifthMeasurment1.grid(row=9,column=15,padx=10,pady=10)
"""
counterConsumption1=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption1.grid(row=9,column=9,padx=10,pady=10)
heatingCalories1=Entry(window, font='calibri 18', width=10)
heatingCalories1.grid(row=9,column=18,padx=10,pady=10)

#Measurments for counter 2 and heating calories
firstMeasurment2=Entry(window, font='calibri 18', width=10)
firstMeasurment2.grid(row=12,column=3,padx=10,pady=10)
secondMeasurment2=Entry(window, font='calibri 18', width=10)
secondMeasurment2.grid(row=12,column=6,padx=10,pady=10)

"""
thirdMeasurment2=Entry(window, font='calibri 18', width=10)
thirdMeasurment2.grid(row=12,column=9,padx=10,pady=10)
fourthMeasurment2=Entry(window, font='calibri 18', width=10)
fourthMeasurment2.grid(row=12,column=12,padx=10,pady=10)
fifthMeasurment2=Entry(window, font='calibri 18', width=10)
fifthMeasurment2.grid(row=12,column=15,padx=10,pady=10)
"""
counterConsumption2=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption2.grid(row=12,column=9,padx=10,pady=10)
heatingCalories2=Entry(window, font='calibri 18', width=10)
heatingCalories2.grid(row=12,column=18,padx=10,pady=10)


#Measurments for counter 3 and heating calories
firstMeasurment3=Entry(window, font='calibri 18', width=10)
firstMeasurment3.grid(row=15,column=3,padx=10,pady=10)
secondMeasurment3=Entry(window, font='calibri 18', width=10)
secondMeasurment3.grid(row=15,column=6,padx=10,pady=10)
"""
thirdMeasurment3=Entry(window, font='calibri 18', width=10)
thirdMeasurment3.grid(row=15,column=9,padx=10,pady=10)
fourthMeasurment3=Entry(window, font='calibri 18', width=10)
fourthMeasurment3.grid(row=15,column=12,padx=10,pady=10)
fifthMeasurment3=Entry(window, font='calibri 18', width=10)
fifthMeasurment3.grid(row=15,column=15,padx=10,pady=10)
"""
counterConsumption3=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption3.grid(row=15,column=9,padx=10,pady=10)
heatingCalories3=Entry(window, font='calibri 18', width=10)
heatingCalories3.grid(row=15,column=18,padx=10,pady=10)

#Measurments for counter 4 and heating calories
firstMeasurment4=Entry(window, font='calibri 18', width=10)
firstMeasurment4.grid(row=18,column=3,padx=10,pady=10)
secondMeasurment4=Entry(window, font='calibri 18', width=10)
secondMeasurment4.grid(row=18,column=6,padx=10,pady=10)
"""
thirdMeasurment4=Entry(window, font='calibri 18', width=10)
thirdMeasurment4.grid(row=18,column=9,padx=10,pady=10)
fourthMeasurment4=Entry(window, font='calibri 18', width=10)
fourthMeasurment4.grid(row=18,column=12,padx=10,pady=10)
fifthMeasurment4=Entry(window, font='calibri 18', width=10)
fifthMeasurment4.grid(row=18,column=15,padx=10,pady=10)
"""
counterConsumption4=Entry(window, font='calibri 18', width=10, bg='#ebc8a4')
counterConsumption4.grid(row=18,column=9,padx=10,pady=10)
heatingCalories4=Entry(window, font='calibri 18', width=10)
heatingCalories4.grid(row=18,column=18,padx=10,pady=10)

calc=Button(window, text='Calculation', font='calibri 16', command=lambda:consumption())
calc.place(x=300, y=400)



window.mainloop()
