from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
from telegram.error import *
import logging
import youtube_dl
import os
import sys
import subprocess

updater=Updater(token='739431728:AAFnFxS4U5XPh49yV5R-1rXoZJxhH4zyfvU',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    print ("New User detected")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome To HurakenTunes\n\nHow to use\nShare the link of the youtube video you wish to convert\nDo wait the server is not always running\n\nSincerely,\nHuraken.")
def dl(update, context):
    p=update.message.text
    p=p.strip('\n')
    print (p)
    if (not "https://youtu.be" in p) :
            context.bot.send_message(chat_id=update.effective_chat.id, text='Wrong Link')
    else :        
        subprocess.call(["youtube-dl --merge-output-format mkv "+p],shell=True)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Checking Link")
        x=""
        list=os.listdir('.')
        for name in list :
                if( ".mkv" in name):
                        x=str(name)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Uploading Video")
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(x, 'rb'))
        os.system("rm *.mkv")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Thank you for using HurakenTube")
        
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, dl)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()

      
    
 
