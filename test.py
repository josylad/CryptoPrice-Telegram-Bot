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

cmc_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
cmc_parameters = {
  'symbol':'TXZ',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CMC_API_KEY,
}


session = Session()
session.headers.update(headers)

try:
    response = session.get(cmc_url, params=cmc_parameters)
    data = json.loads(response.text)
    #   print(data)
    if data['data'] == True:
        price = data['data']['txz']['quote']['USD']['price']
        volume = data['data']['txz']['quote']['USD']['volume_24h']
        price = data['data']['txz']['quote']['USD']['price']
        volume = data['data']['txz']['quote']['USD']['volume_24h']
        round_coin_price = round(price,7)
        coin_name = data['data']['BTC']['name']
        print(price)
        print(coin_name)
    else:
        print("Invalid coin")

except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
  print(e)