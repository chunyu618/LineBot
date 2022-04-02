import requests
import json
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
    if len(tag) == 0:
        return "請輸入關鍵字"

    nhentai = "https://url-detect.robin019.xyz/"
    url = nhentai + "search?query=" + tag
    # Get the result number
    r = requests.get(url)
    
    print(type(r.text))
    data = json.loads(r.text)

    rev = ""
    for ott in data:
        rev += ott['ott'] + '\n'

    if len(rev) == 0:
        return "查無資料"
    return rev.strip()
    
    

def main():
    print(getUrl("找影集 鬼滅"))

if __name__ == "__main__":
    main()
