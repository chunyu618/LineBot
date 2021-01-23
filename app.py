from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
groupID = "Ccfb3d059fffde96fcab318e1c5a24c7e"

# Channel Access Token
line_bot_api = LineBotApi('8kBJ1gq9dgeHZDS7SKd/dVaKkrGwkBEZmscOEqR1yKdwoTb3Zve+6hf8T9HPt1wG4eJKFZi+aUj0DNQncog5n5JGE6dha4G9jEVsn1BLSelYLiWxoNxj0T04DPUk0Hy/WS9ASu4IDuI7JhHmF2MS7gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('be659d2030e45542f71387e202f36c4a')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):    
    message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
    print(event.__dict__)
    ID = ""
    reply = ""
    if event.source.type == "group":
        ID = event['source']['groupId']#"Ccfb3d059fffde96fcab318e1c5a24c7e"
    elif event.source.type == "user":   
        ID = event.source.user_id
    if "生日快樂" in message.text:
        reply = TextSendMessage(text="@林珺瑩 生日快樂")
    #if "切" in message.text:
    #    reply = TextSendMessage(text="@陳文榛 切ㄐㄐ")
    if "野" == message.text.strip():
        reply = TextSendMessage(text="斷")
    line_bot_api.push_message(ID, reply)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
