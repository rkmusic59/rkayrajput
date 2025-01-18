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
│├ ᴛɢ ɴᴀᴍᴇ - ꪜ 𝛊 ɭ ɭ ᧘ 𝛊 𝛈
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴀᴋꜱʜɪᴛ ᴛʜᴀᴋᴜʀ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @iamakki001
├┤~ @iamvillain77
├┤~ @oldskoolgc
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @iamakki001
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" ꪜ 𝛊 ɭ ɭ ᧘ 𝛊 𝛈 ", url=f"https://t.me/iamakki001")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/iamakki001"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/iamvillain77"),
          ],
               [
                InlineKeyboardButton("˹ᴠɪʟʟᴀɪɴ ꭙ ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/iamvillain77"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/radha_music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/pcncfx.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
