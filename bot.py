## Instructions
# Needed external libs
# pip install python-telegram-bot | https://python-telegram-bot.org/

# ------------------------------------------

## Imports

import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text("Hello World, {}!".format(update.message.from_user.first_name))

    
def main():
    token = 'NUNCA DEIXE NO CÓDIGO'

    # Create the Updater and pass it your bot's token.
    updater = Updater(token)
    
    # Add the commands as callbacks
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
