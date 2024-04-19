from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("27455984")
APP_HASH = os.environ.get("62d5f68ce2e9189636967120220f5755")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
