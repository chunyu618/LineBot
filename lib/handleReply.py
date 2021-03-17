from linebot.models import *
from random import seed
from random import random
from random import randint

usage = """
指令集
1. 衛星雲圖
2. 天氣預報 <縣市名稱><縣/市>
3. 骰子
4. 擲硬幣
5. 吃什麼
6. 持續增加中......

還有一些奇奇怪怪的自己去發掘吧
"""

replyDict = {
    "生日快樂": "@布衣 生日快樂",
    "早安": "おはようございます。\n今日も一緒に頑張りましょう。",
    "晚安": "今夜もおやすみなさい。\nやさしい夢みてね。",
    "你好": "ご挨拶をちゃんとして偉いね"
    "指令": usage,
}

def getReply(message, token):
    seed()
    reply = ""
    if "吃什麼" == message.strip():
        from .food import getFood
        reply = TextSendMessage(text=getFood())
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
        if token == "Ccfb3d059fffde96fcab318e1c5a24c7e":
            from . import findNHenTai
            reply = TextSendMessage(text=findNHenTai.getUrl(message))
        else:
            reply = ""
    else:
        try:
            reply = TextSendMessage(text=replyDict[message.strip()].strip())
        except:
            reply = ""
    return reply            

def main():
    s = input()
    print(getReply(s))

if __name__ == "__main__":
    main()
