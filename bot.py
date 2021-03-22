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
	
	if message.chat.type == "group":
		try:
			query = message.text.split()
			coin_symbol = query[1].upper()
			print(coin_symbol)
			crypto_requests = requests.get("https://wavescap.com/api/asset/{}.json".format(coin_symbol))
			crypto_data = crypto_requests.json()
			coin_price = crypto_data["data"]["lastPrice_usd-n"]
			coin_name = crypto_data["name"]
			response = '{} - {} \n ${} \n'.format(coin_symbol,coin_name,coin_price,)
			bot.reply_to(message, response)
		
		except Exception as e:
			print(e)
			response = "Sorry, We do not support this Token/Coin at this Time\n\n Enter '/price Coin Symbol' or Shortcode to get started\n E.g, '/price BTC', ETH, NSBT"
			bot.reply_to(message, response)



# this handles messages in private chats with the bot 
@bot.message_handler(regexp='')
def price_finder(message):
	try:
		coin_symbol = message.text.upper()
		print(coin_symbol)
		crypto_requests = requests.get("https://wavescap.com/api/asset/{}.json".format(coin_symbol))
		crypto_data = crypto_requests.json()
		coin_price = crypto_data["data"]["lastPrice_usd-n"]
		coin_name = crypto_data["name"]
		response = '{} - {} \n ${} \n '.format(coin_symbol,coin_name,coin_price,)
		bot.reply_to(message, response)
	except Exception as e:
		print(e)
		response = "Sorry, We do not support this Token/Coin at this Time\n\n Enter Coin Symbol or Shortcode to get started\n E.g, BTC, ETH, NSBT"
		bot.reply_to(message, response)

	
		
		
# @bot.message_handler(regexp='')
# def send_answer(m):
#     user_msg = 'Hi, it seems you have entered an invalid comman, kindly "/p" with a Crypto Asset to get the price. \n\n Example "/p BTC"'
#     bot.reply_to(m, user_msg)


# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.


bot.polling()