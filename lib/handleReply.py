from linebot.models import *
from random import seed
from random import random
from random import randint
from datetime import datetime


replyDict = {
    "生日快樂": "@曉謙 生日快樂",
    "早安": "おはようございます。\n今日も一緒に頑張りましょう。",
    "晚安": "今夜もおやすみなさい。\nやさしい夢みてね。"
}

def getReply(message):
    seed(datetime.now())
    reply = ""
    if "吃什麼" == message.strip():
        from .food import getFood
        reply = TextSendMessage(text=getFood())
    #elif "切" in message.text:
    #    reply = TextSendMessage(text="@陳文榛 切ㄐㄐ")
    elif "骰子" == message.strip():
        return TextSendMessage(str(randint(1, 6)))
    elif "擲硬幣" == message.strip():
        r = random()
        if r < 0.5:
            return TextSendMessage("正")
        else:
            return TextSendMessage("反")
    elif "野" == message.strip():
        r = random()
        if r < 0.001:
            reply = TextSendMessage(text="幾歲了還在接龍＝＝")
        elif r > 0.5:
            reply = TextSendMessage(text="斷")
        else:
            reply = TextSendMessage(text="格")
    elif "炸" == message.strip():
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
    elif "衛星雲圖" == message.strip():
        imgUrl = "https://opendata.cwb.gov.tw/fileapi/opendata/MSC/O-A0058-003.png"
        reply = ImageSendMessage(
            original_content_url=imgUrl,
            preview_image_url=imgUrl
            )
    elif "找本子" == message.split()[0]:
        from . import findNHenTai
        reply = TextSendMessage(text=findNHenTai.getUrl(message))
    else:
        try:
            reply = TextSendMessage(text=replyDict[message.strip()])
        except:
            reply = ""
    return reply            

def main():
    s = input()
    print(getReply(s))

if __name__ == "__main__":
    main()
