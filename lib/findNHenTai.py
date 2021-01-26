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
    #print(message.split()[1:])
    tag = "+".join(message.split()[1:])
    #print(tag)
    nhentai = "https://nhentai.to/"
    url = nhentai + "search?q=" + tag
    
    # Get the result number
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    result = soup.find_all('h2')[0].get_text().split()[0].replace(",", "")
    
    # Return if result is 0
    if int(result) == 0:
        return "查無結果"

    # Calculate target page and item number
    targetNumber = randint(1, int(result))
    page = (targetNumber / 25) + 1
    item = targetNumber % 25
    
    # Parse page url
    pageUrl = url + "&page=%s" % (page)
    targetRequests = requests.get(pageUrl)
    targetSoup = BeautifulSoup(targetRequests.text, features="html.parser")
    hashNumber = targetSoup.find_all('a', {'class': 'cover'})[item].attrs['href']
    targetUrl = path.join(nhentai, hashNumber.strip('/'))
    return targetUrl

def main():
    print(getUrl("fate"))

if __name__ == "__main__":
    main()
