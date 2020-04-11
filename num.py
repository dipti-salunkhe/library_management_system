

import matplotlib.pyplot as plt
import sqlite3
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
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




'''
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()def all():

    conn = sqlite3.connect('student1.db')
    print ("Opened database successfully")

    cnt1=0
    cnt2=0
    cnt3=0


    cursor = conn.execute("SELECT * from Records")

    for row in cursor:
       if row[3]=='SE':
          cnt1=cnt1+1;
       elif row[3]=='TE':
          cnt2=cnt2+1;
       else:
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
    tick_label = ['SE', 'TE', 'BE'] 
      
    # plotting a bar chart 
    plt.bar(left, height, tick_label = tick_label, 
            width = 0.8, color = ['red', 'green','k']) 
      
    # naming the x-axis 
    plt.xlabel('year') 
    # naming the y-axis 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('Overall') 
      
    # function to show the plot 
    plt.show() 
    conn.close()
'''
