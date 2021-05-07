from tkinter import *
from tkinter import ttk 
from DbConnect import DBConnect
dbConnect=DBConnect()

class ListTicket:	
	 def __init__(self):
	    self._root=Tk()
	    self._dbconnect=DBConnect()
	    tv=ttk.Treeview(self._root)
	    tv.pack()
	    tv.heading('#0',text='ID')
	    tv.configure(column=('#Name','#Phone','#Age','#Date','#Comment'))
	    tv.heading('#Name',text='Name')
	    tv.heading('#Phone',text='Phone')
	    tv.heading('#Age',text='Age')
	    tv.heading('#Date',text='Date')
	    tv.heading('#Comment',text='Comment')
	    cursor=self.dbconnect.ListRequest()
	    for row in cursor:
	    	tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
	    	tv.set('#{}'.format(row['ID']),'#Name', row['Name'])
	    	tv.set('#{}'.format(row['ID']),'#Phone', row['Phone'])
	    	tv.set('#{}'.format(row['ID']),'#Age', row['Age'])
	    	tv.set('#{}'.format(row['ID']),'#Date', row['Date'])
	    	tv.set('#{}'.format(row['ID']),'#Comment', row['Comment'])

	    self._root.mainloop()