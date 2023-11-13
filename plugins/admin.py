from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
ADMIN = int(os.environ.get("ADMIN", 6263893478))
log_channel = int(os.environ.get("LOG_CHANNEL", "-1002066295284"))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("𝐔𝐬𝐞𝐫 𝐍𝐨𝐭𝐟𝐢𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 😉")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("𝐔𝐬𝐞𝐫 𝐍𝐨𝐭 𝐍𝐨𝐭𝐟𝐢𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 😔")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("🦋 𝗦𝗲𝗹𝗲𝗰𝘁 𝗣𝗹𝗮𝗻 𝗧𝗼 𝗨𝗽𝗴𝗿𝗮𝗱𝗲...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("🪙 Sɪʟᴠᴇʀ", callback_data="vip1")
				   ], [
					InlineKeyboardButton("💫 Gᴏʟᴅ", callback_data="vip2")
				   ], [
					InlineKeyboardButton("💎 Dɪᴀᴍᴏɴᴅ", callback_data="vip3")
					]]))



@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
	await message.reply_text(" Cᴇᴀꜱᴇ Pᴏᴡᴇʀ Mᴏᴅᴇ ", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("•× Lɪᴍɪᴛ 𝟷𝟶𝟶ᴍʙ ×•", callback_data="cp1"),
				    InlineKeyboardButton("•×  ×•", callback_data="cp2")
				   ], [
				    InlineKeyboardButton("•••× Cᴇᴀꜱᴇ Aʟʟ Pᴏᴡᴇʀ ×•••", callback_data="cp3")
				    ]]))


@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"Dᴏ Yᴏᴜ Rᴇᴀʟʟʏ Wᴀɴᴛ Tᴏ Rᴇꜱᴇᴛ Dᴀɪʟʏ Lɪᴍɪᴛ Tᴏ Dᴇғᴀᴜʟᴛ Dᴀᴛᴀ Lɪᴍɪᴛ 𝟷.𝟸GB ?",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• YES ! Sᴇᴛ Aꜱ Dᴇғᴀᴜʟᴛ •",callback_data = "dft")],
				   [InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ",callback_data = "cancel")]
				   ]))

        			
@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"🪙 **Sɪʟᴠᴇʀ**")
	addpre(int(user_id))
	await update.message.edit("Aᴅᴅᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶 GB 🤝")
	await bot.send_message(user_id,"Hᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ ꜱɪʟᴠᴇʀ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")
	await bot.send_message(log_channel,f"⚡️ Pʟᴀɴ Uᴘɢʀᴀᴅᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ 💥\n\nHᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ ꜱɪʟᴠᴇʀ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")
	
@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"💫 **Gᴏʟᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶 GB 🤝")
	await bot.send_message(user_id,"Hᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Gᴏʟᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"💎 **Dɪᴀᴍᴏɴᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶 GB 🤝")
	await bot.send_message(user_id,"Hᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Dɪᴀᴍᴏɴᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

# CEASE POWER MODE @LAZYDEVELOPER

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 524288000
	uploadlimit(int(user_id),524288000)
	usertype(int(user_id),"**Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ\n")
	await bot.send_message(user_id,"⚠️ Wᴀʀɴɪɴɢ ⚠️\n\n- Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ\nYᴏᴜ Cᴀɴ Oɴʟʏ Uꜱᴇ 𝟻𝟶𝟶ᴍʙ/ᴅᴀʏ Fʀᴏᴍ Dᴀᴛᴀ Qᴏᴛᴀ.\nCʜᴇᴄᴋ Yᴏᴜʀ Pʟᴀɴ Hᴇʀᴇ - /myplan\n- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 🦋<a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>🦋")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 104857600
	uploadlimit(int(user_id), 104857600)
	usertype(int(user_id),"**Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ Tᴏ Lᴠ-𝟸**")
	addpre(int(user_id))
	await update.message.edit("Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ Tᴏ Lᴇᴠᴇʟ 𝟸\nTʜᴇ Uꜱᴇʀ Cᴀɴ Oɴʟʏ Uꜱᴇ 𝟷𝟶𝟶ᴍʙ/ᴅᴀʏ Fʀᴏᴍ Dᴀᴛᴀ Qᴏᴛᴀ")
	await bot.send_message(user_id,"⛔️ Lᴀꜱᴛ Wᴀʀɴɪɴɢ ⛔️\n\n- Aᴄᴄᴏᴜɴᴛ Dᴏᴡɴɢʀᴀᴅᴇᴅ Tᴏ Lᴇᴠᴇʟ 𝟸\nYᴏᴜ Cᴀɴ Oɴʟʏ Uꜱᴇ 𝟷𝟶𝟶ᴍʙ/ᴅᴀʏ Fʀᴏᴍ Dᴀᴛᴀ Qᴏᴛᴀ.\n Cʜᴇᴄᴋ Yᴏᴜʀ Pʟᴀɴ Hᴇʀᴇ- /myplan\n- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 🦋<a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>🦋")

@Client.on_callback_query(filters.regex('cp3'))
async def cp3(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 0
	uploadlimit(int(user_id), 0)
	usertype(int(user_id),"**Pᴏᴡᴇʀ Cᴇᴀꜱᴇᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aʟʟ Pᴏᴡᴇʀ Cᴇᴀꜱᴇᴅ Fʀᴏᴍ Tʜᴇ Uꜱᴇʀ.\n Tʜɪꜱ Aᴄᴄᴏᴜɴᴛ Hᴀꜱ 𝟶 ᴍʙ Rᴇɴᴀᴍɪɴɢ Cᴀᴘᴀᴄɪᴛʏ")
	await bot.send_message(user_id,"🚫 Aʟʟ Pᴏᴡᴇʀ Cᴇᴀꜱᴇᴅ 🚫\n\n- Aʟʟ Pᴏᴡᴇʀ Hᴀꜱ Bᴇᴇɴ Cᴇᴀꜱᴇᴅ Fʀᴏᴍ Yᴏᴜ \n Fʀᴏᴍ Nᴏᴡ Yᴏᴜ Cᴀɴ'ᴛ Rᴇɴᴀᴍᴇ Fɪʟᴇꜱ Uꜱɪɴɢ Mᴇ\nCʜᴇᴄᴋ Yᴏᴜʀ Pʟᴀɴ Hᴇʀᴇ - /myplan\n- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 🦋<a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>🦋")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 21474836480
	uploadlimit(int(user_id), 21474836480)
	usertype(int(user_id),"**Fʀᴇᴇ**")
	addpre(int(user_id))
	await update.message.edit("Dᴀɪʟʏ Dᴀᴛᴀ Lɪᴍɪᴛ Hᴀꜱ Bᴇᴇɴ Rᴇꜱᴇᴛ Sᴜᴄᴄᴇꜱꜱꜱғᴜʟʟʏ.\nTʜɪꜱ Aᴄᴄᴏᴜɴᴛ Hᴀꜱ Dᴇғᴀᴜʟᴛ 𝟷.𝟸 GB Rᴇɴᴀᴍɪɴɢ Cᴀᴘᴀᴄɪᴛʏ ")
	await bot.send_message(user_id,"Yᴏᴜʀ Dᴀɪʟʏ Dᴀᴛᴀ Lɪᴍɪᴛ Hᴀꜱ Bᴇᴇɴ Rᴇꜱᴇᴛ Sᴜᴄᴄᴇꜱꜱꜱғᴜʟʟʏ.\n\nCʜᴇᴄᴋ Yᴏᴜʀ Pʟᴀɴ Hᴇʀᴇ - /myplan\n- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 🦋<a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>🦋")
