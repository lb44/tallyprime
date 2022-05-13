from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
# from tkcalendar import DateEntry,Calender
root=Tk()
root.geometry("1860x900")
root.resizable(True, True)

root.title("TALLY PRIME")


curnt_period = Label(root, text="CURRENT PERIOD",fg="darkblue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="darkblue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-2023", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",borderwidth=3,fg="darkblue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry", fg="darkblue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22",fg="black").place(x=340, y=140)
frame = Label(root, text="Accounts Book",bg="grey",fg="white",width=40,padx=20,pady=10).place(x=740, y=110)
frame1 = Frame(root, bg="lightblue", width=305, height=540)
frame1.place(x=740, y=145)
frame2 = Frame(frame1, bg="lightblue", width=305, height=540)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Summary",bg="lightblue",fg="black",font="17").place(x=850,y=190)


def func1():
    screen1 = Toplevel(root)
    screen1.title('create')
    screen1.geometry('1860x900') 

def func3():     
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('contra register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='CONTRA REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func4():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('payment register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='PAYMENT REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func5():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('receipt register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='RECEIPT REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()    
def func6():     
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('sales register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='SALES REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func7():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('purchase register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='PURCHASE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func8():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('journal register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='JOURNAL REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()    
def func9():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('debit note register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='DEBIT NOTE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func10():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('credit note register')
    screen2.geometry('1500x770')
    sbmibtn = Button(screen2, text='APRIL',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    Label(screen2, text='CREDIT NOTE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      

b1 = Button(root, text="Cash/Bank Book(s)", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func1).place(x=830, y=230)

b2 = Button(root, text="Ledger", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func1).place(x=830, y=260)
b3 = Button(root, text="Group summary", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func1).place(x=830, y=290)
b4 = Button(root, text="Group Vouchers",fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func1).place(x=830, y=320)
mstrs1 = Label(root, text="Registers",bg="lightblue",fg="black",font="13").place(x=850,y=355)

b6 = Button(root, text="ConTra Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func3).place(x=830, y=390)
b7 = Button(root, text="Payment Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func4).place(x=830, y=420)


b8 = Button(root, text="Reciept Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func5).place(x=830, y=450)
b9 = Button(root, text="Sales Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func6).place(x=830, y=500)
b10 = Button(root, text="Purchase Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func7).place(x=830, y=530)

b10 = Button(root, text="Journal Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func8).place(x=830, y=580)
b11 = Button(root, text="Debit Note Register", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func9).place(x=830, y=610)

b12 = Button(root, text="Credit Note Register", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func10).place(x=830, y=640)

             
b13 = Button(root, text="Quit", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func1).place(x=830, y=670)
             
frame3 = Frame(root, bg="lightblue", width=140, height=790)
frame3.place(x=1400, y=0)
date = Button(frame3, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), command=func1, activebackground="palegreen", activeforeground="red")
date.place(x=13, y=20)


def func2():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('Company')
    screen2.geometry('700x430')
    Label(screen2, text='List Of Companies',bg="blue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(screen2, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=240,y=40)
    sbmibtn2 = Button(screen2, text='Alter Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=240,y=70)
    sbmibtn3 = Button(screen2, text='Select Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=240,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(x=240, y=130)


def create():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('Create Company')
    screen3.geometry('940x520')
    Label(screen3, text='COMPANY CREATION',bg="navyblue",font='15',fg="white",width=640).pack()
    global  Cname,Cmailing,Caddress, email,state,country,pcode,tphone,mphone,fax,site,symbol,format
    Cname = StringVar()
    Cmailing = StringVar()
    Caddress = StringVar()
    email = StringVar()
    state = StringVar()
    country = StringVar()
    pcode = IntVar()
    tphone = StringVar()
    mphone = StringVar()
    fax = StringVar()
    site = StringVar()
    symbol = StringVar()
    format = StringVar()
    
    
    cname = Label(screen3, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen3, textvariable=Cname,width=40).place(x=120, y=70)
    y1 = Label(screen3, text='Financial Year begining From:').place(x=450, y=70)
    # e2 = DateEntry(screen3,width=25)
    adrs1 = Label(screen3, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen3, textvariable=Cmailing, width=40).place(x=120, y=110)
    y2 = Label(screen3, text='Books Begining From:').place(x=450, y=110)
    adrs = Label(screen3, text='Address:').place(x=20, y=150)
    e4 = Entry(screen3,textvariable=Caddress,width=40).place(x=120, y=150)
    
company = Button(frame3, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), command=func2, activebackground="palegreen", activeforeground="red").place(x=13, y=50)

root.mainloop()


