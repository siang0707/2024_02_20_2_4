#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "<p>Hello, 景翔!</p>"
#    return "<h1>Flask</h1><p>Hello, 景翔!</p>"
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import google.generativeai as genai

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
genai.configure(api_key=os.environ['Gemini_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        response = model.generate_content(event.message.text)
        #event.message.text為對方傳送的內容訊息包裝成response
        message = TextSendMessage(text=response.text)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        message = TextSendMessage(text="發生不明錯誤!請稍待一下再重試")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)