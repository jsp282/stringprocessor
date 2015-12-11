import sys
import subprocess
from subprocess import call
import mysql.connector

cnx = mysql.connector.connect(user='root',host='127.0.0.1',database='Blockchain')
cursor = cnx.cursor()

sql = ("SELECT * FROM `Ledger` WHERE 1") 

cursor.execute(sql)

for m in cursor: 
    print m 

cursor.close()
cnx.close()

