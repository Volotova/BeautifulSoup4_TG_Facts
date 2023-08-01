import requests, random, telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.litres.ru/book/l-kremer/1000-udivitelnyh-i-neveroyatnyh-faktov-kotoryh-vy-ne-znali-24530166/chitat-onlayn/'
Token = '6606473700:AAHzy32TYA0M_bTdZZJrYdJ4JZGJuRAMwfE'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    facts = soup.find('div', class_='online_reading').find_all('p')
    return [text.text for text in facts]

list_of_facts = parser(URL)
random.shuffle(list_of_facts)

bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['Start'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуй! Чтобы узнать интересный факт введите любую цифру: ')

@bot.message_handler(content_types=['text'])
def facts(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_facts[0])
        del list_of_facts[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')

bot.polling()