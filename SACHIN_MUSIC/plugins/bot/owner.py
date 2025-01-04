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
│├ ᴛɢ ɴᴀᴍᴇ - ᴛʜᴜɴᴅᴇʀ ᴘᴀᴘᴀ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ɪsᴛᴋʜᴀʀ ᴀʟᴀᴍ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @THUNDERDEVS
├┤~ @ll_THUNDER_lll
├┤~ @ISTKHAR_143
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @THUNDERDEVS
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗟𝗘𝗚𝗘𝗡𝗗 𝗜𝗦𝗧𝗞𝗛𝗔𝗥 ", url=f"https://t.me/ll_THUNDER_lll")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/THUNDERDEVS"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/THUNDERDEVS"),
          ],
               [
                InlineKeyboardButton("ᴛʜᴜɴᴅᴇʀ ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/THUNDERDEVS"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/purvi_music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/09w9tj.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
