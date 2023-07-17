from flask import Flask, request
import requests
from pymessenger import Bot

app = Flask(__name__)

VERIFY_TOKEN = 'Ansab'
PAGE_ACCESS_TOKEN = 'facebook_bot_access_page_token'
bot = Bot(PAGE_ACCESS_TOKEN)

def handling_message(text):
    adjusted_msg = text
    if adjusted_msg =='hi' or adjusted_msg=='Hi':
        response = 'Hello'
        
    elif adjusted_msg =="what's up" or adjusted_msg =="What's Up":
        response = "I'm Fine"
        
    else:
        response = "It's Pleasure to chat with you today, thank you."
    
    return response

app.route('/', method=["POST","GET"])

def web_hook():
    if request.method =="GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Unable to connect to FB'
    
    elif request.method =='POST':
        data = request.json
        process = data['entry'][0]['messaging'] 
        for msg in process:
            text = msg['message']['text']
            sender_id = msg['sender']['id']
            response = handling_message(text)
            bot.send_text_message(sender_id, response)
            
        return 'message_posted'
       
    else:
        return 'ok'
    
    
if __name__== '__main__':
    app.run()