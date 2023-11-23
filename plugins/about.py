import os 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6927866559:AAFCRzLBFtIrotS9iDsGK7DO9H9FPhL9F7c')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**🤖 Mʏ Nᴀᴍᴇ :"" <a href='https://t.me/public_renamerbot'>Pʀᴇᴍɪᴜᴍ Rᴇɴᴀᴍᴇʀ</a>\n**👑 Oᴡɴᴇʀ :**  <a href='https://t.me/mr_kallua'>**₭𝐚𝐋𝐋Ꮼ𝐚 ...♡**</a>\n**🧑🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ :** <a href='https://t.me/PROFE07XHBOT'>**「 #𝑷𝑹𝑶𝑭𝑬𝑺𝑺𝑶𝑹」🪐**</a>\n**👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ :** <a href='https://t.me/Noobseverywhere'>**Nᴏᴏʙs Eᴠᴇʀʏᴡʜᴇʀᴇ**</a>\n\n **Tᴏᴛᴀʟ Rᴇɴᴀᴍᴇᴅ Fɪʟᴇs** :- {total_rename}\n **Tᴏᴛᴀʟ Sɪᴢᴇ Rᴇɴᴀᴍᴇᴅ :-** {humanbytes(int(total_size))} \n\n 𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 ₭🅐︎🅛︎🅛︎Ꮼ🅐︎ ...♡ 🤝",quote=True)
