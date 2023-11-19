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
	await message.reply_text(f"\n🗿𝗢𝘄𝗻𝗲𝗿 :- <a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>\n𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 :- 𝗣𝘆𝘁𝗵𝗼𝗻𝟯\n𝗟𝗶𝗯𝗿𝗮𝗿𝘆 :- 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝟮.𝟬\n\n 𝗧𝗼𝘁𝗮𝗹 𝗥𝗲𝗻𝗮𝗺𝗲𝗱 𝗙𝗶𝗹𝗲𝘀:- {total_rename}\n 𝗧𝗼𝘁𝗮𝗹 𝗦𝗶𝘇𝗲 𝗥𝗲𝗻𝗮𝗺𝗲𝗱 :- {humanbytes(int(total_size))} \n\n 𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 ₭🅐︎🅛︎🅛︎Ꮼ🅐︎ ...♡ 🤝 , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url='https://t.me/Noobseverywhere")]]) "                                              
            ,quote=True)
