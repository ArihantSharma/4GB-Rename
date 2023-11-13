import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','6927866559:AAFCRzLBFtIrotS9iDsGK7DO9H9FPhL9F7c')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", "6263893478"))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["lazyusers"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split(',')

	await message.reply_text(f"⚡️ Aʟʟ IDS : {ids}\n\n⚡️ Total User :- {total_user()}\n\n⚡️ Tᴏᴛᴀʟ Rᴇɴᴀᴍᴇᴅ Fɪʟᴇꜱ :- {total_rename}\nV Tᴏᴛᴀʟ Sɪᴢᴇ Rᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Cʟᴏꜱᴇ Mᴇɴᴜ 🦋", callback_data="cancel")]]) 
                             )
