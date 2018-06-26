# coding=utf-8
import fcoin

key = ''
secret = ''

api = fcoin.authorize(key, secret)
print api.accounts_balance

from fcoin.WebsocketClient import WebsocketClient

bids = []
asks = []


class HandleWebsocket(WebsocketClient):
    def handle(self, msg):
        print "#############################"
        for key, value in msg.items():
            print key, value
            if key == "bids":
                global bids
                bids = value
            if key == "asks":
                global asks
                asks = value


import time
from threading import Thread

ws = HandleWebsocket()
topics = {
    "id": "tickers",
    "cmd": "sub",
    "args": ["depth.L20.ethusdt"],
}
sub = ws.sub
Thread(target=sub, args=(topics,)).start()
time.sleep(1)
ws.close()

print "=========最终==========="
print bids
print asks


# 下一单
# order_create_param = fcoin.order_create_param('ethusdt', 'buy', 'limit', '452.76', '0.001')
# res = api.orders.create(order_create_param)
# print res
# {u'status': 0, u'data': u'1PmVMo90fHTosZapxjn6DVNeIB6V0p8ZLyJI_3mCh5c='}

#
# # 获取订单
# res = api.orders.get()
# print res
