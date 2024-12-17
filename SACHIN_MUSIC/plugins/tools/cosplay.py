import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from SACHIN_MUSIC import app
from config import BOT_USERNAME

SACHIN = [
    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✙", url=f"https://t.me/SUCHI_MUSIC_BOT?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/THE_INCRICIBLE"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ ๛s ᴜ ᴄ ʜ ɪ ༗", reply_markup=InlineKeyboardMarkup(SACHIN),)
