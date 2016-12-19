#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zubair.zahiruddin
#
# Created:     26/08/2015
# Copyright:   (c) zubair.zahiruddin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import pyodbc

# connecting to sql-server through user credentials
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CPUZuby;DATABASE=DB_NEW;UID=sa12;PWD=123')
cursor = cnxn.cursor()

#connecting to sql-server through windows authentication
cnxn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=LTZUBAIRZ\SQLEXPRESS;DATABASE=ETL_TEST;Trusted_Connection=yes;')
#cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=myDB;')
cursor = cnxn.cursor()

cursor.execute('''
SELECT * FROM PATIENTS''')

row = cursor.fetchall();

while row:
    print row ;














