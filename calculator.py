from tkinter import *

def btnclick(numbers):
    global operator
    operator+=str(numbers)
    text_input.set(operator)

def clearbtn():
    global operator
    operator=""
    text_input.set("")

def value():
    global operator
    result=str(eval(text_input.get()))
    text_input.set(result)
    operator=""

def delete():
    global operator
    operator=operator[:-1]
    text_input.set(operator)

window=Tk()
window.title("Calculator")
operator=""
text_input=StringVar()

entry_bar=Entry(window,textvariable=text_input,justify="right",bd=15,bg="light blue",font=("arial",20,"bold")).grid(columnspan=4)

bt1=Button(window,text="7",font=("arial",20,"bold"),padx=20,bd=8,bg="Light Green",command=lambda : btnclick(7)).grid(row=2)
bt2=Button(window,text="8",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green",command=lambda : btnclick(8)).grid(row=2,column=1)
bt3=Button(window,text="9",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green",command=lambda : btnclick(9)).grid(row=2,column=2)
bt4=Button(window,text="+",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green",command=lambda : btnclick("+")).grid(row=2,column=3)

bt5=Button(window,text="4",font=("arial",20,"bold"),padx=20,bd=8,bg="Light Green", command=lambda: btnclick(4)).grid(row= 3)
bt6=Button(window,text="5",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda: btnclick(5)).grid(row= 3, column=1)
bt7=Button(window,text="6",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda: btnclick(6)).grid(row= 3, column=2)
bt8=Button(window,text="-",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda: btnclick("-")).grid(row= 3, column=3)

bt9=Button(window,text="1",font=("arial",20,"bold"),padx=20,bd=8,bg="Light Green", command=lambda : btnclick(1)).grid(row=4)
bt10=Button(window,text="2",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda : btnclick(2)).grid(row=4,column=1)
bt11=Button(window,text="3",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda : btnclick(3)).grid(row=4,column=2)
bt12=Button(window,text="*",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green", command=lambda : btnclick("*")).grid(row=4,column=3)

bt13=Button(window,text="0",font=("arial",20,"bold"),padx=20,bd=8,pady=14,bg="Light Green", command=lambda: btnclick(0)).grid(row=5)
bt14=Button(window,text="=",font=("arial",20,"bold"),padx=14,bd=8,pady=14,bg="Light Green", command=value).grid(row=5,column=1)
bt15=Button(window,text="Clear",font=("arial",19,"bold"),padx=14,bd=8,pady=14,bg="Light Green", width=2, command=clearbtn).grid(row=5,column=2)
bt16=Button(window,text="/",font=("arial",20,"bold"),padx=14,bd=8,pady=14,bg="Light Green", command=lambda: btnclick("/")).grid(row=5,column=3)

bt17=Button(window,text="Off",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green",command=window.destroy).grid(row=6,column=0)
bt19=Button(window,text=".",font=("arial",20,"bold"),padx=18,bd=8,bg="Light Green",command=lambda: btnclick(".")).grid(row=6,column=1)
bt18=Button(window,text="Delete",font=("arial",20,"bold"),padx=14,bd=8,bg="Light Green",command=delete).grid(row=6,column=2,columnspan=2)


window.mainloop()