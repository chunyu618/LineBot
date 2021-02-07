from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from lib.handleReply import getReply

app = Flask(__name__)
groupID = os.getenv("groupID")

# Channel Access Token
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
# Channel Secret
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

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
    if event.source.user_id == "U8a0689e8c509591a033866c59c19b323":
        return   
    message = TextSendMessage(text=event.message.text)
    #print(event.__dict__)
    ID = ""
    if event.source.type == "group":
        ID = event.source.group_id#event.source.group_id
    elif event.source.type == "user":   
        ID = event.source.user_id

    reply = getReply(message.text, ID)            
    #print(reply)
    if reply != "":
        line_bot_api.reply_message(event.reply_token, reply)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
