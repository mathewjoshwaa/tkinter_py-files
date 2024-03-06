from tkinter import *
from tkinter.ttk import *
import calendar

root=Tk()
root.title("Calendar")
root.geometry("350x350")


def show():
    s_month=selected_month.get()
    print(s_month)
    s_year=selected_year.get()
    print(s_year)
    calendar_output=calendar.month(s_year,s_month)
    calendar_field.delete("1.0","end")
    calendar_field.insert("end",calendar_output)



lbl1=Label(root,text="Calendar",font=("Arial",20))
lbl1.pack()

selected_month=IntVar()
month=[]
for mm in range(1,13):
    month.append(mm)

lbl_mon=Label(root,text="select month",font=("Arial",10))
lbl_mon.pack()
month_cb=(Combobox(root,width=7,textvariable=selected_month,values=month))
month_cb.pack()

selected_year=IntVar()
year=[]
for m in range(2000,2023):
    year.append(m)

lbl_yea=Label(root,text="select year",font=("Arial",10))
lbl_yea.pack()
year_cb=(Combobox(root,width=7,textvariable=selected_year,values=year))
year_cb.pack()

btn=Button(root,command=show,text="show")
btn.pack()

calendar_field=Text(root,width=20,height=8,font=("consolas",14))
calendar_field.pack(expand=False,fill=None)

root.mainloop()