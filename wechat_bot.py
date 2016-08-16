#!/usr/bin/env python
# coding: utf-8

from wxbot import WXBot
import requests
bot_api="http://127.0.0.1:8000/get_response"

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            user_input = msg["content"]["data"]
            payload={"user_input":user_input}
            response = requests.get(bot_api,params=payload).json()["response"]
            #print(type(response)) # unicode
            self.send_msg_by_uid(response, msg['user']['id'])

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()
