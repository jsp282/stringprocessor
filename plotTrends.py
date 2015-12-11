import json
import httplib
import mysql.connector
import numpy
from matplotlib import pyplot as plt

# Plotting SQL Data
cnx = mysql.connector.connect(host="localhost", user="root", passwd="", db="User")
cursor = cnx.cursor()

sql = "SELECT * FROM nwams;"

cursor.execute(sql)
amount_history = []
balance_history = []
for m in cursor:
    print m
    amount_history.append(m[0])
    balance.history.append(m[9])

cnx.commit()
cnx.close()

#Plotting Blockchain Data
cnxBC = mysql.connector.connect(host="localhost", user="root", passwd="", db="Blockchain")
cursorBC = cnxBC.cursor()

sqlBC = "SELECT * FROM Ledger;"

cursorBC.execute(sqlBC)
money_history = []
volume_history = []
date_array = []
for m in cursorBC:
    print m
    money_history.append(m[0])
    volume_history.append(m[1])
    date_array.append(m[3])

cnxBC.commit()
cnxBC.close()

plt.figure(1)
plt.plot(date_array, money_history)
plt.show()
