import requests
import telebot
from colorama import Fore, Style, init
from telebot import types

init(autoreset=True)

API_TOKEN = '8060601944:AAF3jsjVcbYrdvrxepFqKi_RdQpiWjynBxk'
bot = telebot.TeleBot(API_TOKEN)

def send_telegram_message(user_id, message):
    bot.send_message(user_id, message)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    image_url = "https://iili.io/2c5Wfsf.md.jpg"
    bot.send_photo(user_id, image_url)
    
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton(text="𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🙀", url="https://t.me/GODXNEXU")
    markup.add(channel_button)
    developer_button = types.InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥 ☠️", url="https://t.me/NEXUXMANAGER")
    markup.add(developer_button)
    
    bot.send_message(user_id, "Welcome to Instagram Password Reset Bot! 🌟\n\nPlease enter your email or username to reset your password:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_user_input(message):
    user_id = message.chat.id
    email_or_username = message.text.strip()
    bot.send_message(user_id, "Please wait, your request is processing... ⏳")

    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    payload = f"email_or_username={email_or_username}"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'x-csrftoken': "r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc",
        'x-requested-with': "XMLHttpRequest",
        'x-ig-app-id': "936619743392459",
        'referer': "https://www.instagram.com/accounts/password/reset/",
        'Cookie': "mid=ZqPYMgABAAE1FS3FyA2mTh6D4nSn; csrftoken=r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            bot.send_message(user_id, f"🎉 The password reset code has been sent successfully to {email_or_username}!")
        else:
            bot.send_message(user_id, f"❌ Error: {response.status_code}\n🛠 Message: {response.text}")
    except Exception as e:
        bot.send_message(user_id, f"❌ Error: {e}")

print("Bot is running...")
bot.polling()