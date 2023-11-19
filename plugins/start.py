from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os
import re, asyncio, os, sys

CHANNEL = os.environ.get('CHANNEL', "Max_Leech_Zone_Update")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 6263893478))
bot_username = os.environ.get("BOT_USERNAME","public_renamerbot")
log_channel = int(os.environ.get("LOG_CHANNEL", "-1002066295284"))
token = os.environ.get('TOKEN', '6927866559:AAFCRzLBFtIrotS9iDsGK7DO9H9FPhL9F7c')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/76d2ce61434f88159952b.jpg")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = " **Gᴏᴏᴅ ᴍᴏʀɴɪɴɢ** "
elif 12 <= currentTime.hour < 12:
    wish = ' **Gᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ** '
else:
    wish = ' **Gᴏᴏᴅ ᴇᴠᴇɴɪɴɢ** '

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        m=await message.reply_sticker("CAACAgUAAxkBAAEB6w5lWnRbiLV7FZKlsEdGBhbn6VtadgACYAQAAioMGFT31AZIdDgfzB4E") 
        await asyncio.sleep(3)
        await m.delete()
        txt=f"""Hᴇʟʟᴏ {wish} {message.from_user.first_name } 🗿\n
	**➻ Wᴇʟᴄᴏᴍᴇ Tᴏ Pʀᴇᴍɪᴜᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ

• Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.
• Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇꜱ
• Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.
• Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.
•  Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB** \n\n /about **Tᴏ Kɴᴏᴡ Mᴏʀᴇ ☺️**"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("⚜ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url="https://t.me/Max_Leech_Zone_Update")],
                                      [InlineKeyboardButton(" 👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url='https://t.me/Noobseverywhere'),
                                      InlineKeyboardButton("🎥 Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ", url='https://t.me/mad_cinema')],
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Yᴏᴜʀ Fʀɪᴇɴᴅ ɪꜱ Aʟʀᴇᴀᴅʏ Uꜱɪɴɢ Oᴜʀ Bᴏᴛ 🙊")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("⚜ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ", url="https://t.me/Max_Leech_Zone_Update")],
                                              [InlineKeyboardButton(" 👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url='https://t.me/Noobseverywhere'),
                                             InlineKeyboardButton("🎥 Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ", url='https://t.me/mad_cinema')],
                                             ]))
            except:
                return
        else:
            await client.send_message(id, "🤩 𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐬! 𝐘𝐨𝐮 𝐖𝐨𝐧 𝟏𝟎𝟎𝐌𝐁 𝐔𝐩𝐥𝐨𝐚𝐝 𝐥𝐢𝐦𝐢𝐭")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	Hello {wish} {message.from_user.first_name }\n\n
	**➻ Wᴇʟᴄᴏᴍᴇ Tᴏ Pʀᴇᴍɪᴜᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ

• Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.
• Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇꜱ
• Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.
• Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.
•  Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB**  \n\n /about **Tᴏ Kɴᴏᴡ Mᴏʀᴇ ☺️**
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("⚜ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url="https://t.me/Max_Leech_Zone_Update")],
                                          [InlineKeyboardButton(" 👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url='https://t.me/Noobseverywhere'),
                                          InlineKeyboardButton(" 🎥 Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ", url='https://t.me/mad_cinema')],
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:	
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__𝗬𝗼𝘂 𝗔𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("⚜ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #rename_logs 🦋,\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n Uꜱᴇʀ-Pʟᴀɴ : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Rᴇꜱᴛʀɪᴄᴛ Uꜱᴇʀ ( PM ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Uꜱᴇ Aʙᴏᴜᴛ ᴄᴍᴅ Fɪʀꜱᴛ /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"Hello dear {message.from_user.first_name}  Wᴇ Aʀᴇ Cᴜʀʀᴇɴᴛʟʏ Wᴏʀᴋɪɴɢ Oɴ Tʜɪꜱ Iꜱꜱᴜᴇ \n\n Pʟᴇᴀꜱᴇ Tʀʏ Tᴏ Rᴇɴᴀᴍᴇ Fɪʟᴇꜱ Fʀᴏᴍ Yᴏᴜʀ Aɴᴏᴛʜᴇʀ Aᴄᴄᴏᴜɴᴛ.\n Bᴇᴄᴀᴜꜱᴇ Tʜɪꜱ BOT Cᴀɴ'ᴛ Rᴇɴᴀᴍᴇ Fɪʟᴇ Sᴇɴᴛ Bʏ Sᴏᴍᴇ Iᴅꜱ.\n\nIғ Yᴏᴜ Aʀᴇ Aɴ ADMIN Dᴏɴ'ᴛ Wᴏʀʀʏ ! Hᴇʀᴇ Wᴇ Hᴀᴠᴇ A Sᴏʟᴜᴛɪᴏɴ Fᴏʀ Yᴏᴜ Dᴇᴀʀ {message.from_user.first_name }.\n\n Pʟᴇᴀꜱᴇ Uꜱᴇ\n👉 `/addpremium ʏᴏᴜʀ_ᴏᴛʜᴇʀ_ᴜꜱᴇʀɪᴅ` 👈 Tᴏ Uꜱᴇ Pʀᴇᴍɪᴜᴍ Fᴇᴀᴜᴛʀᴇ\n\n",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("🦋 Contact Owner 🦋", url='https://telegram.me/mr_kallua')]                                                             
                                                                    ]))
        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 10
    else:
        LIMIT = 00
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sᴏʀʀʏ Dᴜᴅᴇ I Aᴍ Nᴏᴛ Oɴʟʏ Fᴏʀ YOU \nFʟᴏᴏᴅ Cᴏɴᴛʀᴏʟ Iꜱ Aᴄᴛɪᴠᴇ Aᴏ Pʟᴇᴀꜱᴇ Wᴀɪᴛ Fᴏʀ {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"**❗️ 𝟷𝟶𝟶% Oғ Dᴀɪʟʏ {humanbytes(limit)} Dᴀᴛᴀ Qᴜᴏᴛᴀ Exʜᴀᴜꜱᴛᴇᴅ**.\n\n 📁 Fɪʟᴇ Sɪᴢᴇ Dᴇᴛᴇᴄᴛᴇᴅ = {humanbytes(file.file_size)}\n ℹ️ Uꜱᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ = {humanbytes(used)}\n\n Yᴏᴜ Hᴀᴠᴇ Oɴʟʏ {humanbytes(remain)} Lᴇғᴛ Oɴ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ.\nIғ U Wᴀɴᴛ Tᴏ Rᴇɴᴀᴍᴇ Lᴀʀɢᴇ Fɪʟᴇ Yᴏᴜ Nᴇᴇᴅ Tᴏ Uᴘɢʀᴀᴅᴇ Yᴏᴜʀ Pʟᴀɴ 💡", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" Yᴏᴜ Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Mᴏʀᴇ Tʜᴇɴ {humanbytes(limit)} Uꜱᴇᴅ Dᴀɪʟʏ Lɪᴍɪᴛ {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Uᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪꜱ Fɪʟᴇ?__\n\n𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- <code>{filename}</code>\n𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲 :- {humanize.naturalsize(file.file_size)}\n𝗗𝗖 𝗜𝗗 :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Yᴏᴜʀ Pʟᴀɴ Exᴘɪʀᴇᴅ Oɴ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 𝟸GB 😔")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪꜱ Fɪʟᴇ?__\n\n𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- <code>{filename}</code>\n𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲:- {filesize}\n𝗗𝗖 𝗜𝗗 :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ", callback_data="cancel")]]))
