from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import ADMIN_ID

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not Admin.")
        return

    keyboard = [
        [InlineKeyboardButton("💰 Change Referral Bonus", callback_data="ref_bonus")],
        [InlineKeyboardButton("🎯 Change Task Reward", callback_data="task_reward")],
        [InlineKeyboardButton("💸 Change Minimum Withdraw", callback_data="min_withdraw")]
    ]

    await update.message.reply_text(
        "👑 Admin Panel",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )