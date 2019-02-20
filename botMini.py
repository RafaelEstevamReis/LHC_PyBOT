# Needed external libs
# pip install python-telegram-bot | https://python-telegram-bot.org/

# ------------------------------------------

# Adicionamos recursos externos (imports)
from telegram.ext import Updater, CommandHandler
# Dizemos o que o BOT deve fazer
def start(bot, update):
    update.message.reply_text("Hello, World!")

# Criamos uma instância do BOT passando para ele o Token
bot = Updater('TOKEN QUE NÃO DEVE FICAR NO CÓDIGO')

# Explicamos ao BOT que o comando ‘start’ fica no start
bot.dispatcher.add_handler(CommandHandler('start', start))

# Inicia o BOT e manda ele esperar
bot.start_polling()    
bot.idle()

