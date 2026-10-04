import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
OWNER_CHAT_ID = int(os.environ["OWNER_CHAT_ID"])

async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.forward(chat_id=OWNER_CHAT_ID)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL & ~filters.COMMAND, forward_to_owner)
)

print("Bot is running...")
app.run_polling()
