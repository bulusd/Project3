from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import calendar
from ListRequest import ListTicket
from DbConnect import DBConnect


dbConnect=DBConnect()
root = Tk()
root.title('scheduler')
root.geometry("600x600")
root.configure(background='#49A')
style=ttk.Style()
style.configure('TLabel', background='#49A')

# full name
ttk.Label(root, text="Full Name:").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root, width=30, font=('Arial',16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)
# phone number
ttk.Label(root, text="Phone Number:").grid(row=1,column=0,padx=10,pady=10)
EntryPhone=ttk.Entry(root, width=30, font=('Arial',16))
EntryPhone.grid(row=1, column=1, columnspan=2, pady=10)
# age
ttk.Label(root, text="Age:").grid(row=2,column=0,padx=10,pady=10)
EntryAge=ttk.Entry(root, width=30, font=('Arial',16))
EntryAge.grid(row=2, column=1, columnspan=2, pady=10)
# date pick
# Add Calender
cal = Calendar(root, selectmode = 'day',
               year = 2021, month = 5,
               day = 23)
cal.grid(row=3, column=1, columnspan=1, pady=20)
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
# Comment box
ttk.Label(root, text="Comments:").grid(row=4, column=0)
txtComments=Text(root, width=50, height= 5, font=('Arial',16))
txtComments.grid(row=4,column=1, columnspan=2)
#Buttons
buSubmit=ttk.Button(root,text="Submit Appointment")
buSubmit.grid(row=7,column=1)
buList=ttk.Button(root,text="List Res.")
buList.grid(row=7, column=2)

def BuSaveData():
	msg=dbConnect.Add(EntryFullName.get(),EntryPhone.get(),EntryAge.get(),cal.get_date(),txtComments.get(1.0,'end'))
	messagebox.showinfo(title="Add info",message=msg)
	EntryFullName.delete(0,'end')
	txtComments.delete(1.0,'end')

def BuListData():
	listrequest=ListTicket()

buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)

root.mainloop()

