from flask import Flask,request,jsonify
from flask_sslify import SSLify
from twilio.twiml.messaging_response import MessagingResponse

from data import *

import datetime

app=Flask(__name__)
sslify=SSLify(app)

@app.route("/", methods=['GET','POST'])
def sms_reply():
    if request.method=='POST':
        now = datetime.datetime.now()
        msg = request.form
        last_message=msg["Body"]
        #Welcome bot depending on the time of day with a time shift
        #Приветствие бота в зависимости от времени суток со сдвигом по времени
        if last_message.lower() in greetings and 6 <= now.hour+2 < 12:
            bot=MessagingResponse()
            bot.message('Доброе утро!')
            return str(bot)
        elif last_message.lower() in greetings and 12 <= now.hour+2 < 17:
            bot=MessagingResponse()
            bot.message('Добрый день!')
            return str(bot)
        elif last_message.lower() in greetings and 17 <= now.hour+2 < 23:
            bot=MessagingResponse()
            bot.message('Добрый вечер!')
            return str(bot)
        elif last_message.lower() in greetings and ((now.hour+2)>=23 or (now.hour+2)<6):
            bot=MessagingResponse()
            bot.message('Доброго времени суток!')
            return str(bot)
    elif request.method=='GET':
        return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    app.run()
