import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", ))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

log_channel = int(os.environ.get("LOG_CHANNEL", ""))

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
				   InlineKeyboardButton("🪙 Bᴀꜱɪᴄ", callback_data="vip1")
				   ], [
					InlineKeyboardButton("💫 Sᴛᴀɴᴅᴀʀᴅ", callback_data="vip2")
				   ], [
					InlineKeyboardButton("💎 Pʀᴇᴍɪᴜᴍ", callback_data="vip3")
					]]))
        			

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"ᴅᴏ  ʏᴏᴜ  ʀᴇᴀʟʟʏ  ᴡᴀɴᴛ  ᴛᴏ  ʀᴇꜱᴇᴛ  ʜɪꜱ  ʟɪᴍɪᴛ.",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton(" 𝐘𝐞𝐬   ✅ ",callback_data = "dft")],
				   [InlineKeyboardButton(" 𝐍𝐨   ❌ ",callback_data = "cancel")]
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
	inlimit  = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"💫 **Gᴏʟᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶 GB 🤝")
	await bot.send_message(user_id,"Hᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Gᴏʟᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 1073741824000
	uploadlimit(int(user_id), 1073741824000)
	usertype(int(user_id),"💎 **Dɪᴀᴍᴏɴᴅ**")
	addpre(int(user_id))
	await update.message.edit("Aᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Tᴏ Pʀᴇᴍɪᴜᴍ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶 GB 🤝")
	await bot.send_message(user_id,"Hᴇʏ ʏᴏᴜ ᴀʀᴇ Uᴘɢʀᴀᴅᴇᴅ Tᴏ Dɪᴀᴍᴏɴᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 2147483648
	uploadlimit(int(user_id), 1288490188)
	usertype(int(user_id),"**Free**")
	addpre(int(user_id))
	await update.message.edit("Dᴀɪʟʏ Dᴀᴛᴀ Lɪᴍɪᴛ Hᴀꜱ Bᴇᴇɴ Rᴇꜱᴇᴛ Sᴜᴄᴄᴇꜱꜱꜱғᴜʟʟʏ.\nTʜɪꜱ Aᴄᴄᴏᴜɴᴛ Hᴀꜱ Dᴇғᴀᴜʟᴛ 𝟷.𝟸 GB Rᴇɴᴀᴍɪɴɢ Cᴀᴘᴀᴄɪᴛʏ ")
	await bot.send_message(user_id,"Yᴏᴜʀ Dᴀɪʟʏ Dᴀᴛᴀ Lɪᴍɪᴛ Hᴀꜱ Bᴇᴇɴ Rᴇꜱᴇᴛ Sᴜᴄᴄᴇꜱꜱꜱғᴜʟʟʏ.\n\nCʜᴇᴄᴋ Yᴏᴜʀ Pʟᴀɴ Hᴇʀᴇ - /myplan\n- Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ 🦋<a href='https://t.me/mr_kallua'>₭𝐚𝐋𝐋Ꮼ𝐚 ...♡</a>🦋")
