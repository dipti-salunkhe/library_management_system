from tkinter import*
import time
import datetime
import sqlite3
import csv
from datetime import date
import matplotlib.pyplot as plt  
import numpy as np  
import matplotlib.pyplot as plt; plt.rcdefaults()
from PIL import Image, ImageTk


#----------------------------
def auth():
   
   main=Tk()
   main.title('Authentication Box')
   main.geometry('550x200')
   main.configure(background='orange')

   
    
   def clear_widget(event):
    
       
       if username_box == main.focus_get() and username_box.get() == 'Enter Username':
           username_box.delete(0, END)
       elif password_box == password_box.focus_get() and password_box.get() == '     ':
           password_box.delete(0, END)
    
   def repopulate_defaults(event):
    

       if username_box != main.focus_get() and username_box.get() == '':
           username_box.insert(0, 'Enter Username')
       elif password_box != main.focus_get() and password_box.get() == '':
           password_box.insert(0, '     ')
    
   def login(*event):
       flag=0
     
       usr=username_box.get()
       pwd=password_box.get()

       if usr=="admin" and pwd=="admin" :
           print('login success')
           flag=1
       else:
           print('login failed')    

       if flag==1:
           messagebox.showinfo("login successful","login successful")
       else:
           messagebox.showinfo("unsuccessful","login unsuccessful")
           exit()
       
       main.destroy()
    
   rows = 0
   while rows < 10:
       main.rowconfigure(rows, weight=1)
       main.columnconfigure(rows, weight=1)
       rows += 1
    
    
   username_box = Entry(main)
   username_box.insert(0, 'Enter Username')
   username_box.bind("<FocusIn>", clear_widget)
   username_box.bind('<FocusOut>', repopulate_defaults)
   username_box.grid(row=1, column=5, sticky='NS')
    
    
   # adds password entry widget and defines its properties
   password_box = Entry(main, show='*')
   password_box.insert(0, '     ')
   password_box.bind("<FocusIn>", clear_widget)
   password_box.bind('<FocusOut>', repopulate_defaults)
   password_box.bind('<Return>', login)
   password_box.grid(row=3, column=5, sticky='NS')
    
    
   # adds login button and defines its properties
   #login_btn = Button(main, text='Login', command=login)
   #login_btn.bind('<Return>', login)
   #login_btn.grid(row=5, column=5, sticky='NESW')
   b1=Button(main,text="LOGIN",bg="blue",fg="white",height=2,width=15,command=login).grid(row=6,column=5)

    
    
   main.mainloop()
#----------------------------------


#root.configure(background="black")

