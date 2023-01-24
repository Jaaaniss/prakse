
import requests
import json
from datetime import datetime

print('start')

now = datetime.now()

response = requests.get("https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR")

dateOfInterest = now.strftime('%d-%m-%Y')

jayson = json.loads(response.text)

for row in jayson['data']['Rows']:
    if row['IsExtraRow']:
        continue

    for dayData in row['Columns']:
        if (dayData['Name'] != dateOfInterest):
            continue

        sSplit = row['StartTime'].split('T')
        eSplit = row['EndTime'].split('T')


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)


#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")


#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE data (id INT AUTO_INCREMENT PRIMARY KEY, start_hour VARCHAR(255), end_hour VARCHAR(255), price INT)")


mycursor = mydb.cursor()

sql = "INSERT INTO data (start_hour, end_hour, price) VALUES (%s, %s, %s)"
val = [
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value']),
  (sSplit[1], eSplit[1], dayData['Value'])
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")