# coding=utf-8
import fcoin
from conf import config

api = fcoin.authorize(config.key, config.secret)
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

print "=========阶段 1 ==========="
print "买家愿意买的最高价位：bids>>>>>", bids
print "卖家愿意卖的最低价位：asks>>>>>", asks

print "=========阶段 2 ==========="
buy_price = str(asks[0])
sell_price = str(bids[0])
print "那我们买出的价格：", buy_price
print "那我们卖出的价格：", sell_price

# 下一买单
# order_create_param = fcoin.order_create_param('ethusdt', 'buy', 'limit', '452.76', '0.001')
# res = api.orders.create(order_create_param)
# print res
# {u'status': 0, u'data': u'1PmVMo90fHTosZapxjn6DVNeIB6V0p8ZLyJI_3mCh5c='}


# 下一卖单
order_create_param = fcoin.order_create_param('ethusdt', 'sell', 'limit', sell_price, '0.01')
res = api.orders.create(order_create_param)
print res

#
# # 获取订单
# res = api.orders.get()
# print res
