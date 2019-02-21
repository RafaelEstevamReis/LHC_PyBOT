## Instructions
# Needed external libs
# pip install python-telegram-bot | https://python-telegram-bot.org/

# ------------------------------------------

# Imports para as funções de Log
import logging
# Imports para o Updater (da main) e funcionamento básico do BOT
from telegram.ext import Updater, CommandHandler
#Imports para o BOT receber mensagens além dos comandos
from telegram.ext import MessageHandler, Filters

# Cria um Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Primeira função: a START
# É chamada sempre que alguém dá /start no BOT
def start(bot, update):
    update.message.reply_text("Olá, {}!".format(update.message.from_user.first_name))

 # Função ajuda utilizando MARKDOWN para deixar partes em negrito
 def ajuda(bot, update):
    bot.send_message(chat_id=update.message.chat.id,
                                   text="""*{}* os comandos são:
*/start* para iniciar
*/ajuda* para este menu""".format(update.message.from_user.first_name),
                                   parse_mode=ParseMode.MARKDOWN)
    
# Retorna para o usuário vários dados dele
# Como Nome, ID do usuário, UserName e Tipo
# O 'Tipo' identifica o tipo do CHAT, se é privado, Grupo, etc...
def userInfo(bot, update):
    update.message.reply_text(
        'Nome: {0} ({1}) UserName: {3} Tipo: {2}'.format(update.message.from_user.first_name,
            update.message.from_user.id,
            update.message.chat.type,
            update.message.from_user.username))

def receberStiker(bot, update):
    # Obtém o código (ID) do sticker recebido
    Id_do_sticker = update.message.sticker.file_id
    # Envia o código do 
    update.message.reply_text("Id do sticker: {}".format(Id_do_sticker))
    # Retorna o mesmo sticker
    update.message.reply_sticker(stickerid)

    
def echo(bot, update):
    update.message.reply_text(update.message.text)
    
    
# Inicializa o BOT numa função main
def main():
    token = 'NUNCA DEIXE NO CÓDIGO'

    # Cria um bot 
    bot = Updater(token)
    
    # Adiciona todos os comandos que o bot vai ter
    
    #  Função start mostra o uso básico de responder uma mensagem com o nome da pessoa que chamou o BOT
    bot.dispatcher.add_handler(CommandHandler('start', start))
    #  Função start mostra o uso básico de MarkDown mostrando como usar negrito
    bot.dispatcher.add_handler(CommandHandler('ajuda', ajuda))
    #  Função mostra como obter várias informações sobre o usuário e o CHAT
    bot.dispatcher.add_handler(CommandHandler('info', userInfo))

    
    #Adiciona funções para o BOT sem ser recebimento de comandos
    # Lembrando que num chat em grupo o BOT, por padrão, recebe apenas comandos e mensagens direcionadas a ele (mencionando com @ ou dando Responder)
    
    # Função para o bot receber Stickers
    bot.dispatcher.add_handler(MessageHandler(Filters.sticker, receberStiker))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    
    # Manda o bot comaçar a funcionar
    bot.start_polling()

    # Roda o bot até apertar Control+C
    bot.idle()

    
# Chama a função Main
if __name__ == '__main__':
    main()
