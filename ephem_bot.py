# -*- coding: utf-8 -*-
import logging
from key import API_KEY
import ephem 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

now = datetime.datetime.now()

planets_dict = {"Mercury" : ephem.Mercury(),
                "Venus" : ephem.Venus(),
                "Mars" : ephem.Mars(),
                "Jupiter" : ephem.Jupiter(), 
                "Saturn" : ephem.Saturn(),
                "Uranus" : ephem.Uranus(),
                "Neptune" : ephem.Neptune(),
                "Pluto" : ephem.Pluto()
                }

# planets_dict["mercury"](sun) == ephem.Mercury(sun)

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
         'urllib3_proxy_kwargs':{'username':"learn", "password": "python"}}


logging.basicConfig(format='%(name)s - %(levelname)s -%(message)s',
                        level=logging.INFO,
                        filename='bot.log')

def start_handler(bot, update):
    text = '/start initiated'
    # print(text)
    # print(update)
    # if update['chat']['id'] == '585766625':
    update.message.reply_text(text)
    # else:zz
    #     update.message.reply_text(text)

def planet2constellation(bot, update):
    text = update.message.text.split()
    # print(text)
    # print(text[1])
    # planet = text(1)
    planet = planets_dict.get(text[1])
    # print(f'planet = ', planet)
    # u = ephem.Uranus()
    # u.compute(now)
    # print(ephem.constellation(u))
    # print(ephem.constellation(u))
    # print(ephem.constellation(planet))
    if planet is None:
        # print ('none')
        update.message.reply_text("Нет такой планеты!")
        # constellation = ephem.constellation(planet)
        # print(constellation)
        # update.message.reply_text(constellation)
    else:
        # print('true')
        # update.message.reply_text("Нет такой планеты!")
        planet.compute(now)
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(constellation)    
       # d = ephem.date(date())
    


def talk_to_me(bot,update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CommandHandler("planet", planet2constellation))
    # dp.add_handler(CommandHandler("planet" + input(' '), planet2constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()



main()
