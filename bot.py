from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7975587876:AAEPJnx7pt-qeqM41ijxg6dRU_wfzgEx1aA"

CHANNEL_LINKS = """🔗 قنواتنا الرسمية:
1️⃣ يوتيوب: [Popxev Games](https://youtube.com/@popxevgames-v1w?si=QulhnL1ZbhMU3mDK)
2️⃣ إنستجرام: [Popxev Games](https://www.instagram.com/popxev_games?igsh=anNwdzR5dXFwc2E4)
3️⃣ فيسبوك: [Popxev Games](https://www.facebook.com/share/1Dsxdcv7yN/)
4️⃣ جروب تيليجرام: [اضغط هنا](https://t.me/Popxevgamesgroup)
5️⃣ ديسكورد: [انضم إلينا](https://discord.gg/hK33DD74QN)
"""

custom_replies = {
    "مرحبا": "أهلًا وسهلًا بك! 😊",
    "كيف حالك؟": "أنا بخير، وأنت؟",
    "ما اسمك؟": "أنا بوت Popxev Games! 🤖"
}

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text(f"مرحبًا {update.effective_user.first_name}! 🎮\n{CHANNEL_LINKS}")

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("🔹 أوامر البوت:\n/start - روابط القنوات 📢\n/help - المساعدة ℹ️")

async def contact(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("💬 للتواصل معنا، يمكنك إرسال رسالة عبر تيليجرام إلى: @Popxev_games")

async def discord(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("🎮 انضم إلى سيرفر ديسكورد الخاص بنا:\n🔗 [اضغط هنا](https://discord.gg/hK33DD74QN)")

async def handle_messages(update: Update, context: CallbackContext.DEFAULT_TYPE):
    text = update.message.text
    reply = custom_replies.get(text, "عذرًا، لا أفهم هذا الأمر! 🤔")
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("discord", discord))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
