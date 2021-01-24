from linebot.models import *

from random import seed
from random import random
from datetime import datetime
from .food import getFood
seed(datetime.now())


def getReply(message):
    reply = ""
    if "吃什麼" == message.strip():
        reply = TextSendMessage(text=getFood())
    elif "生日快樂" in message:
        reply = TextSendMessage(text="@林珺瑩 生日快樂")
    #if "切" in message.text:
    #    reply = TextSendMessage(text="@陳文榛 切ㄐㄐ")
    elif "野" == message.strip():
        if random() > 0.5:
            reply = TextSendMessage(text="斷")
        else:
            reply = TextSendMessage(text="格")

    return reply            

def main():
    s = input()
    print(getReply(s))

if __name__ == "__main__":
    main()
