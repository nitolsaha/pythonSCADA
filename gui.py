# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
import os
import matplotlib
import OpenOPC
import datetime, threading, time
import mysql.connector
from  datetime import  datetime


from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use("ggplot")


fig = Figure(figsize=(8,2), dpi=100)
a = fig.add_subplot(111)


class SCADA_GUI_LOGIN:

    def __init__(self,master):
        self.master=master
        self.master.geometry("520x300")
#row1

        self.label1 = Label(master, height=3, width=20, text= "INDUSTRIAL SCADA SYSTEM")
        self.label1.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)
        self.label1.config(font=("Arial", 15))

        #row two
        self.label2 = Label(master, height=3, width=20)
        self.label2.grid(row=1, column=0, sticky=N + S + E + W)

        self.label3 = Label(master, height=3, width=20)
        self.label3.grid(row=1, column=3, sticky=N + S + E + W)
#row 3
        self.label4 = Label(master, height=3, width=20)
        self.label4.grid(row=2, column=0, sticky=N + S + E + W)

        self.label5 = Label(master, height=3, width=20)
        self.label5.grid(row=2, column=3, sticky=N + S + E + W)

#row 4
        self.label6 = Label(master, height=3, width=20)
        self.label6.grid(row=3, column=0,columnspan=2, sticky=N + S + E + W)


        self.label7 = Label(master,height=3, width=20)
        self.label7.grid(row=3, column=3, sticky=N + S + E + W)
#row 5
        self.label8 = Label(master, height=3, width=20)
        self.label8.grid(row=4, column=0, columnspan=4, sticky=N + S + E + W)

#Labels
        self.labelUserName = Label(master, text= "USER NAME")
        self.labelUserName.grid(row=1, column= 1)

        self.entryUserName = Entry(master)
        self.entryUserName.grid(row=1, column= 2)
        self.entryUserName.config(font=("Arial", 8))

        self.labelPassword = Label(master, text= "PASSWORD")
        self.labelPassword.grid(row=2, column= 1)

        self.entryPassword = Entry(master, show='*')
        self.entryPassword.grid(row=2, column= 2)

        self.loginButton = Button(master, text= "LOGIN", command= self.loginwindow, height= 1, width= 15)
        self.loginButton.grid(row=3, column=2)


    def loginwindow(self):
        u=self.entryUserName.get()
        p=self.entryPassword.get()
        f=open('admin_list.txt','r')
        f.close()
        f = open('admin_password.txt', 'r')
        f.close()
        with open('admin_list.txt') as f:
            main_admin = (f.read().strip(' ')).split(' ')
            print(main_admin)
        with open('admin_password.txt') as f:
            main_admin_pass = (f.read().strip(' ')).split(' ')
            print(main_admin_pass)
        if u in main_admin:
            index_admin= main_admin.index(u)
            if main_admin_pass[index_admin]==p:
                self.master.destroy()
                root1=Tk()
                SCADA_OPTION(root1)
                root1.mainloop()
        else:
            root3=Tk()
            labelInvalidEntry = Label(root3, text="Invalid Entry")
            labelInvalidEntry.grid(row=0, column=0)
            root3.mainloop()


#Option Menu for SCADA0


