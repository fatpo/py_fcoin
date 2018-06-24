# coding=utf-8

import fcoin

key = ''
secret = ''

api = fcoin.authorize(key, secret)
print api.accounts_balance
