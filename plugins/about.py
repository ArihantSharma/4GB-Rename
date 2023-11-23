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
	await message.reply_text(f"🤖 Mʏ Nᴀᴍᴇ : [Pʀᴇᴍɪᴜᴍ Rᴇɴᴀᴍᴇʀ](https://t.me/public_renamerbot)

👑 Oᴡɴᴇʀ :  [₭𝐚𝐋𝐋Ꮼ𝐚 ...♡](https://t.me/mr_kallua)

🧑🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : [「 #𝑷𝑹𝑶𝑭𝑬𝑺𝑺𝑶𝑹」🪐](https://t.me/PROFE07XHBOT)

👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : [Nᴏᴏʙs Eᴠᴇʀʏᴡʜᴇʀᴇ](https://t.me/Noobseverywhere) """\n\n 𝗧𝗼𝘁𝗮𝗹 𝗥𝗲𝗻𝗮𝗺𝗲𝗱 𝗙𝗶𝗹𝗲𝘀:- {total_rename}\n 𝗧𝗼𝘁𝗮𝗹 𝗦𝗶𝘇𝗲 𝗥𝗲𝗻𝗮𝗺𝗲𝗱 :- {humanbytes(int(total_size))} \n\n 𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 ₭🅐︎🅛︎🅛︎Ꮼ🅐︎ ...♡ 🤝",quote=True)
