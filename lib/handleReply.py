from linebot.models import *
from random import seed
from random import random
from random import randint
import json

usage = """
指令集
1. 衛星雲圖
2. 天氣預報 <縣市名稱><縣/市>
3. 骰子
4. 擲硬幣
5. 吃什麼
6. 地震報告
7. 持續增加中......

還有一些奇奇怪怪的自己去發掘吧
"""

replyDict = {
    "生日快樂": "@布衣 生日快樂",
    "早安": "おはようございます。\n今日も一緒に頑張りましょう。",
    "晚安": "今夜もおやすみなさい。\nやさしい夢みてね。",
    "你好": "ご挨拶をちゃんとして偉いね",
    "午安": "請用冰開水",
    "指令": usage,
}

token_read = False
token_list = []
def read_token():
    global token_list
    global token_read
    with open('files/token.json') as f:
        data = json.load(f)
        token_list = data['token']
        token_read = True
            
    return


def getReply(message, token, replyMetaData):
    seed()
    #print(replyMetaData.numberOfMochi)
    global token_list
    global token_read
    
    if not token_read:
        read_token()
    if token not in token_list:
        return ""

    matchValue = message.strip()
    if "吃什麼" == matchValue:
        from .food import getFood
        replyMetaData.numberOfFood += 1
        called = replyMetaData.numberOfFood
        reply = TextSendMessage(text=getFood())
        if replyMetaData.numberOfFood == 6:
            replyMetaData.numberOfFood = 0

    elif "骰子" == matchValue:
        return TextSendMessage(str(randint(1, 6)))
    elif "擲硬幣" == matchValue:
        r = random()
        if r < 0.5:
            return TextSendMessage("正")
        else:
            return TextSendMessage("反")
    elif "野" == matchValue:
        r = random()
        if r < 0.001:
            reply = TextSendMessage(text="幾歲了還在接龍＝＝")
        elif r > 0.5:
            reply = TextSendMessage(text="斷")
        else:
            reply = TextSendMessage(text="格")
    elif "炸" == matchValue:
        r = random()
        if r < 0.001:
            reply = TextSendMessage(text="幾歲了還在接龍＝＝")
        elif r > 0.5:
            reply = TextSendMessage(text="斷")
        else:
            reply = TextSendMessage(text="彈")
    elif "天氣預報" == message.split()[0]:
        from . import weatherForecast
        reply = TextSendMessage(text=weatherForecast.getUrl(message))
    elif "地震報告" == matchValue:
        from . import EarthquakeReport
        reply = TextSendMessage(text=EarthquakeReport.getUrl(message))
    elif "雷達回波" == matchValue:
        imgUrl = "https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png"
        reply = ImageSendMessage(
            original_content_url=imgUrl,
            preview_image_url=imgUrl
            )
    elif "衛星雲圖" == matchValue:
        imgUrl = "https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-B0028-003.jpg"
        reply = ImageSendMessage(
            original_content_url=imgUrl,
            preview_image_url=imgUrl
            )
    elif "麻糬" == matchValue:
        replyMetaData.numberOfMochi += 1    
        if replyMetaData.numberOfMochi == 6:
            replyMetaData.numberOfMochi = 0
            return TextSendMessage("救命！")
    elif "找本子" == message.split()[0]:
        if token == token_list[0]:
            from . import findNHenTai
            reply = TextSendMessage(text=findNHenTai.getUrl(message))
        else:
            reply = ""
    elif "找影集" == message.split()[0]:
        from . import findTV
        reply = TextSendMessage(text=findTV.getUrl(message))
    else:
        try:
            reply = TextSendMessage(text=replyDict[matchValue].strip())
        except:
            reply = ""
    return reply            

def main():
    s = input()
    print(getReply(s))

if __name__ == "__main__":
    main()
