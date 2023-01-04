from tkinter import *
from tkinter import ttk   
from PIL import ImageTk, Image
import mysql.connector as sqltor
from tkinter import messagebox
con=sqltor.connect(host="localhost",user="root",password="1661",database="bloodbucket")
cur=con.cursor()
#pip  install pillow
def nearest(a):
    global n
    n=[]
    cur.execute("Select Hospital_Name,pincode from connected_hospitals")
    b=cur.fetchall()
    d={}
    l=[]
    if 201298<=a<=201313:
        for i in b:
            if a in i:
                l.append(i[0])
        if len(l)==0:
            for i in b:
                d[i[0]]=abs(a-i[1])
                l.append(abs(a-i[1]))
            c=min(l)
            print("Nearest Hospitals:")
            n=[i for i in d if d[i]==c]
            print(n)
            return n
        else:
            print("Nearest Hospitals:\n",l)
            return l
    else:
        messagebox.showinfo("Pincode Out of range!","No Blood Bank Found In Given Range")
def appointment_slip():
    global name_1,phone_1,hospital_1,requirement_1,time_1
    Name_1=name_1.get()
    Phone_1=phone_1.get()
    cur.execute('select PName,`P.No`,Hospital_Name,Requirement,Apt_Time from person_info where `P.No`={}'.format(Phone_1))
    a=cur.fetchall()
    if len(a)!=0:
        Name_1,Phone_1,hospital_1,requirement_1,time_1=a[0][0],a[0][1],a[0][2],a[0][3],a[0][4]
        print('Name:',a[0][0])
        print('P.No:',a[0][1])
        print('Hospital_Name:',a[0][2])
        print('Requirement:',a[0][3])
        print('Apt_Time:',a[0][4])
        messagebox.showinfo("Appointment Found!","Appointment Shown Below")
    else:
        messagebox.showinfo("No Appointment!","No Appointment found for the given information\nPlease retry")
def winzero():
    window00.destroy()
    windown0()

def windown0():
    global window0
    window0=Tk()
    window0.geometry("400x200")
    window0.configure(background='#ff9966')
    window0.title("Blood_Bucket")
    #window0.iconbitmap("File Address")
    la1=Label(window0,text="Welcome To Blood Bucket",fg="black",bg="#ff9966",font='5')
    la1.place(x=90,y=15)
    bt_1=Button(window0,text="Make An Appointment",command=windowN1,bg="#ff9966",cursor='hand2')
    bt_1.place(x=145,y=100)
    bt_2=Button(window0,text="  Check Appointment  ",command=CheckApp,bg="#ff9966",cursor='hand2')
    bt_2.place(x=145,y=140)
    window0.mainloop()

def CheckApp():
    global window00
    global name_1
    global phone_1
    window0.destroy()
    window00=Tk()
    window00.geometry("400x200")
    window00.configure(background='#ff9966')
    window00.title("  Check Appointment  ")
    l1=Label(window00,text="  Checking Appointment \n*************************",fg="black",bg="#ff9966",font='5')
    l1.place(x=70,y=20)
    Name_1= Label(window00,text = "Name -->",fg="black",bg="#ff9966")
    Name_1.place(x=40,y=80)
    name_1=StringVar()
    Name_1 = Entry(window00,textvariable=name_1)
    Name_1.place(x=150,y=80)
    Phone_1= Label(window00,text = "Phone Number -->",fg="black",bg="#ff9966")
    Phone_1.place(x=40,y=120)
    phone_1=StringVar()
    Phone_1 = Entry(window00,textvariable=phone_1)
    Phone_1.place(x=150,y=120)
    bt_5=Button(window00,text="Next",command=appointment_slip)
    bt_5.place(x=350,y=165)
    bt_6=Button(window00,text="Back",command=winzero)
    bt_6.place(x=90,y=165)
    window00.mainloop()

