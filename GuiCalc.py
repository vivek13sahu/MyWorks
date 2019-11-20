import tkinter
#from tkinter import*
#tkinter._test() 
                                                             #initialvale
val=""
A=0
opr=""


def btn_1_isclicked():                                       #NumericButtons
    global val
    val+="1"
    data.set(val)
def btn_2_isclicked():
    global val
    val+="2"
    data.set(val)
def btn_3_isclicked():
    global val
    val+="3"
    data.set(val)
def btn_4_isclicked():
    global val
    val+="4"
    data.set(val)
def btn_5_isclicked():
    global val
    val+="5"
    data.set(val)
def btn_6_isclicked():
    global val
    val+="6"
    data.set(val)
def btn_7_isclicked():
    global val
    val+="7"
    data.set(val)
def btn_8_isclicked():
    global val
    val+="8"
    data.set(val)
def btn_9_isclicked():
    global val
    val+="9"
    data.set(val)
def btn_0_isclicked():
    global val
    val+="0"
    data.set(val)

                                                            #OperatorButtons
def btn_p_clicked():
    global A
    global val
    global opr
    A=int(val)
    opr="+"
    val+="+"
    data.set(val)

def btn_s_clicked():
    global A
    global val
    global opr
    A=int(val)
    opr="-"
    val+="-"
    data.set(val)

def btn_d_clicked():
    global A
    global val
    global opr
    A=int(val)
    opr="/"
    val+="÷"
    data.set(val)

def btn_m_clicked():
    global A
    global val
    global opr
    A=int(val)
    opr="*"
    val+="x"
    data.set(val)

def btn_c_clicked():
    global A
    global val
    global opr
    A=0
    opr=""
    val=""
    data.set(val)

def btn_e_clicked():                                         #LogicalAction
    global A
    global val
    global opr
    vam=val
    if opr=="+":
        v=int(vam.split("+")[1])
        c=A+v
        data.set(c)
        val=str(c)
    elif opr=="-":
        v=int(vam.split("-")[1])
        c=A-v
        data.set(c)
        val=str(c)
    elif opr=="*":
        v=int(vam.split("x")[1])
        c=A*v
        data.set(c)
        val=str(c)
    elif opr=="/":
        v=int(vam.split("÷")[1])
        if v==0:
            messagebox.showerror("Error","Invalid Input")
            A=0
            opr=""
            val=""
            data.set(val)
        else:
            c=int(A/v)
            data.set(c)
            val=str(c)


root=tkinter.Tk()                                                  #root
root.geometry("400x400+300+300")
root.resizable(1,1)
root.title("MyCalc")     
               

data=StringVar()
lbl=Label(root,anchor=E,textvariable=data,font=("CURSIVE",30),relief=GROOVE,highlightbackground="red", highlightcolor="red",bd=10, highlightthickness=10)
lbl.pack(expand=True,fill="both")


br1=Frame(root,bg="#2B60DE")                                    #ButtonRow1
br1.pack(expand=True,fill="both")


bn1=Button(br1,bg="#2B60DE",text="+",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_p_clicked)
bn1.pack(side=RIGHT,expand=True,fill="both")
bn2=Button(br1,bg="#2B60DE",text="7",font=("ROBOTO",25),command=btn_7_isclicked)
bn2.pack(side=RIGHT,expand=True,fill="both")
bn3=Button(br1,bg="#2B60DE",text="8",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_8_isclicked)
bn3.pack(side=RIGHT,expand=True,fill="both")
bn4=Button(br1,bg="#2B60DE",text="9",font=("ROBOTO",25),command=btn_9_isclicked)
bn4.pack(side=RIGHT,expand=True,fill="both")



br2=Frame(root,bg="#306EFF")                                   #ButtonRow2
br2.pack(expand=True,fill="both")


bn1=Button(br2,bg="#306EFF",text=" -",font=("ROBOTO",25),command=btn_s_clicked)
bn1.pack(side=RIGHT,expand=True,fill="both")
bn2=Button(br2,bg="#306EFF",text="4",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_4_isclicked)
bn2.pack(side=RIGHT,expand=True,fill="both")
bn3=Button(br2,bg="#306EFF",text="5",font=("ROBOTO",25),command=btn_5_isclicked)
bn3.pack(side=RIGHT,expand=True,fill="both")
bn4=Button(br2,bg="#306EFF",text="6",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_6_isclicked)
bn4.pack(side=RIGHT,expand=True,fill="both")

br3=Frame(root,bg="#38ACEC")                                   #ButtonRow3
br3.pack(expand=True,fill="both")


bn1=Button(br3,bg="#38ACEC",text="÷",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_d_clicked)
bn1.pack(side=RIGHT,expand=True,fill="both")
bn2=Button(br3,bg="#38ACEC",text="1",font=("ROBOTO",25),command=btn_1_isclicked)
bn2.pack(side=RIGHT,expand=True,fill="both")
bn3=Button(br3,bg="#38ACEC",text="2",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_2_isclicked)
bn3.pack(side=RIGHT,expand=True,fill="both")
bn4=Button(br3,bg="#38ACEC",text="3",font=("ROBOTO",25),command=btn_3_isclicked)
bn4.pack(side=RIGHT,expand=True,fill="both")

br4=Frame(root,bg="#3BB9FF")                                   #ButtonRow4
br4.pack(expand=True,fill="both")


bn1=Button(br4,bg="#3BB9FF",text=" x",font=("ROBOTO",20),command=btn_m_clicked)
bn1.pack(side=RIGHT,expand=True,fill="both")
bn2=Button(br4,bg="#3BB9FF",text="=",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_e_clicked)
bn2.pack(side=RIGHT,expand=True,fill="both")
bn3=Button(br4,bg="#3BB9FF",text="0",font=("ROBOTO",25),command=btn_0_isclicked)
bn3.pack(side=RIGHT,expand=True,fill="both")
bn4=Button(br4,bg="#3BB9FF",text="C",font=("ROBOTO",25),relief=GROOVE,border=1,command=btn_c_clicked)
bn4.pack(side=RIGHT,expand=True,fill="both")


root.mainloop()