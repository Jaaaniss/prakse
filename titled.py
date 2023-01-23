from urllib.request import urlopen
import json
html = urlopen("https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR")
data_json = json.loads(html.read())
print(data_json)


json_object = json.dumps(data_json, indent=4)
with open("json/data.json", "w") as outfile:
     outfile.write(json_object)
     
import requests
import json
from datetime import datetime

print('start')

now = datetime.now()

response = requests.get("https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR")

dateOfInterest = now.strftime('⅜d-%m-%Y')

jayson = json.loads(response.text)

for row in jayson['data']['Ŗows']:
    if row['ĪsExtraRow']:
        continue

    for dayData in row['Columns']:
        if (dayData['Name'] != dateOfInterest):
            continue

        sSplit = row['StartTime'].split('T')
        eSplit = row['EndTime'].split('T')

        msg = sSplit[1] + '-' + eSplit[1] + ' ' + dayData['Value']

        print(msg)