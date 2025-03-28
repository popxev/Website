from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '7628635799:AAEvKuQsHdJJZtw_4ZCaPOJX73p8QSb2z2Q'

blocked_words = [
    "للانضمام", "join", "إعلانات", "لشراء", "رابط قروب", "انضم", "نيك", "شرموط", "كس", "اباحي",
    "adult", "xxx", "www", "http", "https", "porn"
]

def filter_message(update: Update, context: CallbackContext):
    message = update.message.text.lower()
    for word in blocked_words:
        if word in message:
            try:
                update.message.delete()
                print("تم مسح رسالة تحتوي على كلمات محظورة.")
            except Exception as e:
                print(f"حدث خطأ أثناء مسح الرسالة: {e}")
            break

def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أنا بوت المسح، سأقوم بمسح الرسائل المخالفة.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, filter_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
