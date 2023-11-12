"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Fʀᴇᴇ Uꜱᴇʀ Pʟᴀɴ**
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷.𝟸GB Aᴛ 𝟶 ₹
 
 🪙 𝗦𝗶𝗹𝘃𝗲𝗿 𝗧𝗶𝗲𝗿
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷𝟶GB Aᴛ 𝟸 ₹ 
 
 💫 𝗚𝗼𝗹𝗱 𝗧𝗶𝗲𝗿
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟻𝟶ɢʙ Aᴛ 𝟹 ₹
 
 💎 𝗗𝗶𝗮𝗺𝗼𝗻𝗱 𝗧𝗶𝗲𝗿 
 Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷𝟶𝟶ɢʙ Aᴛ 𝟺 ₹ 

 **Pᴀʏ Uꜱɪɴɢ Uᴘɪ Iᴅ** ```mekhaleanish@okicici```
 <a href='https://t.me'>𝐐𝐑 𝐂𝐎𝐃𝐄 𝐇𝐄𝐑𝐄</a> 
 
**Sᴇɴᴅ Sᴄʀᴇᴇɴꜱʜᴏᴛꜱ Tᴏ** @mr_kallua 🤝"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🗿Oᴡɴᴇʀ",url = "https://t.me/mr_kallua"), 
        		        InlineKeyboardButton("✖️Cᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Fʀᴇᴇ Uꜱᴇʀ Pʟᴀɴ**
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷.𝟸GB Aᴛ 𝟶 ₹
 
 🪙 𝗦𝗶𝗹𝘃𝗲𝗿 𝗧𝗶𝗲𝗿
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷𝟶GB Aᴛ 𝟸 ₹ 
 
 💫 𝗚𝗼𝗹𝗱 𝗧𝗶𝗲𝗿
Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟻𝟶ɢʙ Aᴛ 𝟹 ₹
 
 💎 𝗗𝗶𝗮𝗺𝗼𝗻𝗱 𝗧𝗶𝗲𝗿 
 Dᴀɪʟʏ Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ 𝟷𝟶𝟶ɢʙ Aᴛ 𝟺 ₹ 

 **Pᴀʏ Uꜱɪɴɢ Uᴘɪ Iᴅ** ```mekhaleanish@okicici```
 <a href='https://t.me'>𝐐𝐑 𝐂𝐎𝐃𝐄 𝐇𝐄𝐑𝐄</a> 
 
**Sᴇɴᴅ Sᴄʀᴇᴇɴꜱʜᴏᴛꜱ Tᴏ** @mr_kallua 🤝"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🗿Oᴡɴᴇʀ",url = "https://t.me/mr_kallua"), 
        		        InlineKeyboardButton("✖️Cᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