auth()
root=Tk()
root.geometry("1600x8000")
root.title("Department Library")

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("3.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


e = Example(root)
e.pack(fill=BOTH, expand=YES)


#--------------------------------------------------------------------------------------------------------------------------------
def databasei():

   global Fullname1 ,Roll1 ,Div1 ,Year1 ,Doiss1,Bid1 ,Bname1

   Fullname1=e1.get()
   Roll1=e2.get()
   Div1=e3.get()
   Year1=e4.get()
   Doiss1=e5.get()
   Bid1=e6.get()
   Bname1=e7.get()
   Date_of_return='00-00-0000'
   conn = sqlite3.connect('student1.db')
   c=conn.cursor()
   c.execute('''CREATE TABLE if not exists STUDENT(Fullname TEXT,Roll TEXT,Div TEXT,Year TEXT,Doiss Date,Bid TEXT,Bname TEXT)''')
   c.execute('''CREATE TABLE if not exists Records(Fullname TEXT,Roll TEXT,Div TEXT,Year TEXT,Date_of_issue Date,date_of_ret Date,Bid TEXT,Bname TEXT)''')
   c.execute('''INSERT INTO STUDENT(Fullname ,Roll ,Div ,Year ,Doiss,Bid ,Bname ) VALUES(?,?,?,?,?,?,?)''',(Fullname1 ,Roll1 ,Div1 ,Year1 ,Doiss1,Bid1 ,Bname1))
   c.execute('''INSERT INTO Records(Fullname ,Roll ,Div ,Year ,Date_of_issue ,date_of_ret,Bid ,Bname ) VALUES(?,?,?,?,?,?,?,?)''',(Fullname1 ,Roll1 ,Div1 ,Year1 ,Doiss1,Date_of_return,Bid1 ,Bname1))
   c.execute('''SELECT Fullname,Roll ,Div ,Year ,Doiss,Bid ,Bname from STUDENT''')
   conn.commit()
   print (c.fetchall())
    
#--------------------------------------------------------------------------------------------------------------------------------
def create1():

    
    global e1,e2,e3,e4,e5,e6,e7,t
    t=Toplevel() 
    t.title("ISSUE BOOKS")
    t.configure(background='cornsilk2')

    Label(t).grid(row=0)
    l1=Label(t,text="ISSUE BOOKS",bg='cornsilk2',fg="black")
    l1.place(relx=0.25, rely=0.03, anchor=CENTER)
    Label(t).grid(row=1)
    t.geometry("600x600")
    Label(t, text="FULLNAME ",bg='cornsilk2',fg="black").grid(row=2)
    Label(t,bg='cornsilk2').grid(row=3)
    Label(t, text="ROLL NO",bg='cornsilk2',fg="black").grid(row=4)
    Label(t,bg='cornsilk2').grid(row=5)
    Label(t, text="DIV",bg='cornsilk2',fg="black").grid(row=6)
    Label(t,bg='cornsilk2').grid(row=7)
    Label(t, text="YEAR",bg='cornsilk2',fg="black").grid(row=8)
    Label(t,bg='cornsilk2').grid(row=9)
    Label(t, text="DATE OF ISSUE",bg='cornsilk2',fg="black").grid(row=10)
    Label(t,bg='cornsilk2').grid(row=11)
    Label(t, text="BOOK ID",bg='cornsilk2',fg="black").grid(row=12)
    Label(t,bg='cornsilk2').grid(row=13)
    Label(t, text="BOOK NAME",bg='cornsilk2',fg="black").grid(row=14)
    Label(t,bg='cornsilk2').grid(row=15)

    e1=Entry(t)
    e2=Entry(t)
    e3=Entry(t)
    e4=Entry(t)
    e5=Entry(t)
    e6=Entry(t)
    e7=Entry(t)

    e1.grid(row=2, column=1)
    Label(t,bg='cornsilk2').grid(row=3)
    e2.grid(row=4, column=1)
    Label(t,bg='cornsilk2').grid(row=5)
    e3.grid(row=6, column=1)
    Label(t,bg='cornsilk2').grid(row=7)
    e4.grid(row=8, column=1)
    Label(t,bg='cornsilk2').grid(row=9)
    e5.grid(row=10, column=1)
    Label(t,bg='cornsilk2').grid(row=11)
    e6.grid(row=12, column=1)
    Label(t,bg='cornsilk2').grid(row=1)
    e7.grid(row=14, column=1)
    Label(t,bg='cornsilk2').grid(row=15)

    b1=Button(t,text="INSERT",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=databasei).grid(row=16,column=1)

    b2=Button(t,text="BACK",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=t.destroy).grid(row=16,column=2)

#------------------------------------------------------------------------------------------------------------------------

def databaser():

   global Fullname1 ,Roll1 ,Div1 ,Year1 ,Doret1,Bid1 ,Bname1

   Fullname1=e1.get()
   Roll1=e2.get()
   Div1=e3.get()
   Year1=e4.get()
   Date_of_return=e5.get()
   Bid1=e6.get()
   Bname1=e7.get()
   Date_of_issue='00-00-0000'

   conn = sqlite3.connect('student1.db')
   c=conn.cursor()
   c.execute('''delete from STUDENT where Roll=? and Year=?''',(Roll1,Year1,))
   c.execute('''INSERT INTO Records(Fullname ,Roll ,Div ,Year ,Date_of_issue ,date_of_ret,Bid ,Bname ) VALUES(?,?,?,?,?,?,?,?)''',(Fullname1 ,Roll1 ,Div1 ,Year1 ,Date_of_issue,Date_of_return,Bid1 ,Bname1))

   conn.commit()
   print (c.fetchall())
#--------------------------------------------------------------------------------------------------------------------------------
def create2():
    global e1,e2,e3,e4,e5,e6,e7,t

    t=Toplevel()
    t.title("RETURN BOOKS")
    t.configure(background='cornsilk2')
    Label(t).grid(row=0)
    l1=Label(t,text="RETURN BOOKS",bg='cornsilk2',fg="black")
    l1.place(relx=0.25, rely=0.03, anchor=CENTER)
    Label(t).grid(row=1)
    t.geometry("600x600")
    Label(t, text="FULLNAME ",bg='cornsilk2',fg="black").grid(row=2)
    Label(t,bg='cornsilk2').grid(row=3)
    Label(t, text="ROLL NO",bg='cornsilk2',fg="black").grid(row=4)
    Label(t,bg='cornsilk2').grid(row=5)
    Label(t, text="DIV",bg='cornsilk2',fg="black").grid(row=6)
    Label(t,bg='cornsilk2').grid(row=7)
    Label(t, text="YEAR",bg='cornsilk2',fg="black").grid(row=8)
    Label(t,bg='cornsilk2').grid(row=9)
    Label(t, text="DATE OF RETURN",bg='cornsilk2',fg="black").grid(row=10)
    Label(t,bg='cornsilk2').grid(row=11)
    Label(t, text="BOOK ID",bg='cornsilk2',fg="black").grid(row=12)
    Label(t,bg='cornsilk2').grid(row=13)
    Label(t, text="BOOK NAME",bg='cornsilk2',fg="black").grid(row=14)
    Label(t,bg='cornsilk2').grid(row=15)

    e1=Entry(t)
    e2=Entry(t)
    e3=Entry(t)
    e4=Entry(t)
    e5=Entry(t)
    e6=Entry(t)
    e7=Entry(t)

    e1.grid(row=2, column=1)
    Label(t,bg='cornsilk2').grid(row=3)
    e2.grid(row=4, column=1)
    Label(t,bg='cornsilk2').grid(row=5)
    e3.grid(row=6, column=1)
    Label(t,bg='cornsilk2').grid(row=7)
    e4.grid(row=8, column=1)
    Label(t,bg='cornsilk2').grid(row=9)
    e5.grid(row=10, column=1)
    Label(t,bg='cornsilk2').grid(row=11)
    e6.grid(row=12, column=1)
    Label(t,bg='cornsilk2').grid(row=1)
    e7.grid(row=14, column=1)
    Label(t,bg='cornsilk2').grid(row=15)

    b1=Button(t,text="RETURN",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=databaser).grid(row=16,column=1)

    b2=Button(t,text="BACK",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=t.destroy).grid(row=16,column=2)
#----------------------------------------------------------------------------------------------------------------------
def csvfile():

	conn=sqlite3.connect("student1.db")
	c=conn.cursor()
	conn.row_factory=sqlite3.Row
	crsr=conn.execute("SELECT * From Records")
	row=crsr.fetchone()
	titles=row.keys()

	data = c.execute("SELECT * FROM Records")
	if sys.version_info < (3,):
	    f = open('RECORD.csv', 'wb')
	else:
	    f = open('RECORD.csv', 'w', newline="")

	writer = csv.writer(f,delimiter=';')
	writer.writerow(titles)
        # keys=title you're looking for
	# write the rest
	writer.writerows(data)
	f.close()
       
#----------------------------------------------------------------------------------------------------------------------------
def INSERT_BOOK():
   global Bid2 ,Bname2,author,publication,date_of_entry,no_of_copies,price

   Bid2 =e1.get()
   Bname2=e2.get()
   author=e3.get()
   publication=e4.get()
   date_of_entry=e5.get()
   no_of_copies=e6.get()
   price=e7.get()
   conn = sqlite3.connect('student1.db')
   c=conn.cursor()
   c.execute('''CREATE TABLE if not exists Book_Entries(Bid TEXT ,Bname TEXT,Author TEXT,publication text,Date_of_entry DATE,No_of_copies TEXT,price real)''')

   c.execute('''INSERT INTO Book_Entries(Bid ,Bname,author,publication,Date_of_entry,No_of_copies,price  ) VALUES(?,?,?,?,?,?,?)''',(Bid2 ,Bname2,author,publication,date_of_entry,no_of_copies,price))

   print("Second time")
   c.execute('''SELECT * from Book_Entries''')
   conn.commit()
   print (c.fetchall())
#---------------------------------------------------
   
#--------------------------------------------------------------------------------------------------------------------------
def add_books():
    global e1,e2,e3,e4,e5,e6,e7,t

    t=Toplevel()
    t.title("BOOKS DETAILS")
    t.configure(background='cornsilk2')
    Label(t).grid(row=0)
    l1=Label(t,text="",bg='cornsilk2',fg="black")
    l1.place(relx=0.25, rely=0.03, anchor=CENTER)
    Label(t).grid(row=1)
    t.geometry("600x600")
    Label(t, text="BOOKID",bg='cornsilk2',fg="black").grid(row=2)
    Label(t,bg='cornsilk2').grid(row=3)
    Label(t, text="BOOKNAME ",bg='cornsilk2',fg="black").grid(row=4)
    Label(t,bg='cornsilk2').grid(row=5)
    Label(t, text="AUTHOR NAME ",bg='cornsilk2',fg="black").grid(row=6)
    Label(t,bg='cornsilk2').grid(row=7)
    Label(t, text="SUBJECT ",bg='cornsilk2',fg="black").grid(row=8)
    Label(t,bg='cornsilk2').grid(row=9)
    
    Label(t, text="DATE OF ENTRY",bg='cornsilk2',fg="black").grid(row=10)
    Label(t,bg='cornsilk2').grid(row=11)
    Label(t, text="NO OF COPIES",bg='cornsilk2',fg="black").grid(row=12)
    Label(t,bg='cornsilk2').grid(row=13)
    Label(t, text="PRICE",bg='cornsilk2',fg="black").grid(row=14)
    Label(t,bg='cornsilk2').grid(row=15)


    e1=Entry(t)
    e2=Entry(t)
    e3=Entry(t)
    e4=Entry(t)
    e5=Entry(t)
    e6=Entry(t)
    e7=Entry(t)

    e1.grid(row=2, column=1)
    Label(t,bg='cornsilk2').grid(row=3)
    e2.grid(row=4, column=1)
    Label(t,bg='cornsilk2').grid(row=5)
    e3.grid(row=6, column=1)
    Label(t,bg='cornsilk2').grid(row=7)
    e4.grid(row=8, column=1)
    Label(t,bg='cornsilk2').grid(row=9)
    e5.grid(row=10, column=1)
    Label(t,bg='cornsilk2').grid(row=11)
    e6.grid(row=12, column=1)
    Label(t,bg='cornsilk2').grid(row=13)
    e7.grid(row=14, column=1)
    Label(t,bg='cornsilk2').grid(row=15)

    b1=Button(t,text="INSERT",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=INSERT_BOOK).grid(row=16,column=1)

    b2=Button(t,text="BACK",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=t.destroy).grid(row=16,column=2)

#-----------------------------------------------------------------------		
def DELETE_BOOK():
   global No_of_copies,Bid3 ,Bname3,author,publication,price

   Bid3 =e1.get()
   Bname3=e2.get()
   author=e3.get()
   publication=e4.get()
   No_of_copies=e5.get()
   print(type(No_of_copies))
   No_of_copies=int(No_of_copies)
   print(type(No_of_copies))
   conn = sqlite3.connect('student1.db')
   c=conn.cursor()
   cr=c.execute('''SELECT * from Book_Entries''')
   for row in cr:
        if row[0]==Bid3:
	        #print(row[5])
                a=row[5] 
                print(a)
                print(type(a))
                a=int(a)
                print(type(a))
   if(a==No_of_copies):
        c.execute('''DELETE from Book_Entries where Bid=? and Bname=?''',(Bid3 ,Bname3,))
        conn.commit()
        print("executed successfully")
        c.execute('''SELECT * from Book_Entries''')

   elif(a>(No_of_copies)):
       (a)=(a)-(No_of_copies)
       c.execute('''UPDATE Book_Entries SET  No_of_copies= ? WHERE Bid = ? ''',(a,Bid3,)) 
       conn.commit()
       c.execute('''SELECT * from Book_Entries''')
       print("Updated Successfully")      

   else:
       print("Enter correct number of books")

   conn.commit()
   #cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',(newphone, userid)) 
   # Delete user with id 2
   #delete_userid = 2
   #cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
   #print(anoe)
   #c.execute('''DELETE from Book_Entries where Bid=? and Bname=?''',(Bid3 ,Bname3,))
   #c.execute('''INSERT INTO Book_Entries(No_of_copies) VALUES(?)''',(No_of_copies))
   #c.execute('''SELECT * from Book_Entries''')
   #print (c.fetchall())

#--------------------------------------------------------------------------------------------------------------------------
def remove_books():
    global e1,e2,e3,e4,e5,e6,e7,t

    t=Toplevel()
    t.title("REMOVING BOOKS")
    t.configure(background='cornsilk2')
    Label(t).grid(row=0)
    l1=Label(t,text="",bg='cornsilk2',fg="black")
    l1.place(relx=0.25, rely=0.03, anchor=CENTER)
    Label(t).grid(row=1)
    t.geometry("600x600")
    Label(t, text="BOOKID",bg='cornsilk2',fg="black").grid(row=2)
    Label(t,bg='cornsilk2').grid(row=3)
    Label(t, text="BOOKNAME ",bg='cornsilk2',fg="black").grid(row=4)
    Label(t,bg='cornsilk2').grid(row=5)
    Label(t, text="AUTHOR NAME ",bg='cornsilk2',fg="black").grid(row=6)
    Label(t,bg='cornsilk2').grid(row=7)
    Label(t, text="PUBLICATION ",bg='cornsilk2',fg="black").grid(row=8)
    Label(t,bg='cornsilk2').grid(row=9)
    Label(t, text="No.OF COPIES",bg='cornsilk2',fg="black").grid(row=10)
    Label(t,bg='cornsilk2').grid(row=11)


    e1=Entry(t)
    e2=Entry(t)
    e3=Entry(t)
    e4=Entry(t)
    e5=Entry(t)

    e1.grid(row=2, column=1)
    Label(t,bg='cornsilk2').grid(row=3)
    e2.grid(row=4, column=1)
    Label(t,bg='cornsilk2').grid(row=5)
    e3.grid(row=6, column=1)
    Label(t,bg='cornsilk2').grid(row=7)
    e4.grid(row=8, column=1)
    Label(t,bg='cornsilk2').grid(row=9)
    e5.grid(row=10, column=1)
    Label(t,bg='cornsilk2').grid(row=11)

    b1=Button(t,text="REMOVE",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=DELETE_BOOK).grid(row=12,column=1)

    b2=Button(t,text="BACK",bg="BLACK",fg="CORNSILK3",height=2,width=15,command=t.destroy).grid(row=12,column=2)
#--------------------------------------------------------------------------------------------------

def all():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

    cnt1=0
    cnt2=0
    cnt3=0


    cursor = conn.execute("SELECT * from Records")

    for row in cursor:
       if row[3]=='SE' and row[5]=='00-00-0000':
          cnt1=cnt1+1;
       elif row[3]=='TE' and row[5]=='00-00-0000':
          cnt2=cnt2+1;
       elif row[3]=='BE' and row[5]=='00-00-0000':
          cnt3=cnt3+1;
      

    print ("Operation done successfully")
    print(cnt1)
    print(cnt2)
    print(cnt3)


    # x-coordinates of left sides of bars  
    left = [1, 2, 3] 
      
    # heights of bars i.e. y axis points 
    height = [cnt1,cnt2,cnt3] 
      
    # labels for bars 
    classes = ['SE', 'TE', 'BE'] 
    x_pos=np.arange(len(classes))
      
    # plotting a bar chart 
    plt.bar(x_pos,height,width = 0.8,align='center',color = ['red', 'green','k'] ) 
    plt.xticks(x_pos,classes)
      
    # naming the x-axis 
    plt.xlabel('year') 
    # naming the y-axis 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('Overall') 
      
    # function to show the plot 
    plt.show() 
    conn.close()
#-------------------------------------------------------------------------------------------------
def SEall():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

    cnt1=0
    cnt2=0
    cnt3=0


    cursor = conn.execute("SELECT * from Records")

    for row in cursor:
       if row[2]=='A' and row[3]=='SE'  and row[5]=='00-00-0000':
          cnt1=cnt1+1;
       elif row[2]=='B' and row[3]=='SE'  and row[5]=='00-00-0000':
          cnt2=cnt2+1;
       elif  row[2]=='C' and row[3]=='SE'  and row[5]=='00-00-0000':
          cnt3=cnt3+1;
      

    print ("Operation done successfully")
    print(cnt1)
    print(cnt2)
    print(cnt3)


    # x-coordinates of left sides of bars  
    left = [1, 2, 3] 
      
    # heights of bars i.e. y axis points 
    height = [cnt1,cnt2,cnt3] 
      
    # labels for bars 
    classes = ['A', 'B', 'C'] 
    x_pos=np.arange(len(classes))
      
    # plotting a bar chart 
    plt.bar(x_pos,height,align='center',alpha=0.4,color = ['red', 'green','k'])  
    plt.xticks(x_pos,classes)
     
    # naming the x-axis 
    plt.xlabel('DIVISION') 
    # naming the y-axis 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('UTILIZATION BY SE') 
    
    # function to show the plot 
    plt.show() 
    conn.close()
#-----------------------------------------------------------------------------

def prize():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

   

    x=[]
    y=[]
    cursor = conn.execute("SELECT  publication from Book_Entries")
    #c.execute('''CREATE TABLE if not exists Book_Entries(Bid TEXT ,Bname TEXT,Author TEXT,publication text,Date_of_entry DATE,No_of_copies TEXT,price real)''')
    cursor1 = conn.execute("SELECT  price from Book_Entries")
   
    for row in cursor:
       x.append(row[0])
      
    for row in cursor1:
       y.append(row[0])


    # x-coordinates of left sides of bars  
    
      
    # heights of bars i.e. y axis points 
     
      
    # labels for bars 
 
    
      
    # plotting a bar chart 
    plt.bar(x,cursor1,align='center',alpha=0.4) 
    #plt.xticks(x_pos,classes)
     
    # naming the x-axis 
    plt.xlabel('Books') 
    # naming the y-axis 
    plt.ylabel('Price') 
    # plot title 
    plt.title('Range of books') 
    
    # function to show the plot 
    plt.show() 
    conn.close()
#---------------------------------------------------------------------------------------------------


def TEall():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

    cnt1=0
    cnt2=0
    cnt3=0


    cursor = conn.execute("SELECT * from Records")

    for row in cursor:
       if row[2]=='A' and row[3]=='TE'  and row[5]=='00-00-0000':
          cnt1=cnt1+1;
       elif row[2]=='B' and row[3]=='TE'  and row[5]=='00-00-0000':
          cnt2=cnt2+1;
       elif  row[2]=='C' and row[3]=='TE'  and row[5]=='00-00-0000':
          cnt3=cnt3+1;
      

    print ("Operation done successfully")
    print(cnt1)
    print(cnt2)
    print(cnt3)


    # x-coordinates of left sides of bars  
    left = [1, 2, 3] 
      
    # heights of bars i.e. y axis points 
    height = [cnt1,cnt2,cnt3] 
      
    # labels for bars 
    classes = ['A', 'B', 'C'] 
    x_pos=np.arange(len(classes))
      
    # plotting a bar chart 
    plt.bar(x_pos,height,align='center',alpha=0.8) 
    plt.xticks(x_pos,classes)
     
    # naming the x-axis 
    plt.xlabel('DIVISION') 
    # naming the y-axis 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('UTILIZATION BY TE') 
    
    # function to show the plot 
    plt.show() 
    conn.close()
#----------------------------------------------------------------------------------------------------


def BEall():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

    cnt1=0
    cnt2=0
    cnt3=0


    cursor = conn.execute("SELECT * from Records")

    for row in cursor:
       if row[2]=='A' and row[3]=='BE'  and row[5]=='00-00-0000':
          cnt1=cnt1+1;
       elif row[2]=='B' and row[3]=='BE'  and row[5]=='00-00-0000':
          cnt2=cnt2+1;
       elif  row[2]=='C' and row[3]=='BE'  and row[5]=='00-00-0000':
          cnt3=cnt3+1;
      

    print ("Operation done successfully")
    print(cnt1)
    print(cnt2)
    print(cnt3)


    # x-coordinates of left sides of bars  
    left = [1, 2, 3] 
      
    # heights of bars i.e. y axis points 
    height = [cnt1,cnt2,cnt3] 
      
    # labels for bars 
    classes = ['A', 'B', 'C'] 
    x_pos=np.arange(len(classes))
      
    # plotting a bar chart 
    x=plt.bar(x_pos,height,align='center',alpha=0.8,color = ['red', 'green','y'])
    
    plt.xticks(x_pos,classes)
     
    # naming the x-axis 
    plt.xlabel('DIVISION') 
    # naming the y-axis 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('UTILIZATION BY BE') 
    
    # function to show the plot 
    plt.show() 
    conn.close()

#-------------------------------------------------------------------------------------------------
def piechart():
    conn = sqlite3.connect('student1.db')


    print ("Opened database successfully")
    cnt=0
    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0
    cnt5=0
    cnt6=0
    cnt7=0
    cnt8=0
    cnt9=0
    cnt10=0
    cnt11=0
    cnt12=0
    cnt13=0
    cnt14=0

    cursor = conn.execute("SELECT publication from Book_Entries")

    for row in cursor:
                 if row[0]=='sepm':
                    cnt=cnt+1;
                 elif row[0]=='toc':
                    cnt1=cnt1+1;
                 elif row[0]=='dell':
                     cnt2=cnt2+1;
                 elif row[0]=='m3':
                      cnt3=cnt3+1;
                 elif row[0]=='hcd':
                      cnt4=cnt4+1;
                 elif row[0]=='iot':
                         cnt5=cnt5+1;
                 elif row[0]=='java':
                    cnt6=cnt6+1;
                 elif row[0]=='cpp':
                     cnt7=cnt7+1;
                 elif row[0]=='isee':
                       cnt8=cnt8+1;
                 elif row[0]=='mp':
                       cnt9=cnt9+1;
                 elif row[0]=='coa':
                      cnt10=cnt10+1;
                 elif row[0]=='php':
                      cnt11=cnt11+1;
                 elif row[0]=='daa':
                      cnt12=cnt12+1;
                 elif row[0]=='dbms':
                      cnt13=cnt13+1;
                 else:
                     cnt14=cnt14+1;
    print ("Operation done successfully")



    labels = 'SEPM', 'TOC','DELD','M3','HCD','IOT','JAVA','C++','ISEE','MP','COA','PHP','DAA','DBMS'
    sizes = [cnt,cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8,cnt9,cnt10,cnt11,cnt12,cnt13]
    print(type(sizes))
    explode = (0, 0.1, 0, 0,0,0,0,0,0,0,0,0,0,0)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show() 

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------    
def create3():

    t=Toplevel()
    t.title("REPORTS")
    t.configure(background='light cyan')
    t.geometry("500x500")
    Button(t,text="Add books in record",bg="grey",fg="CORNSILK2",height=2,width=15,command=add_books).place(x=100,y=100)
    Button(t,text="Remove books from record",bg="grey",fg="CORNSILK2",height=2,width=15,command=remove_books).place(x=300,y=100)
    Button(t,text="Overall Utilization",bg="grey",fg="CORNSILK2",height=2,width=15,command=all).place(x=100,y=200)
    Button(t,text="Utilized by SE",bg="grey",fg="CORNSILK2",height=2,width=15,command=SEall).place(x=300,y=200)
    Button(t,text="Utilized by TE",bg="grey",fg="CORNSILK2",height=2,width=15,command=TEall).place(x=100,y=300)
    Button(t,text="Utilized by BE",bg="grey",fg="CORNSILK2",height=2,width=15,command=BEall).place(x=300,y=300)
#    Button(t,text="Usability",bg="grey",fg="CORNSILK2",height=2,width=15,command=add_books).place(x=100,y=400)
    Button(t,text="No of copies",bg="grey",fg="CORNSILK2",height=2,width=15,command=piechart).place(x=200,y=400)
    #Button(t,text="Price",bg="grey",fg="CORNSILK2",height=2,width=15,command=prize).place(x=300,y=400)
Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)


b=Button(root,padx=16,pady=10,bd=20,fg="black",font=('arial',16,'bold'),width=30,text="Department Library",bg="pale goldenrod")
b.place(x=450,y=40)
#--------------------------------------------------------------------------

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=400,height=700,bg="pale turquoise",relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=400, height=700,bg="pale turquoise", relief=SUNKEN,pady=10)
f2.pack(side=RIGHT)

b=Button(root,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Issue Book",bg="plum1",command=create1)
b.place(x=50,y=400)
#----------------------------------------------------------

b=Button(root,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Return Book",bg="plum1",command=create2)
b.place(x=550,y=400)

b=Button(root,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Report",bg="plum1",command=create3)
b.place(x=1050,y=400)

root.mainloop()


