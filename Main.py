import telebot

# උඹේ අලුත්ම Token එක
TOKEN = '8625934766:AAGATqJ3uyK_tC-r_kUhGlrKMi25PNkuqkw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "අඩෝ Basilu! මම දැන් Railway එකේ ඉඳන් වැඩ! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "මම වැඩ මචං: " + message.text)

bot.infinity_polling()
