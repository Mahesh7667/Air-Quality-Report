import requests
import json
url1="http://api.airpollutionapi.com/1.0/aqi?lat="
cities=['blr','chen','delhi']
city = {1:'12.971599,77.594566',2:'13.082680,80.270721',3:'28.704060,77.102493'}

j=1
lat=''
url2='&lon='
lon=''
print("Enter any city:")
for i in cities:
    print(str(j)+". "+str(i))
    j=j+1
print("4. Or enter longitude and latitudes ")
c = int(input())
if c == 1:
    cord= city.get(c)
    lat,lon = cord.split(",")
elif c == 2:
    cord= city.get(c)
    lat,lon = cord.split(",")
elif c == 3:
    cord= city.get(c)
    lat,lon = cord.split(",")
elif c == 4:
    lat=str(input("enter latitude:"))
    lon = str(input("enter longitude:"))
else:
    print("invalid option")

    
#Replace "xxxxxxxxxxxxxxxxxx" with your API-KEY
url3="&APPID=XXXXXXXXXXXXXXXXXXXXXXXXXXX"
url = url1 + lat + url2 + lon + url3
data = requests.get(url)
data = data.json()
print("Conditions:"+data['data']['text'])
print("Alert:"+data['data']['alert'])
print("Last updated:"+data['data']['updated'])
print("Current temp:"+data['data']['temp'])
print("dominant:"+data['data']['dominating'])
print("NAME"+"\t"+"AQI"+"\t"+"safe")
for para in data['data']['aqiParams']:
    if para['text'] == None:
        break
    else:
        print(para['name']+"\t"+str(para['aqi'])+"\t"+para["text"])
    

