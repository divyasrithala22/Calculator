from tkinter import *

def clickButton(num):
   global operator
   operator=operator+str(num)
   EnterInput.set(operator)
def evaluatingOperator():
   global operator
   output=str(eval(operator))
   EnterInput.set(output)
def clearButtonDisplay():
   global operator
   operator=""
   EnterInput.set(operator)
cal=Tk()
cal.title("Calculator")
operator=""
EnterInput=StringVar()
Display_text=Entry(cal,font=('arial',15,'bold'),bd=10,justify="right",insertwidth=5,textvariable=EnterInput,bg="lightskyblue").grid(columnspan=12)
 
 
bt7=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(7),bg="lightskyblue",text="7",bd=4,padx=15,pady=10).grid(row=1,column=0)
bt8=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(8),bg="lightskyblue",text="8",bd=4,padx=15,pady=10).grid(row=1,column=1)
bt9=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(9),bg="lightskyblue",text="9",bd=4,padx=15,pady=10).grid(row=1,column=2)
addition=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton('+'),bg="lightskyblue",text="+",bd=4,padx=15,pady=10).grid(row=1,column=3)
 
 
 
bt4=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(4),bg="lightskyblue",text="4",bd=4,padx=15,pady=10).grid(row=2,column=0)
bt5=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(5),bg="lightskyblue",text="5",bd=4,padx=15,pady=10).grid(row=2,column=1)
bt6=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(6),bg="lightskyblue",text="6",bd=4,padx=15,pady=10).grid(row=2,column=2)
subtraction=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton('-'),bg="lightskyblue",text="-",bd=4,padx=15,pady=10).grid(row=2,column=3)
 
 
 
bt1=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(1),bg="lightskyblue",text="1",bd=4,padx=15,pady=10).grid(row=3,column=0)
bt2=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(2),bg="lightskyblue",text="2",bd=4,padx=15,pady=10).grid(row=3,column=1)
bt3=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(3),bg="lightskyblue",text="3",bd=4,padx=15,pady=10).grid(row=3,column=2)
multiplication=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton('*'),bg="lightskyblue",text="*",bd=4,padx=15,pady=10).grid(row=3,column=3)
 
 
bt0=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton(0),bg="lightskyblue",text="0",bd=4,padx=15,pady=10).grid(row=4,column=0)
btC=Button(cal,font=('arial',13,'bold'),command=clearButtonDisplay,bg="lightskyblue",text="C",bd=4,padx=15,pady=10).grid(row=4,column=1)
eql=Button(cal,font=('arial',13,'bold'),command=evaluatingOperator,bg="lightskyblue",text="=",bd=4,padx=15,pady=10).grid(row=4,column=2)
division=Button(cal,font=('arial',13,'bold'),command=lambda:clickButton('/'),bg="lightskyblue",text="/",bd=4,padx=15,pady=10).grid(row=4,column=3)
cal.mainloop()
