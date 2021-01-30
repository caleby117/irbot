from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
 
import logging

TOKEN = '1697331324:AAFj6GPlhH4lNaZ3jslhQrsZfPTTkWJDyXo'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='hello world!')
    return START

def bar(update,context):
    update.message.reply_text('baaar')
    

START, FOO, BAR, GET_SYMPTOMS = range(4)

conv_handler = ConversationHandler(
                    entry_points=[CommandHandler('start', start)], 
                    states = {START : [MessageHandler(Filters.regex('^(foo)$'), bar)]},
                    fallbacks = None
                    )

dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
