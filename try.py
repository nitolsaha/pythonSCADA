# -*- coding: utf-8 -*-

import mysql.connector

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database= "SCADA")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sensor1 WHERE time BETWEEN '2019-12-23 15:07:17' AND '2019-12-23 15:07:48' ")
myresult = mycursor.fetchall()

for x in myresult:
  print(str(x[0]) + " Temperature : " + str(x[1]) + " RH : " +str(x[2]))


pdfReportPages = "test.pdf"
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


import os
os.startfile('test.pdf')
