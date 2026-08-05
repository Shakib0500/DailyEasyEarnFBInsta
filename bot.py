from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import TOKEN, ADMIN_ID
from database import add_user, get_balance
from admin import admin
from settings import (
    REFERRAL_BONUS,
    TASK_REWARD,
    MIN_WITHDRAW,
    WITHDRAW_METHOD,
)

menu = [
    ["💰 Balance", "👥 Referral"],
    ["📋 Task", "📤 Withdraw"],
    ["ℹ️ Help"],
]
CHANNEL_LINK = "https://t.me/FBInstaVault24"

async def verify_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        user_id = query.from_user.id

        member = await context.bot.get_chat_member(
            chat_id="@FBInstaVault24",
            user_id=user_id
        )

        if member.status in ["member", "administrator", "creator"]:
            await query.message.reply_text(
                "✅ Join Verified!\n\nWelcome to DailyEasyEarnFBInsta 🎉"
            )
        else:
            await query.message.reply_text(
                "❌ আগে Channel Join করুন।"
            )

    except Exception as e:
        await query.message.reply_text(
            f"❌ Verify Error:\n{e}"
        )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)

    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

    channel_button = [
    [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
    [InlineKeyboardButton("✅ Verify Join", callback_data="verify")]
]

    inline_markup = InlineKeyboardMarkup(channel_button)

    text = f"""
👋 Welcome {update.effective_user.first_name}!

🎉 Welcome to DailyEasyEarnFBInsta

📢 Please join our channel.
"""

    await update.message.reply_text(
        text,
        reply_markup=inline_markup
    )

    await update.message.reply_text(
        "👇 Bot Menu:",
        reply_markup=keyboard
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "💰 Balance":
        balance = get_balance(update.effective_user.id)
        await update.message.reply_text(
            f"💰 Balance: ${balance:.2f} USD"
        )

    elif msg == "👥 Referral":
        await update.message.reply_text(
            f"👥 Your Referral Link:\n"
            f"https://t.me/FBInstaEasyEarnBot?start={update.effective_user.id}\n\n"
            f"🎁 Referral Bonus: ${REFERRAL_BONUS:.2f} USDT"
        )

    elif msg == "📋 Task":
        await update.message.reply_text(
            f"📋 Task Reward: ${TASK_REWARD:.2f} USDT"
        )

    elif msg == "📤 Withdraw":
        balance = get_balance(update.effective_user.id)

        if balance < MIN_WITHDRAW:
            await update.message.reply_text(
                f"❌ Minimum Withdraw: ${MIN_WITHDRAW:.2f}\n"
                f"💰 Your Balance: ${balance:.2f}"
            )
        else:
            await update.message.reply_text(
                f"💳 Withdraw Method: {WITHDRAW_METHOD}\n\n"
                "Send your wallet address to continue."
            )

    elif msg == "ℹ️ Help":
        await update.message.reply_text(
            "ℹ️ Help Center\n\n"
            "👋 Welcome to DailyEasyEarnFBInsta\n\n"
            "📋 Complete tasks to earn rewards.\n"
            "👥 Invite friends to earn referral bonuses.\n"
        "💰 Minimum Withdraw: $0.20 USDT\n"
        f"💳 Payment Method: {WITHDRAW_METHOD}\n\n"
        "📞 Contact Admin: @Dmitri_rw1"
    )

async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ref_bonus":
        await query.message.reply_text(
            f"👥 Current Referral Bonus: ${REFERRAL_BONUS:.2f} USDT"
        )

    elif query.data == "task_reward":
        await query.message.reply_text(
            f"🎯 Current Task Reward: ${TASK_REWARD:.2f} USDT"
        )

    elif query.data == "min_withdraw":
        await query.message.reply_text(
            f"💸 Minimum Withdraw: ${MIN_WITHDRAW:.2f} via {WITHDRAW_METHOD}"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CallbackQueryHandler(admin_buttons))
app.add_handler(CallbackQueryHandler(verify_join, pattern="verify"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Bot is running...")
app.run_polling()