def windowN1():
    global window1
    #global pincode
    global Pin_Field # a=pincode.get()
    window1=Tk()
    window1.geometry("400x200")
    window1.configure(background='#ff9966')
    window1.title("PinCode Entry")
    la1=Label(window1,text="To find the nearest blood centers \n*********************\nEnter your pincode:",fg="black",bg="#ff9966",font='5')
    la1.place(x=60,y=30)
    #pincode=StringVar()
    Pin_Field=Entry(window1)
    Pin_Field.place(x=145,y=130)
    #must submit
    bt_2=Button(window1,text="Submit",command=printp,bg="#ff9966",cursor='hand2')
    bt_2.place(x=280,y=130)
    bt_1=Button(window1,text="Next",command=windowN2,bg="#ff9966",cursor='hand2')
    bt_1.place(x=340,y=130)
    window1.mainloop()

def printp():
    global p
    p=int(Pin_Field.get())


def windowN2():
    global window2
    window1.destroy()
    window2=Tk()
    window2.geometry("400x200")
    window2.configure(background='#ff9966')
    window2.title("Blood Bucket Affililated Hospital")
    la=Label(window2,text="Nearest Blood Bank/Centers to you\n***********************\nSelect your hospital ",fg="black",bg="#ff9966",font='5')
    la.place(x=67,y=30)
    def comboclick(event):
        global mycombo
        mycombo=my_combo.get()
    y=nearest(p)
    my_combo =ttk.Combobox(window2,value=y)
    my_combo.bind("<<ComboboxSelected>>",comboclick)
    my_combo.place(x=125,y=125) 
    bt=Button(window2,text="Donate",width=5,command=windowp11,bg="#ff9966",cursor='hand2')
    bt.place(x=150,y=150)
    bt=Button(window2,text="Request",width=5,command=windowp22,bg="#ff9966",cursor='hand2')
    bt.place(x=200,y=150)
    window2.mainloop()


def windowp11():
    global windowp1
    global bunit
    global Btype
    global bunits,btype
    global D
    window2.destroy()
    windowp1=Tk()
    windowp1.title("Entry No. OF Units")
    windowp1.geometry("500x250")
    windowp1.configure(background='#ff9966')
    greet = Label(windowp1, text = "Donate Blood\n*************\nEnter No. of Units:",fg="black",bg="#ff9966",font='5')
    greet.place(x=180,y=20)
    bunit=IntVar()
    bunits=Entry(windowp1,textvariable=bunit,width=20,font =('arial', 10))
    bunits.place(x=180,y=100)
    D='D'
    l3=Label(windowp1,text="Choose Blood Group",fg="black",bg="#ff9966",font='5')
    l3.place(x=170,y=130)
    Btype=StringVar()
    btype = Entry(windowp1,textvariable=Btype,width='5')
    btype.place(x=240, y=160)
    submit_btn=Button(windowp1,text="Submit",width=13,command=printd,bg="#ff9966",cursor='hand2')
    submit_btn.place(x=150,y=220)
    submitbtn=Button(windowp1,text="Next",width=13,command=windowNp2,bg="#ff9966",cursor='hand2')
    submitbtn.place(x=240,y=220)
    windowp1.mainloop()

def printd():
    global f,g
    f=bunits.get()
    g=btype.get()
    print(f,g)

def windowp22():
    global windowp2
    global blunit
    global bltype
    global bunits,btype
    global D
    window2.destroy()
    windowp2=Tk()
    windowp2.title("Entry No. OF Units")
    windowp2.geometry("500x250")
    windowp2.configure(background='#ff9966')
    greet = Label(windowp2, text = "Request Blood\n*************\nEnter No. of Units:",fg="black",bg="#ff9966",font='5')
    greet.place(x=180,y=20)
    blunit=IntVar()
    bunits=Entry(windowp2,textvariable=blunit,width=20,font =('arial', 10))
    bunits.place(x=180,y=100)
    l3=Label(windowp2,text="Choose Blood Group",fg="black",bg="#ff9966",font='5')
    l3.place(x=170,y=130)
    bltype=StringVar()
    btype = Entry(windowp2,textvariable=bltype,width='5')
    btype.place(x=240, y=160)
    D='R'
    submitbtn=Button(windowp2,text="Submit",width=16,command=printr,bg="#ff9966",cursor='hand2')
    submitbtn.place(x=150,y=220)
    submit=Button(windowp2,text="Next",width=13,command=windowNp3,bg="#ff9966",cursor='hand2')
    submit.place(x=240,y=220)
    windowp2.mainloop()

def printr():
    global f,g
    f=bunits.get()
    g=btype.get()
    print(f,g)

def windowNp3():
    windowp2.destroy()
    windowN3()
def windowNp2():
    windowp1.destroy()
    windowN3()

def windowN3():
    global window3
    global name
    global age
    global gender
    global phno
    global addr
    global Addr_field,Name_field,Age_field,Gender_field,PhNo_field
    window3=Tk()
    window3.title("Personal Deatils")
    window3.geometry("400x200")
    window3.configure(background='#ff9966')
    name=StringVar()
    age=StringVar()
    gender=StringVar()
    phno=StringVar()
    addr=StringVar()
    Name_title = Label(window3,text = "Name -->",fg="black",bg="#ff9966")
    Name_title.place(x=10,y=20)
    Name_field = Entry(window3,textvariable=name)
    Name_field.place(x=150,y=20)
    Age_title = Label(window3,text = "Age -->",fg="black",bg="#ff9966")
    Age_title.place(x=10,y=40)
    Age_field = Entry(window3,textvariable=age)
    Age_field.place(x=150,y=40)
    Gender_title = Label(window3,text = "Gender -->",fg="black",bg="#ff9966")
    Gender_title.place(x=10,y=60)
    Gender_field = Entry(window3,textvariable=gender)
    Gender_field.place(x=150,y=60)
    PhNo_title = Label(window3,text = "Phone Number -->",fg="black",bg="#ff9966")
    PhNo_title.place(x=10,y=80)
    PhNo_field = Entry(window3,textvariable=phno)
    PhNo_field.place(x=150,y=80)
    Addr_title = Label(window3,text = "Address -->",fg="black",bg="#ff9966")
    Addr_title.place(x=10,y=100)
    Addr_field = Entry(window3,textvariable=addr)
    Addr_field.place(x=150,y=100)
    Next_button = Button(window3,text= "Submit",width = 15, command =printit,bg="#ff9966",cursor='hand2')
    Next_button.place(x=150,y=150)
    Nxt_button=Button(window3,text= "Next",width = 15, command =windowN4,bg="#ff9966",cursor='hand2')
    Nxt_button.place(x=10,y=150)
    window3.mainloop()

def printit():
    global a,b,c,d,e
    a=Name_field.get()
    b=Age_field.get()
    c=Gender_field.get()
    d=PhNo_field.get()
    e=Addr_field.get()
    query="insert into person_info(pname,age,gender,`P.No`,address,Hospital_Name,`D/R`,requirement,units) values('{}','{}','{}',{},'{}','{}','{}','{}',{})".format(a,b,c,d,e,mycombo,D,g,f)
    cur.execute(query)
    con.commit()


def windowN4():
    global window4
    window3.destroy()
    window4=Tk()
    window4.title("Select Time Slot")
    window4.geometry("400x400")
    window4.configure(background='#ff9966') 
    l1=Label(window4 ,text =" Welcome To\n*****************\n{}".format(mycombo),fg="black",bg="#ff9966",font='5')
    l1.place(x=100,y=15)
    
    label1=Label(window4,text="Select Your Time slot",fg="black",bg="#ff9966",font='5')
    label1.place(x=115,y=110)
    #def sel():
    #    selection = " You selected the time slot " + str(time.get())
    #    label.config(text = selection,fg="black",bg="#ff9966")
    #time = StringVar()
    #R1 = Radiobutton(window4, text="9:00AM to 12:00PM ", variable=time, value="9:00AM to 12:00PM ",command=sel,fg="black",bg="#ff9966")
    #R1.place(x=70,y=135)
    #R2 = Radiobutton(window4, text="12:00PM to 3:00PM", variable=time, value="12:00PM to 3:00PM", command=sel,fg="black",bg="#ff9966")
    #R2.place(x=70,y=160)
    #R3 = Radiobutton(window4, text="3:00PM to 6:00PM", variable=time, value="3:00PM to 6:00PM", command=sel,fg="black",bg="#ff9966")
    #R3.place(x=70,y=190)
    def comboclick1(event):
        global mycombo1
        mycombo1=my_combo1.get()
    my_combo1 =ttk.Combobox(window4,value=["9:00AM to 12:00PM ","12:00PM to 3:00PM","3:00PM to 6:00PM"])
    my_combo1.bind("<<ComboboxSelected>>",comboclick1)
    my_combo1.place(x=120,y=160)
    label = Label(window4)
    label.place(x=65,y=230)
    finish_button = Button(window4,text="Finish",width=10,command=popup,fg="black",bg="#ff9966")
    finish_button.place(x=150,y=280)
    finish_button1 = Button(window4,text="Submit",width=10,command=input2,fg="black",bg="#ff9966")
    finish_button1.place(x=150,y=200)
    window4.mainloop()

