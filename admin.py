from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not Admin.")
        return

    await update.message.reply_text(
        "👑 Admin Panel\n\n"
        "✅ Welcome Admin!"
    )