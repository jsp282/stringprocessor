import json
import httplib
import mysql.connector

# Getting data from Parse to SQL
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/Transactions/', '', {
    "X-Parse-Application-Id": "QrNi3zPI9lmQq60eFZBsdNrB9LpuTfMB8MPhTJ0n",
    "X-Parse-REST-API-Key": "N9Ix3DMj34lO6b1FTPuwtScWQ2nSt6Q5TAVGsbcv"
})

cnx = mysql.connector.connect(host="localhost", user="root", passwd="", db="User")
cursor = cnx.cursor()

cnxBC = mysql.connector.connect(host="localhost", user="root", passwd="", db="Blockchain")
cursorBC = cnxBC.cursor()

result = json.loads(connection.getresponse().read())
print "ERROR is ", result['error']
for m in result: 
    print m
result = result('results')
createdAt_array = []

print result(len(result) - 1)
m = result(len(result) - 1)
username = m('username')
receiver_account_number = m('receiver_account_number')
receiver_mobile_number = m('receiver_mobile_number')
objectId = m('objectId')
receiver_bank_name = m('receiver_bank_name')
amount = m('amount')
receiver_last_name = m('receiver_last_name')
updatedAt = m('updatedAt')
receiver_first_name = m('receiver_first_name')
createdAt = m('createdAt')
createdAt_array.append(createdAt[0:10])
# sql = "SELECT * FROM nwams;"
temp = createdAt
sql = "INSERT INTO `nwams` (`amount`, `receiver_first_name`, `receiver_last_name`, `receiver_user_name`, `receiver_bank_name`, `receiver_account_number`, `total_sent`, `total_received`, `net`, `balance`) VALUES (\'" + str(amount) + "\', \'" + receiver_first_name + "\', \'" + receiver_last_name + "\', \'" + username + "\', \'" + receiver_bank_name + "\', \'" + str(receiver_account_number) + "\', \'" + str(300) + "\', \'" + str(0) + "\', \'" + str(100) + "\', \'" + str(89000) + "\')"
#print(sql)
cursor.execute(sql)
cnx.commit()

#Get latest values from ledger and apply latest payment
sql = "SELECT * FROM Ledger"
cursorBC.execute(sql)
ledgerLine = []
dayCreated = createdAt[0:10]
moneyPerDayCount = 0
volumePerDayCount = 0
moneyPerDay = 0
volumePerDay = 0
for m in cursorBC:
    ledgerLine = m
    if (m[3] == dayCreated):
        moneyPerDay += m[0]
        volumePerDay += 1
    else:
        dayCreated = m(3)

totalVolume = ledgerLine(2)

moneyPerDay +=amount
volumePerDay += 1
totalVolume += 1
dayCreated = createdAt[0:10]

print volumePerDay, " on the day", dayCreated

print moneyPerDay, " money per day", dayCreated
print totalVolume
totalVolume += 1

#Update SQL Ledger for Blockchain
temp = createdAt_array[0]
y = []

sqlBC = "INSERT INTO `Ledger` (`money_per_day`, `volume_per_day`, `total_volume`, `date`) VALUES (\'" + str(moneyPerDay) + "\', \'" + str(volumePerDay) + "\', \'" + str(totalVolume) + "\', \'" + str(createdAt) + "\')"

#bunchofcomments

cnx.close()
cnxBC.close()

#print result
