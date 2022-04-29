import telebot
from telebot import types
import requests
import os

TOKEN = os.environ.get("TOKEN")
TRIGGER_TOKEN = os.environ.get("TRIGGER_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Для запуска pipeline наберите /run_pipeline')


@bot.message_handler(commands=['run_pipeline'])
def start(message):
    rsp = requests.post(f'https://gitlab.smartworld.team/api/v4/projects/332/trigger/pipeline?token={TRIGGER_TOKEN}&ref=develop')
    text = f"Запуск Pipeline из ветки Develop. Trigger Response {rsp.status_code}"
    bot.send_message(message.chat.id, text)
    


bot.polling(non_stop=True)