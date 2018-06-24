# coding=utf-8
import time

import fcoin

key = ''
secret = ''

api = fcoin.authorize(key, secret)
print api.accounts_balance


import fcoin
from fcoin.WebsocketClient import WebsocketClient
from threading import Thread
class HandleWebsocket(WebsocketClient):
    def handle(self,msg):
        for key,value in msg.items():
            print(key,value)
ws = HandleWebsocket()
topics = {
         "id": "tickers",
         "cmd": "sub",
         "args": ["depth.L20.ethusdt"],
    }
sub = ws.sub
Thread(target=sub,args=(topics,)).start()
time.sleep(20)
ws.close()

