from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʟᴇɢᴇɴᴅ ᴍɪᴄᴋᴇʏ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴛᴏsᴜ ᴍᴇᴍᴏɴ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @THE_INCRICIBLE
├┤~ @LEGEND_MICKEY
├┤~ @ABOUT_GODFATHER
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @LEGEND_MICKEY
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗟𝗘𝗚𝗘𝗡𝗗 𝗠𝗜𝗖𝗞𝗘𝗬", url=f"https://t.me/LEGEND_MICKEY")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/THE_INCRICIBLE"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/THE_INCRICIBLE"),
          ],
               [
                InlineKeyboardButton("ɪɴᴄʀɪᴄɪʙʟᴇ ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/THE_INCRICIBLE"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/ZOYUMUSICBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0wtv2m.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
