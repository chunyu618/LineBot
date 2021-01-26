from linebot.models import *

from random import seed
from random import random
from datetime import datetime
from .food import getFood
from . import findNHenTai

seed(datetime.now())

replyDict = {
    "生日快樂": "@曉謙 生日快樂",
    "早安": "おはようございます。\n今日も一緒に頑張りましょう。",
    "晚安": "今夜もおやすみなさい。\nやさしい夢みてね。"
}

def getReply(message):
    reply = ""
    if "吃什麼" == message.strip():
        reply = TextSendMessage(text=getFood())
    #elif "切" in message.text:
    #    reply = TextSendMessage(text="@陳文榛 切ㄐㄐ")
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
    elif "衛星雲圖" == message.strip():
        imgUrl = "https://opendata.cwb.gov.tw/fileapi/opendata/MSC/O-A0058-003.png"
        reply = ImageSendMessage(
            original_content_url=imgUrl,
            preview_image_url=imgUrl
            )
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