def input2():
    cur.execute("update person_info set apt_time='{}' where `P.No`='{}'".format(mycombo1,d))
    con.commit()
    print(mycombo)
    print(mycombo1)
    query1="select {},{},{} from appointments where hospital_name='{}'".format("sum(9AMto12PM)","sum(12PMto3PM)","sum(3PMto6PM)",mycombo)
    query2="select {} from appointments where hospital_name='{}'"
    query3="insert into appointments(hospital_name,{}) values('{}',1)"
    if mycombo1=="9:00AM to 12:00PM ":
        cur.execute(query1)
        v=cur.fetchall()
        v=[int(i) for i in v[0] if i!=None]
        if v==[3,3,3]:
            messagebox.showinfo("Slots Filled!","Sorry,All slots are filled")
        else:
            query2=query2.format("sum(9AMto12PM)",mycombo)
            cur.execute(query2)
            v1=cur.fetchall()
            try:
                if int(v1[0][0])<3:
                    query3=query3.format("9AMto12PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
            except:
                if v1[0][0]==None:
                    query3=query3.format("9AMto12PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
    elif mycombo1=="12:00PM to 3:00PM":
        cur.execute(query1)
        v=cur.fetchall()
        v=[int(i) for i in v[0] if i!=None]
        if v==[3,3,3]:
            messagebox.showinfo("Slots Filled!","Sorry,All slots are filled")
        else:
            query2=query2.format("sum(12PMto3PM)",mycombo)
            cur.execute(query2)
            v1=cur.fetchall()
            try:
                if int(v1[0][0])<3:
                    query3=query3.format("12PMto3PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
            except:
                if v1[0][0]==None:
                    query3=query3.format("12PMto3PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
                
    else:
        cur.execute(query1)
        v=cur.fetchall()
        v=[int(i) for i in v[0] if i!=None]
        if v==[3,3,3]:
            messagebox.showinfo("Slots Filled!","Sorry,All slots are filled")
        else:
            query2=query2.format("sum(3PMto6PM)",mycombo)
            cur.execute(query2)
            v1=cur.fetchall()
            try:
                if int(v1[0][0])<3:
                    query3=query3.format("3PMto6PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
            except:
                if v1[0][0]==None:
                    query3=query3.format("3PMto6PM",mycombo)
                    cur.execute(query3)
                    con.commit()
                else:
                    messagebox.showinfo("Time Slot Filled!","Choose Another Time Slot")
def windowNq4():
    pop.destroy()
    windowN4()

def popup():
    global pop 
    window4.destroy()
    pop=Tk()
    pop.title("Details")
    pop.geometry("400x200")
    pop.configure(background='#ff9966') 
    cur.execute("select apt_time from person_info where `P.No`='{}'".format(d))
    v=cur.fetchall()
    print(v[0][0])
    if len(v)!=0:
        lablel5=Label(pop,text="Appointed accepted\nYour Appointment Time is: '{}'\nThank You For choosing Bloodbucket\n**********".format(v[0][0]),fg="black",bg="#ff9966")
        lablel5.place(x=85,y=10)
        a4 = Button(pop,text="Close",width="20",command=pop.destroy ,fg="black",bg="#ff9966")
        a4.place(x=120,y=130)

    #else:    
    #    label5=Label(pop,text="Appointment Declined.\n**************\nPlease change your timings",fg="black",bg="#ff9966")
    #    label5.place(x=135,y=10)
    #    r4 = Button(pop,text="Change time",width="20",command=windowNq4,fg="black",bg="#ff9966")
     #   r4.place(x=10,y=30)
     #   label6=Label(text="No time Available ,sorry",fg="black",bg="#ff9966")
     #   label6.place(x=50,y=50)
    pop.mainloop()


windown0()