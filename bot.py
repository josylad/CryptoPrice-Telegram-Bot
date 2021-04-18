#!/usr/bin/env python
import os
import telebot 
import logging
from telebot import types
from decouple import config
import requests



TOKEN = config("TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML") # You can set parse_mode by default. HTML or MARKDOWN


# This will start the bot for a new user 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	cid = message.chat.id
	bot.reply_to(message, "Welcome to CryptoStats, this Bot provides you with Up-to-date Cryptocurrencies Price\n\n Type 'Waves' to get Waves Price and you can do the Same for All Cryptocurrencies")



# this handles messages from group chats 
@bot.message_handler(commands=['price', 'p', 'waves'])
def price_finder(message):
	
	if message.chat.type == "group" or message.chat.type == "supergroup":
		try:
			query = message.text.split()
			coin_symbol = query[1].upper()
			print(coin_symbol)
			crypto_requests = requests.get("https://wavescap.com/api/asset/{}.json".format(coin_symbol))
			crypto_data = crypto_requests.json()
			coin_price = crypto_data["data"]["lastPrice_usd-n"]
			round_coin_price = round(coin_price,7)
			coin_name = crypto_data["name"]
			response = '<b>{} - {}</b> \n Price: ${} USD \n 24h volume: ${} USD \n \n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'.format(coin_symbol,coin_name,round_coin_price,volume)
			bot.reply_to(message, response, disable_web_page_preview=True)
		
		except Exception as e:
			print(e)
			response = '''Sorry, We do not support this Token/Coin at this Time\n\n Enter '/price Coin Symbol' or Shortcode to get started\n E.g, '/price BTC', ETH, NSBT \n\n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'''
			bot.reply_to(message, response, disable_web_page_preview=True)


	if message.chat.type == "private":
		try:
			query = message.text.split()
			coin_symbol = query[1].upper()
			print(coin_symbol)
			crypto_requests = requests.get("https://wavescap.com/api/asset/{}.json".format(coin_symbol))
			crypto_data = crypto_requests.json()
			coin_price = crypto_data["data"]["lastPrice_usd-n"]
			round_coin_price = round(coin_price,7)
			coin_name = crypto_data["name"]
			response = '<b>{} - {}</b> \n Price: ${} USD \n 24h volume: ${} USD \n \n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'.format(coin_symbol,coin_name,round_coin_price,volume)
			bot.reply_to(message, response, disable_web_page_preview=True)
		
		except Exception as e:
			print(e)
			response = '''Sorry, We do not support this Token/Coin at this Time\n\n Enter '/price Coin Symbol' or Shortcode to get started\n E.g, '/price BTC', ETH, NSBT \n\n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'''
			bot.reply_to(message, response, disable_web_page_preview=True)



# this handles messages in private chats with the bot 
@bot.message_handler(regexp='')
def price_finder(message):
	if message.chat.type == "private":
		try:
			coin_symbol = message.text.upper()
			print(coin_symbol)
			crypto_requests = requests.get("https://wavescap.com/api/asset/{}.json".format(coin_symbol))
			crypto_data = crypto_requests.json()
			coin_price = crypto_data["data"]["lastPrice_usd-n"]
			volume = crypto_data["24h_vol_usd-n"]
			round_coin_price = round(coin_price,7)
			coin_name = crypto_data["name"]
			response = '<b>{} - {}</b> \n Price: ${} USD \n 24h volume: ${} USD \n \n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'.format(coin_symbol,coin_name,round_coin_price,volume)
			bot.reply_to(message, response, disable_web_page_preview=True)
		except Exception as e:
			print(e)
			response = '''Sorry, We do not support this Token/Coin at this Time\n\n Enter '/price Coin Symbol' or Shortcode to get started\n E.g, '/price BTC', ETH, NSBT \n\n <a href="https://www.binance.com/en/register?ref=UM7SAUZG">💰 Trade Crypto on Binance (-10% transaction fee)</a>'''
			bot.reply_to(message, response, disable_web_page_preview=True)

	
		
		
# @bot.message_handler(regexp='')
# def send_answer(m):
#     user_msg = 'Hi, it seems you have entered an invalid comman, kindly "/p" with a Crypto Asset to get the price. \n\n Example "/p BTC"'
#     bot.reply_to(m, user_msg)


# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.


bot.polling(none_stop=True)