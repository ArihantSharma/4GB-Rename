from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("🔗 𝐒𝐡𝐚𝐫𝐞 𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤" ,url=f"https://t.me/share/url?url=https://t.me/public_renamerbot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Rᴇғᴇʀ Aɴᴅ Eᴀʀɴ Gᴇᴛ 𝟷𝟶𝟶MB Uᴘʟᴏᴀᴅ Lɪᴍɪᴛ \nPᴇʀ Rᴇғᴇʀ 𝟷𝟶𝟶MB\n Yᴏᴜʀ Lɪɴᴋ :- https://t.me/public_renamerbot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
