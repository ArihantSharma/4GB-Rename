from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("𝐆𝐢𝐯𝐞 𝐌𝐞 𝐀 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐓𝐨 𝐒𝐞𝐭.\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲:- `/set_caption File Name`")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐀𝐝𝐝𝐞𝐝 ✅")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("𝐘𝐨𝐮 𝐃𝐨𝐧'𝐭 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐀𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐘𝐞𝐭 🙂")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ✅")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<code><u>Your Caption:</code></u>\n\n`{caption}`")
    else:
       await message.reply_text("𝐘𝐨𝐮 𝐃𝐨𝐧'𝐭 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐀𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐘𝐞𝐭 🙂")
          
