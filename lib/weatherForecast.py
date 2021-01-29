import requests
from bs4 import BeautifulSoup
from random import randint
from random import seed
from datetime import datetime
from os import path
seed(datetime.now())
'''
for i in range(1,10):
    r = requests.get('https://unity3d.com/unity/qa/lts-releases?page='+str(i))
    soup = BeautifulSoup(r.text)
    for ii in soup.find_all('h4',{'class':'mb5 expand'}):
        print(ii.get_text())
'''
def getUrl(message):
    rev = ""
    token = "CWB-C8E5074D-8641-4E75-A81A-AB1CD0AC099E"
    location = message.split()[1].replace("台", "臺")
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=%s&locationName=%s" % (token, location)
    r = requests.get(url).json()
    if len(r['records']['location']) == 0:
        return "查無地點"
    weatherElement = r['records']['location'][0]['weatherElement']
    nameTranslation = {"Wx": "天氣現象", "MaxT": "最高溫度", "MinT": "最低溫度", "CI": "舒適度", "PoP": "降雨機率"}
    nameUnit = {"Wx": "", "MaxT": "°C", "MinT": "°C", "CI": "舒適度", "PoP": "%"}
    for element in weatherElement:
        elementName = element['elementName']
        rev += "%s: %s%s\n" % (nameTranslation[elementName], element['time'][0]['parameter']['parameterName'], nameUnit[elementName])
        #print(element['elementName'])
        #print(element['time'][0]['parameter']['parameterName'])
        #print(rev)

    return rev.strip()

def main():
    print(getUrl("天氣預報 桃園市是"))

if __name__ == "__main__":
    main()
