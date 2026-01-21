import tkinter
from tkinter import *

root=Tk()
root.title("Calculator") 
root.geometry("450x370+100+200")
root.resizable(False,False)
root.configure(bg="black")

# show values
equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

#clear for next
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

#all calculations
def calculate():
    global equation
    result=""
    if equation != "":       #not proceed if there is nothing
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=30,y=110)
Button(root,text="/",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=140,y=110)
Button(root,text="%",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=250,y=110)
Button(root,text="*",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=360,y=110)

Button(root,text="7",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=30,y=160)
Button(root,text="8",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=140,y=160)
Button(root,text="9",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=250,y=160)
Button(root,text="-",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=360,y=160)

Button(root,text="4",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=30,y=210)
Button(root,text="5",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=140,y=210)
Button(root,text="6",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=250,y=210)
Button(root,text="+",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=360,y=210)

Button(root,text="1",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=30,y=260)
Button(root,text="2",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=140,y=260)
Button(root,text="3",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=250,y=260)
Button(root,text="0",width=15,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=30,y=310)

Button(root,text=".",width=5,height=1,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=250,y=310)
Button(root,text="=",width=5,height=3,font={"arial",30,"bold"},bd=1,fg="#fff",bg="#5e9037",command=lambda:calculate()).place(x=360,y=260)

root.mainloop()
