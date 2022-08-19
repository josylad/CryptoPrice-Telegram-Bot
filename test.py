#!/usr/bin/env python
import os
import telebot 
import logging
from telebot import types
from decouple import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


CMC_API_KEY = config("CMC_KEY")
coin_symbol = "A4h9aifPtz371noBA1Khi2Eb4L3Vzf8LC8PtF4QysEd9"

cmc_url = 'https://api.wavesplatform.com/v0/pairs/{}/DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'.format(coin_symbol)

headers = {
  'accepts': 'application/json',
}


session = Session()
session.headers.update(headers)


response = session.get(cmc_url)
data = json.loads(response.text)
# print(data)

if data["amountAsset"] == "A4h9aifPtz371noBA1Khi2Eb4L3Vzf8LC8PtF4QysEd9":
  coin_name = 'FROE'
  print(coin_name)

  try:
    price = data['data']["lastPrice"]
    volume = data['data']["volume"]
    round_coin_price = round(price,7)

    response = '<b>{}</b> \n Price: ${} USD \n 24h volume: ${} USD \n \n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'.format(coin_name,round_coin_price,volume)
    print(response)

  except (Exception, KeyError) as e:
    print(e)
    response = '''Sorry, We do not support this Token/Coin at this Time\n\n Enter '/price Coin Symbol' or Shortcode to get started\n E.g, '/price BTC', ETH, NSBT \n\n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance</a>'''
