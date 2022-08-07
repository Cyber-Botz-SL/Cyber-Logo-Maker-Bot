import aiohttp
from pyrogram import Client
from config import *

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("[INFO]: STARTING Cyber Logo Maker Bot...")
app.start()

print("[INFO]: STARTING Cyber Logo Maker Bot...")
session = aiohttp.ClientSession()