class SCADA_OPTION:
    def __init__(self,master):
        self.master=master
        self.master.geometry("520x300")

        self.label1 = Label(master, height=1, width=20)
        self.label1.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)

        self.adduserButton = Button(master, text="ADD USER", command=self.add_user, height=1, width=30)
        self.adduserButton.grid(row=1, column=1, columnspan=2, sticky=N + S + E + W)

        self.label3 = Label(master, height=1, width=20)
        self.label3.grid(row=2, column=0, columnspan=4, sticky=N + S + E + W)

        self.monitoringviewButton = Button(master, text= "MONITORING VIEW", command= self.monitoring_view)
        self.monitoringviewButton.grid(row=3, column=1, columnspan=2, sticky=N + S + E + W)

        self.label4 = Label(master, height=1, width=20)
        self.label4.grid(row=4, column=0, columnspan=4, sticky=N + S + E + W)

        self.graphviewButton = Button(master, text= "GRAPH VIEW", command= self.graph_view)
        self.graphviewButton.grid(row=5, column=1, columnspan=2, sticky=N + S + E + W)

        self.label5 = Label(master, height=1, width=20)
        self.label5.grid(row=6, column=0, sticky=N + S + E + W)

        self.parametersetButton = Button(master, text= "PARAMETER SETTING", command= self.parameter_setting)
        self.parametersetButton.grid(row=7, column=1, columnspan=2, sticky=N + S + E + W)

        self.label6 = Label(master, height=1, width=20)
        self.label6.grid(row=8, column=0, columnspan=4, sticky=N + S + E + W)

        self.dataprintButton = Button(master, text= "TREND DATA PRINT", command= self.trend_print)
        self.dataprintButton.grid(row=9, column=1, columnspan=2, sticky=N + S + E + W)

        self.label7= Label(master, height=1, width=20)
        self.label7.grid(row=10, column=0, sticky=N + S + E + W)

        self.logoutButton = Button(master, text= "LOGOUT", command= self.logout)
        self.logoutButton.grid(row=11, column=1, columnspan=2, sticky=N + S + E + W)


    def add_user(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI__add_user(root)
        root.mainloop()

    def monitoring_view(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI__monitoring_view(root)
        root.mainloop()

    def graph_view(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI__graph_view(root)
        root.mainloop()

    def parameter_setting(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI__trend_print(root)#######################
        root.mainloop()

    def trend_print(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI__trend_print(root)#######################
        root.mainloop()

    def logout(self):
        self.master.destroy()
        root=Tk()
        SCADA_GUI_LOGIN(root)
        root.mainloop()


#Add user class for SCADA


class SCADA_GUI__add_user:
    def __init__(self,master):
        self.master=master
        self.master.geometry("520x300")
        self.role_option=["admin", "employee"]

        self.label1 = Label(master, height=1, width=20)
        self.label1.grid(row=0, column=0,sticky=N + S + E + W)

        self.label2 = Label(master,height=1, width=20, text="Add Employee")
        self.label2.grid(row=0, column=1, columnspan=2, sticky=N + S + E + W)
        self.label2.config(font=("Arial", 15))

        self.label3 = Label(master, height=1, width=20)
        self.label3.grid(row=1, column=0, columnspan=4, sticky=N + S + E + W)

        self.label4 = Label(master, height=1, width=20)
        self.label4.grid(row=2, column=0, columnspan=4, sticky=N + S + E + W)

        self.labelUserName = Label(master, text= "User Name")
        self.labelUserName.grid(row=2, column= 1)

        self.entryUserName = Entry(master)
        self.entryUserName.grid(row=2, column=2)

        self.label4 = Label(master, height=1, width=20)
        self.label4.grid(row=3, column=0, columnspan=4, sticky=N + S + E + W)

        self.label5 = Label(master, height=1, width=20)
        self.label5.grid(row=4, column=0, sticky=N + S + E + W)


        self.labelPassword = Label(master, text= "Password")
        self.labelPassword.grid(row=4, column= 1)

        self.entryPassword = Entry(master, show='*')
        self.entryPassword.grid(row=4, column= 2)

        self.label5 = Label(master, height=1, width=20)
        self.label5.grid(row=5, column=0, columnspan=4, sticky=N + S + E + W)

        self.label6 = Label(master, height=1, width=20)
        self.label6.grid(row=6, column=0,sticky=N + S + E + W)

        self.labelRole = Label(master, text= "Role :")
        self.labelRole.grid(row=6, column= 1)

        self.role = StringVar(master)
        self.role.set(self.role_option[0])
        self.role_menu = OptionMenu(master, self.role, self.role_option[0], self.role_option[1])
        self.role_menu.config(width=15)
        self.role_menu.grid(row=6, column=2)


        self.label7 = Label(master, height=1, width=20)
        self.label7.grid(row=7, column=0,columnspan=4, sticky=N + S + E + W)

        self.label8 = Label(master, height=1, width=20)
        self.label8.grid(row=8, column=0,sticky=N + S + E + W)

        self.submitButton = Button(master, text="Submit", command=self.add_user)
        self.submitButton.grid(row=8, column=2)
        self.submitButton.config(width=17)

        self.label9 = Label(master, height=1, width=20)
        self.label9.grid(row=9, column=0, columnspan= 4, sticky=N + S + E + W)

        self.label10 = Label(master, height=1, width=20)
        self.label10.grid(row=10, column=0,columnspan=4, sticky=N + S + E + W)


        self.label11 = Label(master, height=1, width=20)
        self.label11.grid(row=11, column=0,columnspan=2, sticky=N + S + E + W)

        self.MainMenuButton = Button(master, text="Main Menu", command=self.SCADA_menu)
        self.MainMenuButton.grid(row=11, column=2)
        self.MainMenuButton.config(width=17)


    def add_user(self):
        emp_role=self.role.get()
        emp_name=self.entryUserName.get()
        emp_password= self.entryPassword.get()
        if (emp_name != "" and emp_password != ""):
            if emp_role == "admin":
                a = open('admin_list.txt', 'a')
                a.write(' '+emp_name)
                a.close()
                b = open('admin_password.txt', 'a')
                b.write(' '+emp_password)
                b.close()
                self.master.destroy()
                root = Tk()
                SCADA_GUI__add_user(root)
                root.mainloop()


        else:
            root6 = Tk()
            labelInvalidEntry = Label(root6, text="Invalid Entry")
            labelInvalidEntry.grid(row=0, column=0)
            root6.mainloop()



    def SCADA_menu(self):
        self.master.destroy()
        root = Tk()
        SCADA_OPTION(root)
        root.mainloop()


#Monitoring view class for SCADA


class SCADA_GUI__monitoring_view:
    def __init__(self,master):
        self.master=master
        self.master.geometry("520x300")

        self.label1 = Label(master, height=1, width=20, text="SENSOR-01")
        self.label1.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)

        self.label2 = Label(master,height=1, width=10, text="TEMPERATURE")
        self.label2.grid(row=1, column=0, sticky=N + S + E + W)

        self.sensor1_temp_text = Text(master,height=1, width=20, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor1_temp_text.grid(row=1, column=1, sticky=N + S + E + W)

        self.label3 = Label(master,height=1, width=20, text="RH(%)")
        self.label3.grid(row=2, column=0, sticky=N + S + E + W)

        self.sensor1_RH_text = Text(master,height=1, width=10, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor1_RH_text.grid(row=2, column=1, sticky=N + S + E + W)

        self.label4 = Label(master, height=1, width=20)
        self.label4.grid(row=3, column=0, sticky=N + S + E + W)

        self.label5 = Label(master, height=1, width=20, text="SENSOR-02")
        self.label5.grid(row=4, column=0, columnspan=4, sticky=N + S + E + W)

        self.label6 = Label(master,height=1, width=10, text="TEMPERATURE")
        self.label6.grid(row=5, column=0, sticky=N + S + E + W)


        self.sensor2_temp_text = Text(master,height=1, width=20, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor2_temp_text.grid(row=5, column=1, sticky=N + S + E + W)

        self.label7 = Label(master,height=1, width=20, text="RH(%)")
        self.label7.grid(row=6, column=0, sticky=N + S + E + W)

        self.sensor2_RH_text = Text(master,height=1, width=10, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor2_RH_text.grid(row=6, column=1, sticky=N + S + E + W)

        self.label8 = Label(master, height=1, width=20)
        self.label8.grid(row=7, column=0, sticky=N + S + E + W)

        self.label9 = Label(master, height=1, width=20, text="SENSOR-03")
        self.label9.grid(row=8, column=0, columnspan=4, sticky=N + S + E + W)

        self.label10 = Label(master,height=1, width=10, text="TEMPERATURE")
        self.label10.grid(row=9, column=0, sticky=N + S + E + W)


        self.sensor3_temp_text = Text(master,height=1, width=20, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor3_temp_text.grid(row=9, column=1, sticky=N + S + E + W)

        self.label11 = Label(master,height=1, width=20, text="RH(%)")
        self.label11.grid(row=10, column=0, sticky=N + S + E + W)

        self.sensor3_RH_text = Text(master,height=1, width=10, wrap= WORD, bg='yellow', font = "Calibri 11")
        self.sensor3_RH_text.grid(row=10, column=1, sticky=N + S + E + W)

        self.label12 = Label(master,height=1, width=20)
        self.label12.grid(row=11, column=0, sticky=N + S + E + W)


        self.MainMenuButton = Button(master, text="Main Menu", width=20, command=self.SCADA_menu)
        self.MainMenuButton.grid(row=12, column=3)


        timerThread = threading.Thread(target=self.sensor_reading)
        timerThread.start()



    def sensor_reading(self):
        next_call = time.time()
        while True:
            opc=OpenOPC.open_client('localhost')
            opc.connect('Kepware.KEPServerEX.V6', 'localhost')
           # t1= opc.read('Channel1.Device1._System._SecondsInError')
           # rh1= opc.read('Channel1.Device1._System._SecondsInError')

            t1= opc.read('Channel1.Device1.T')
            rh1= opc.read('Channel1.Device1.RH')

            t2= opc.read('Channel1.Device2.T')
            rh2= opc.read('Channel1.Device2.RH')

            t3= opc.read('Channel1.Device3.T')
            rh3= opc.read('Channel1.Device3.RH')

            T1=float(t1[0])/100
            RH1=float(rh1[0])/100

            T2=float(t2[0])/100
            RH2=float(rh2[0])/100

            T3=float(t3[0])/100
            RH3=float(rh3[0])/100

            self.sensor1_temp_text.delete('0.0', END)
            self.sensor1_temp_text.insert(0.0,T1)
            self.sensor1_RH_text.delete('0.0', END)
            self.sensor1_RH_text.insert(0.0,RH1)
            self.sensor2_temp_text.delete('0.0', END)
            self.sensor2_temp_text.insert(0.0,T2)
            self.sensor2_RH_text.delete('0.0', END)
            self.sensor2_RH_text.insert(0.0,RH2)
            self.sensor3_temp_text.delete('0.0', END)
            self.sensor3_temp_text.insert(0.0,T3)
            self.sensor3_RH_text.delete('0.0', END)
            self.sensor3_RH_text.insert(0.0,RH3)

            next_call = next_call+1;
            time.sleep(next_call - time.time())

    def SCADA_menu(self):
        self.master.destroy()
        root = Tk()
        SCADA_OPTION(root)
        root.mainloop()


#Graph View Class SCADA


class SCADA_GUI__graph_view:
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x550")

        self.label1 = Label(master,text="SENSOR 01 TEMPERATURE TREND")
        self.label1.grid(row=0, column=0, sticky=N + S + E + W)
        self.label1.config(font=("Arial", 15))

        canvas=FigureCanvasTkAgg(fig, master)
        canvas.get_tk_widget().grid(row=1,column=0)

        self.anim = animation.FuncAnimation(fig, self.animate_graph,interval=2000, repeat=True)

        self.label2 = Label(master,text="SENSOR 01 RH TREND")
        self.label2.grid(row=2, column=0, sticky=N + S + E + W)
        self.label2.config(font=("Arial", 15))

        canvas=FigureCanvasTkAgg(fig, master)
        canvas.get_tk_widget().grid(row=3,column=0)

        self.anim = animation.FuncAnimation(fig, self.animate_graph,interval=2000, repeat=True)

        self.label2 = Label(master)
        self.label2.grid(row=4, column=0, sticky=N + S + E + W)
        self.label2.config(font=("Arial", 15))

        self.MainMenuButton = Button(master, text="Main Menu", width=20, command=self.SCADA_menu)
        self.MainMenuButton.grid(row=5, column=0)



    def animate_graph(self, i):
        opc=OpenOPC.open_client('localhost')
        opc.connect('Kepware.KEPServerEX.V6', 'localhost')


        t1_data_raw = open("Temperature-01.txt","r")
        pullDataRaw = t1_data_raw.read()
        dataListRaw=pullDataRaw.split('\n')
        dataListRaw_len=len(dataListRaw)

        if len(dataListRaw)==6:
            dataListRaw.pop(0)
            t1_data_raw.close()
            newDataList='\n'.join(dataListRaw)
            t1_data_raw=open("Temperature-01.txt","w")
            t1_data_raw.write(newDataList)
            t1_data_raw.close()

            t1= opc.read('Channel1.Device1.T')
            rh1= opc.read('Channel1.Device1.RH')
            t1_data = open("Temperature-01.txt","a")
            t1_data.write(str(float(t1[0])/100)+'**'+ str(t1[2])+'\n')
            t1_data.close()
        else:
            t1_data_raw.close()
            t1= opc.read('Channel1.Device1.T')
            rh1= opc.read('Channel1.Device1.RH')
            t1_data = open("Temperature-01.txt","a")
            t1_data.write(str(float(t1[0])/100)+'**'+ str(dataListRaw_len)+'\n')
            t1_data.close()


        pullData = open("Temperature-01.txt","r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        xList_raw = []
        for eachLine in dataList:
            if len(eachLine)>1:
                y, x = eachLine.split('**')
                xList.append(x)
                yList.append(float(y))
        a.clear()
        a.plot(xList, yList)

    def SCADA_menu(self):
        self.master.destroy()
        root = Tk()
        SCADA_OPTION(root)
        root.mainloop()


#SCADA Parameter Setting


class SCADA_GUI__trend_print:
    def __init__(self,master):
        self.master=master
        self.master.geometry("520x300")
#row1

        self.label1 = Label(master, height=3, width=20, text= "TREND DATA PRINT")
        self.label1.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)
        self.label1.config(font=("Arial", 15))

        #row two
        self.label2 = Label(master, height=3, width=20)
        self.label2.grid(row=1, column=0, sticky=N + S + E + W)

        self.label3 = Label(master, height=3, width=20)
        self.label3.grid(row=1, column=3, sticky=N + S + E + W)
#row 3
        self.label4 = Label(master, height=3, width=20)
        self.label4.grid(row=2, column=0, sticky=N + S + E + W)

        self.label5 = Label(master, height=3, width=20)
        self.label5.grid(row=2, column=3, sticky=N + S + E + W)

#row 4
        self.label6 = Label(master, height=3, width=20)
        self.label6.grid(row=3, column=0,columnspan=2, sticky=N + S + E + W)


        self.label7 = Label(master,height=3, width=20)
        self.label7.grid(row=3, column=3, sticky=N + S + E + W)
#row 5
        self.label8 = Label(master, height=3, width=20)
        self.label8.grid(row=4, column=0, columnspan=4, sticky=N + S + E + W)

        time_now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#Labels
        self.labelStartDate = Label(master, text= "START DATE")
        self.labelStartDate.grid(row=1, column= 1)

        self.entryStartDate = Entry(master)
        self.entryStartDate.grid(row=1, column= 2)
        self.entryStartDate.config(font=("Arial", 8))

        self.entryStartDate.delete(0,END )
        self.entryStartDate.insert(0,time_now )


        self.labelEndDate = Label(master, text= "END DATE")
        self.labelEndDate.grid(row=2, column= 1)

        self.entryEndDate = Entry(master)
        self.entryEndDate.grid(row=2, column= 2)

        self.entryEndDate.delete(0,END )
        self.entryEndDate.insert(0,time_now )

        self.printButton = Button(master, text= "PRINT", command= self.data_print, height= 1, width= 15)
        self.printButton.grid(row=3, column=2)

        self.menuButton = Button(master, text= "MENU", command= self.SCADA_menu, height= 1, width= 15)
        self.menuButton.grid(row=4, column=2)

    def data_print (self):
        start_date=self.entryStartDate.get()
        print (start_date)
        end_date=self.entryEndDate.get()
        print (end_date)
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database= "SCADA")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM sensor1 WHERE time BETWEEN '%s' AND '%s' " %(start_date,end_date))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(str(x[0]) + " Temperature : " + str(x[1]) + " RH : " +str(x[2]))
        pdfReportPages = "report.pdf"

        doc = SimpleDocTemplate(pdfReportPages, pagesize=A4)
        # container for the "Flowable" objects
        elements = []
        styles=getSampleStyleSheet()
        styleN = styles["Normal"]

        # Make heading for each column and start data list
        column1Heading = "Time"
        column2Heading = "Temperature (°C)"
        column3Heading = "RH (%)"
        # Assemble data for each column using simple loop to append it into data list
        data = [[column1Heading,column2Heading,column3Heading]]
        for x in myresult:
            data.append([str(x[0]),str(x[1]), str (x[2])])


        tableThatSplitsOverPages = Table(data, [4 * cm, 2.9 * cm, 2.5 * cm], repeatRows=1)
        tableThatSplitsOverPages.hAlign = 'CENTRE'
        tblStyle = TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(1,0),(-2,-1),1,colors.black),
                               ('BOX',(0,0),(0,-1),1,colors.black)])

        tblStyle.add('BACKGROUND',(0,0),(-1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
        tableThatSplitsOverPages.setStyle(tblStyle)
        elements.append(tableThatSplitsOverPages)

        doc.build(elements)
        os.startfile('report.pdf')

    def SCADA_menu(self):
        self.master.destroy()
        root = Tk()
        SCADA_OPTION(root)
        root.mainloop()






def GUI_Section ():
    root=Tk()
    SCADA_GUI_LOGIN(root)
    root.mainloop()




def data_logging ():
    while True:
        time.sleep(2)
        opc=OpenOPC.open_client('localhost')
        opc.connect('Kepware.KEPServerEX.V6', 'localhost')
        # t1= opc.read('Channel1.Device1._System._SecondsInError')
        # rh1= opc.read('Channel1.Device1._System._SecondsInError')

        t1= opc.read('Channel1.Device1.T')
        rh1= opc.read('Channel1.Device1.RH')

        t2= opc.read('Channel2.Device1.T')
        rh2= opc.read('Channel2.Device1.RH')

        t3= opc.read('Channel3.Device1.T')
        rh3= opc.read('Channel3.Device1.RH')

        T1=float(t1[0])/100
        RH1=float(rh1[0])/100
        time_now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #time_now=datetime.now()
        print (time_now)

        print(str(time_now) + " Temperature : " + str(x[1]) + " RH : " +str(x[2]))


        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database= "SCADA")
      
        mycursor = mydb.cursor()
        #mycursor.execute("CREATE TABLE sensor1 (time DATETIME, temperature DECIMAL(8,2),rh DECIMAL(8,2))")
        #mycursor.execute("CREATE TABLE sensor2 (time DATETIME PRIMARY KEY, temperature FLOAT(3,2),rh FLOAT(3,2))")
        #mycursor.execute("CREATE TABLE sensor3 (time DATETIME PRIMARY KEY, temperature FLOAT(3,2),rh FLOAT(3,2))")

        sql = ("INSERT INTO sensor1 (time, temperature,rh) VALUES (%s, %s, %s)")
        val = (time_now, T1, RH1)
        mycursor.execute(sql, val)
        mydb.commit()





t=time.time()
t1=threading.Thread(target=GUI_Section)
t2=threading.Thread(target=data_logging)
t1.start()
t2.start()
t1.join()
t2.join()

