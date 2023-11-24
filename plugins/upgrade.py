"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """
 🔹𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫 𝐏𝐥𝐚𝐧 𝟐𝟎ɢʙ/ᴅᴀʏ
🔹𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐏𝐥𝐚𝐧 𝟓𝟎ɢʙ/ᴅᴀʏ
 
Tʜɪs Bᴏᴛ Is Tᴏᴛᴀʟʟʏ Fʀᴇᴇ Fᴏʀ Aʟʟ Bᴜᴛ Aᴛ Fɪʀsᴛ Yᴏᴜ Nᴇᴇᴅ Tᴏ Rᴇғᴇʀ Tᴡᴏ Fʀɪᴇɴᴅs Aɴᴅ Tʜᴇɴ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Yᴏᴜʀ Pʟᴀɴ Wɪʟʟ Bᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Pʀᴇᴍɪᴜᴍ 🤩

/refer 𝗙ᴏʀ 𝗥ᴇғᴇʀ ☑️

𝗦ʜᴀʀᴇ 𝗔ɴᴅ 𝗦ᴜᴘᴘᴏʀᴛ ❤️🙏"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🗿 Cᴏɴᴛᴀᴄᴛ",url = "https://t.me/mr_kallua"), 
        		        InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """
 🔹𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫 𝐏𝐥𝐚𝐧 𝟐𝟎ɢʙ/ᴅᴀʏ
🔹𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐏𝐥𝐚𝐧 𝟓𝟎ɢʙ/ᴅᴀʏ
 
Tʜɪs Bᴏᴛ Is Tᴏᴛᴀʟʟʏ Fʀᴇᴇ Fᴏʀ Aʟʟ Bᴜᴛ Aᴛ Fɪʀsᴛ Yᴏᴜ Nᴇᴇᴅ Tᴏ Rᴇғᴇʀ Tᴡᴏ Fʀɪᴇɴᴅs Aɴᴅ Tʜᴇɴ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Yᴏᴜʀ Pʟᴀɴ Wɪʟʟ Bᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Pʀᴇᴍɪᴜᴍ 🤩

/refer 𝗙ᴏʀ 𝗥ᴇғᴇʀ ☑️

𝗦ʜᴀʀᴇ 𝗔ɴᴅ 𝗦ᴜᴘᴘᴏʀᴛ ❤️🙏"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🗿 Cᴏɴᴛᴀᴄᴛ ",url = "https://t.me/mr_kallua"), 
        		        InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
