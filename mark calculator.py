from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("MARK SHEET")
def show():
    result=""
    m1=int(txt_m1.get())
    m2=int(txt_m2.get())
    m3=int(txt_m3.get())

    total=m1+m2+m3
    per=total/3
    if m1>=40 and m2>=40 and m3>=40:
        result="Pass"
    else:
        result="Fail"

    txt_tot.config(text=total)
    txt_per.config(text=per)
    txt_res.config(text=result)

lbl_ed=Label(root,text="Mark sheet",font=("Arial,25"))
lbl_ed.grid(row=0,column=1)

lbl_name=Label(root,text="Enter a Name:",font=("Arial",15))
txt_name=Entry(root,font=("Arial,10"))
lbl_name.grid(row=1,column=0)
txt_name.grid(row=1,column=1)

lbl_reg=Label(root,text="Enter a register no:",font=("Arial,15"))
txt_reg=Entry(root,font=("Arial,10"))
lbl_reg.grid(row=2,column=0)
txt_reg.grid(row=2,column=1)

lbl_m1=Label(root,text="Python:",font=("Arial,15"))
txt_m1=Entry(root,font=("Arial,10"))
lbl_m1.grid(row=3,column=0)
txt_m1.grid(row=3,column=1)

lbl_m2=Label(root,text="AI & DA:",font=("Arial,15"))
txt_m2=Entry(root,font=("Arial,10"))
lbl_m2.grid(row=4,column=0)
txt_m2.grid(row=4,column=1)

lbl_m3=Label(root,text="Cloud computing:",font=("Arial,15"))
txt_m3=Entry(root,font=("Arial,10"))
lbl_m3.grid(row=5,column=0)
txt_m3.grid(row=5,column=1)

btn=Button(root,command=show,text="calculate",font=("Arial,15"))
btn.grid(row=6,column=1)

lbl_tot=Label(root,text="Total:",font=("Arial,15"))
txt_tot=Label(root,text="0",font=("Arial,10"))
lbl_tot.grid(row=7,column=0)
txt_tot.grid(row=7,column=1)

lbl_per=Label(root,text="Percentage:",font=("Arial,15"))
txt_per=Label(root,font=("Arial,10"),text="0")
lbl_per.grid(row=8,column=0)
txt_per.grid(row=8,column=1)

lbl_res=Label(root,text="Result:",font=("Arial,15"))
txt_res=Label(root,font=("Arial,10"),text="0",)
lbl_res.grid(row=9,column=0)
txt_res.grid(row=9,column=1)



root.mainloop()