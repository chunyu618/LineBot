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
from lib.ReplyClass import ReplyMetaData

app = Flask(__name__)
group_1 = os.getenv("group_1")
group_2 = os.getenv("group_2")

# Channel Access Token
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
# Channel Secret
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
replyMetaData = ReplyMetaData()

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
    #print(group_1)
    #print(group_2)
    ID = ""
    if event.source.type == "group":
        ID = event.source.group_id  #event.source.group_id
        if ID != group_1 and ID != group_2:
            return
    elif event.source.type == "user":
        ID = event.source.user_id
        if ID != "U16329817cbf4c6df77f60b122707a691":
            return

    global replyMetaData
    reply = getReply(message.text, ID, replyMetaData)            
    #print(reply)
    if reply != "":
        line_bot_api.reply_message(event.reply_token, reply, replyMetaData)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

