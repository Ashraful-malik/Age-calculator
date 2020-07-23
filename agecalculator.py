from tkinter import*
import time
# from tkinter import messagebox
year=time.strftime("%Y")
month=12
a=("year old ")

def showdata():
    
    try:
        
        userdate=int(date_value.get())
        usermonth=int(month_value.get())
        useryear=int(year_value.get())
        listbox.insert(END,int(year)-useryear,a)
        listbox.insert(END,int(month)-usermonth,"month left for your birthday ")
    except Exception:
        listbox.insert(END,str(" please fill all data"))
    
    if userdate>31:
        
        date_entry.delete(0,END)
        date_entry.insert(END,"Enter valif date")
        listbox.delete(0,END)
          
            
    elif usermonth>12:
        month_entry.delete(0,END)
        month_entry.insert(END,"Enter valif month ")
        listbox.delete(0,END)

    elif usermonth==month:
        listbox.insert(END,"happy birthday")

def cleanall():
    listbox.delete(0,END)

window=Tk()
window.title("Age calculator")
window.geometry("450x450")
window.resizable(FALSE,False)
frame=Frame(window)
frame.pack(side=TOP)

title=Label(frame,text="Age Calculator",font="jokerman 20 bold",fg="red")
title.grid(row=0,column=3)


date_value=StringVar()
month_value=StringVar()
year_value=StringVar()

# date box 
date_name=Label(frame,text="Date",font="arial 15 bold",fg="blue")
date_name.grid(row=1,column=2)

date_entry=Entry(frame,textvariable=date_value,font="arial 15 bold",justify="right")
date_entry.grid(row=1,column=3,pady=10)

# month box 
month_name=Label(frame,text="Month",font="arial 15 bold",fg="blue")
month_name.grid(row=2,column=2)

month_entry=Entry(frame,textvariable=month_value,font="arial 15 bold",justify="right")
month_entry.grid(row=2,column=3,pady=10)

# year box 
year_name=Label(frame,text="Year",font="arial 15 bold",fg="blue")
year_name.grid(row=3,column=2)

year_entry=Entry(frame,textvariable=year_value,font="arial 15 bold",justify="right")
year_entry.grid(row=3,column=3,pady=10)

# list result box
listname=Label(frame,text="RESULT",font="arial 15 bold",fg="green")
listname.grid(row=4,column=1)

listbox=Listbox(frame,width=32,height=5)
listbox.grid(row=4,column=3)

# button
result_button=Button(frame,text="Result",width=20,pady=10,command=showdata,activebackground="orange",font=" safron 12 bold",activeforeground="white")
result_button.grid(row=5,column=3,columnspan=4,pady=10)

claenall=Button(frame,text="Clean",width=10,pady=10,command=cleanall,font=" safron 10 bold",activeforeground="white",activebackground="orange")
claenall.grid(row=5,column=0,columnspan=2)

window.mainloop()
