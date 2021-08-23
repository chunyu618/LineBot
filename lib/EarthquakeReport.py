import requests
from bs4 import BeautifulSoup
from random import randint
from random import seed
from datetime import datetime
from os import path
from os import getenv
seed(datetime.now())
'''
for i in range(1,10):
    r = requests.get('https://unity3d.com/unity/qa/lts-releases?page='+str(i))
    soup = BeautifulSoup(r.text)
    for ii in soup.find_all('h4',{'class':'mb5 expand'}):
        print(ii.get_text())
'''

reportContent = {""}

def getUrl(message):
    rev = ""
    token = getenv("CWB_AUTHORIZATION")

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=%s" % (token)
    #print(url)
    #print(requests.get(url))
    r = requests.get(url).json()
    
    earthquakeReport = r['records']['earthquake'][0]
    rev += "地震編號: %s\n" % (earthquakeReport['earthquakeNo'])
    rev += "地震時間: %s\n" % (earthquakeReport['earthquakeInfo']['originTime'])
    rev += "規模: %s\n" % (earthquakeReport['earthquakeInfo']['magnitude']['magnitudeValue'])
    rev += "深度: %s公里\n" % (earthquakeReport['earthquakeInfo']['depth']['value'])
    rev += "震央: %s\n" % (earthquakeReport['earthquakeInfo']['epiCenter']['location'])
    rev += "經緯度: %s度 %s度\n" % (earthquakeReport['earthquakeInfo']['epiCenter']['epiCenterLat']['value'], earthquakeReport['earthquakeInfo']['epiCenter']['epiCenterLon']['value'])
    rev += "報告內容: %s\n" % (earthquakeReport['reportContent'])
    


    return rev.strip()

def main():
    print(getUrl("天氣預報 桃園市是"))

if __name__ == "__main__":
    main()
