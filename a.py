
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
    plt.bar(x,y,align='center',alpha=0.4) 
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
